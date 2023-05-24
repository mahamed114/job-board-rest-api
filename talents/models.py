from django.db import models


from authentication.models import Talent


class Education(models.Model):
    id = models.AutoField(primary_key=True)
    education_for = models.ForeignKey(
        Talent, on_delete=models.CASCADE, related_name="Education"
    )
    education_school = models.CharField(max_length=120)
    education_level = models.CharField(max_length=120)
    education_field = models.CharField(max_length=120)
    start_date = models.CharField(max_length=50)
    end_date = models.CharField(max_length=50)
    education_created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.education_school


class Experience(models.Model):
    id = models.AutoField(primary_key=True)
    experience_for = models.ForeignKey(
        Talent, on_delete=models.CASCADE, related_name="Experience"
    )
    start_date = models.CharField(max_length=50)
    end_date = models.CharField(max_length=50)
    currently_working = models.BooleanField(default=False)
    experience_title = models.CharField(max_length=120)
    experience_company = models.CharField(max_length=120)
    experience_details = models.TextField(max_length=1000, blank=True, null=True)
    experience_created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.experience_title


class Certificate(models.Model):
    id = models.AutoField(primary_key=True)
    certificate_for = models.ForeignKey(
        Talent, on_delete=models.CASCADE, related_name="Certificate"
    )
    certificate_name = models.CharField(max_length=120)
    issue_date = models.CharField(max_length=50)
    expiration_date = models.CharField(max_length=50)
    issuing_organization = models.CharField(max_length=120)
    certificate_created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.certificate_name
