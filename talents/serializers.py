from rest_framework import serializers


from authentication.models import Talent

from .models import *


class EducationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Education
        fields = [
            "id",
            "education_for",
            "education_school",
            "education_level",
            "education_field",
            "start_date",
            "end_date",
            "education_created",
        ]


class ExperienceSerializer(serializers.ModelSerializer):
    class Meta:
        model = Experience
        fields = [
            "id",
            "experience_for",
            "currently_working",
            "experience_title",
            "experience_company",
            "experience_details",
            "start_date",
            "end_date",
            "experience_created",
        ]


class CertificateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Certificate
        fields = [
            "id",
            "certificate_for",
            "certificate_name",
            "issue_date",
            "expiration_date",
            "issuing_organization",
            "certificate_created",
        ]


class GetTalentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Talent
        fields = [
            "id",
            "talent_name",
            "talent_title",
            "talent_bio",
            "talent_email",
            "talent_country",
            "created_at",
        ]
