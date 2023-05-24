from django.db import models
from django.utils import timezone
from django.contrib.auth.models import AbstractUser
from django.contrib.auth.base_user import BaseUserManager


class CustomUserManager(BaseUserManager):
    use_in_migrations = True

    def create_user(self, email, password=None, **extra_fields):
        if not email:
            raise ValueError(("The Email must be set"))
        email = self.normalize_email(email)
        user = self.model(email=email, **extra_fields)
        user.set_password(password)
        user.save()
        return user

    def create_superuser(self, email, password, **extra_fields):
        extra_fields.setdefault("is_staff", True)
        extra_fields.setdefault("is_superuser", True)
        extra_fields.setdefault("is_active", True)

        if extra_fields.get("is_staff") is not True:
            raise ValueError(("Superuser must have is_staff=True."))
        if extra_fields.get("is_superuser") is not True:
            raise ValueError(("Superuser must have is_superuser=True."))
        return self.create_user(email, password, **extra_fields)


class User(AbstractUser):
    id = models.AutoField(
        primary_key=True,
    )
    is_verified = models.BooleanField(default=False)
    email = models.EmailField(max_length=80, unique=True)
    otp = models.CharField(max_length=6, null=True, blank=True)
    is_talent = models.BooleanField(default=False)
    is_client = models.BooleanField(default=False)
    date_joined = models.DateTimeField(default=timezone.now, verbose_name="date joined")

    objects = CustomUserManager()
    username = None
    first_name = None
    last_name = None
    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = []

    def __str__(self):
        return self.email


class Talent(models.Model):
    id = models.AutoField(
        primary_key=True,
    )
    user = models.OneToOneField(
        User,
        on_delete=models.CASCADE,
        related_name="Talent",
    )
    talent_name = models.CharField(max_length=120, blank=True, null=True)
    talent_title = models.CharField(max_length=120, blank=True, null=True)
    talent_bio = models.TextField(max_length=1000, blank=True, null=True)
    talent_email = models.CharField(max_length=120, blank=True, null=True)
    talent_country = models.CharField(max_length=255, blank=True, null=True)
    created_at = models.DateTimeField(default=timezone.now, verbose_name="Created At")

    def __str__(self):
        return str(self.user)


class Client(models.Model):
    id = models.AutoField(
        primary_key=True,
    )
    user = models.OneToOneField(
        User,
        on_delete=models.CASCADE,
        related_name="Client",
    )
    can_access_talents = models.BooleanField(default=False)
    created_at = models.DateTimeField(default=timezone.now, verbose_name="Created At")

    def __str__(self):
        return str(self.user)
