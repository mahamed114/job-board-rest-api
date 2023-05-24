from django.db import models
from django.contrib.postgres import fields as PostgresFields
from django.utils import timezone
from django.utils.translation import gettext_lazy as _


from authentication.models import Client


class Job(models.Model):
    class Status(models.TextChoices):
        REVIEW = ("Review", _("Review"))
        RUNNING = ("Running", _("Running"))
        FINISHED = ("Finished", _("Finished"))
        SUSPENDED = ("Suspended", _("Suspended"))

    id = models.AutoField(
        primary_key=True,
    )
    created_at = models.DateTimeField(default=timezone.now, verbose_name="Created At")
    job_status = models.CharField(
        max_length=9,
        choices=Status.choices,
        default=Status.REVIEW,
    )
    posted_by = models.ForeignKey(
        Client,
        on_delete=models.CASCADE,
        related_name="Post",
    )
    job_title = models.CharField(max_length=120)
    job_description = models.TextField(max_length=99000)
    job_apply_url = models.CharField(max_length=120)
    job_primary_tag = models.CharField(max_length=50)
    job_tags = PostgresFields.ArrayField(
        models.CharField(max_length=50, null=True, blank=True), blank=True, null=True
    )
    job_locations = PostgresFields.ArrayField(
        models.CharField(max_length=50, null=True, blank=True), blank=True, null=True
    )
    job_type = models.CharField(max_length=20)
    job_workspace_type = models.CharField(max_length=20)
    job_posted_at = models.CharField(max_length=20)
    job_salary = models.CharField(max_length=20)
    featured = models.CharField(max_length=7, blank=True, null=True)
    email_blasted = models.BooleanField(default=False)
    is_featured = models.BooleanField(default=False)
    post_price = models.CharField(max_length=20, blank=True, null=True)
    post_note = models.CharField(max_length=255, blank=True, null=True)
    post_invoice_name = models.CharField(max_length=120, blank=True, null=True)
    post_invoice_address = models.CharField(max_length=255, blank=True, null=True)
    post_invoice_email = models.CharField(max_length=120, blank=True, null=True)
    client_name = models.CharField(max_length=80, blank=True, null=True)
    client_contact = models.CharField(max_length=50, blank=True, null=True)
    client_website = models.CharField(max_length=80, blank=True, null=True)
    logo = models.ImageField(upload_to="logos/", blank=True, null=True)

    def __str__(self):
        return self.job_title

    class Meta:
        ordering = ["-created_at"]
