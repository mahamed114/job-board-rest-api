from rest_framework import serializers

from .models import Job


class JobSerializer(serializers.ModelSerializer):
    class Meta:
        model = Job
        fields = [
            "id",
            "created_at",
            "job_status",
            "posted_by",
            "job_title",
            "job_description",
            "job_apply_url",
            "job_primary_tag",
            "job_tags",
            "job_locations",
            "job_type",
            "job_workspace_type",
            "job_posted_at",
            "job_salary",
            "featured",
            "email_blasted",
            "is_featured",
            "post_price",
            "post_note",
            "post_invoice_name",
            "post_invoice_address",
            "post_invoice_email",
            "client_name",
            "client_contact",
            "client_website",
            "logo",
        ]


class GetJobSerializer(serializers.ModelSerializer):
    class Meta:
        model = Job
        fields = [
            "id",
            "created_at",
            "job_title",
            "job_description",
            "job_apply_url",
            "job_primary_tag",
            "job_tags",
            "job_locations",
            "job_type",
            "job_workspace_type",
            "job_posted_at",
            "job_salary",
            "featured",
            "email_blasted",
            "is_featured",
            "client_name",
            "client_contact",
            "client_website",
            "logo",
        ]
