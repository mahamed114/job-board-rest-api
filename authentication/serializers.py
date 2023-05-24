from rest_framework.response import Response
from rest_framework.authtoken.models import Token
from rest_framework import serializers
from rest_framework import status

from .models import *


class SignUpViewSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ["email", "is_talent", "is_client"]

    def validate(self, attrs):
        email_exists = User.objects.filter(email=attrs["email"]).exists()

        if email_exists:
            return Response(
                data="Email has already been used", status=status.HTTP_400_BAD_REQUEST
            )

        return super().validate(attrs)

    def create(self, validated_data):
        user = super().create(validated_data)
        user.save()

        Token.objects.create(user=user)
        Client.objects.create(user=user)
        Talent.objects.create(user=user)

        return user


class SignInViewSerializer(serializers.ModelSerializer):
    email = serializers.EmailField()

    class Meta:
        model = User
        fields = ["email"]


class VerifyOTPSerializer(serializers.Serializer):
    email = serializers.EmailField()
    otp = serializers.CharField()


class TalentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Talent
        fields = [
            "id",
            "user",
            "talent_name",
            "talent_title",
            "talent_bio",
            "talent_email",
            "talent_country",
            "created_at",
        ]


class ClientSerializer(serializers.ModelSerializer):
    class Meta:
        model = Client
        fields = [
            "id",
            "user",
            "can_access_talents",
            "created_at",
        ]
