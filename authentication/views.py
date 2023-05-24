from rest_framework.authtoken.models import Token
from rest_framework.permissions import IsAuthenticated
from rest_framework.decorators import (
    APIView,
    api_view,
    permission_classes,
)
from rest_framework.views import APIView
from rest_framework.request import Request
from rest_framework.response import Response
from rest_framework import generics, status, mixins
from django.contrib.auth import authenticate, logout

from .models import *
from .serializers import *
from .tokens import create_jwt_pair_for_user
from .emails import send_otp_via_email


class SignUpView(APIView):
    def post(self, request):
        try:
            data = request.data
            serializer = SignUpViewSerializer(data=data)

            if serializer.is_valid():
                serializer.save()

                send_otp_via_email(serializer.data["email"])

                response = {
                    "status": 201,
                    "message": "User Created Successfully. Check email.",
                    "data": serializer.data,
                }
                return Response(data=response, status=status.HTTP_201_CREATED)

            response = {
                "status": 400,
                "message": "something went wrong",
                "data": serializer.errors,
            }
            return Response(data=response, status=status.HTTP_400_BAD_REQUEST)

        except Exception as e:
            print(f"Exception: {e}")


class SignInView(APIView):
    def post(self, request):
        data = request.data
        serializer = SignInViewSerializer(data=data)

        if serializer.is_valid():
            email = serializer.data["email"]

            user = User.objects.filter(email=email)

            if not user.exists():
                response = {
                    "status": 400,
                    "message": "Something went wront!",
                    "data": "Invalid Email",
                }
                return Response(data=response, status=status.HTTP_400_BAD_REQUEST)

            send_otp_via_email(email)
            user = user.first()
            Token.objects.get_or_create(user=user)
            user.save()

            response = {
                "status": 200,
                "message": "OTP successfully sent. check your email",
                "data": {},
            }
            return Response(data=response, status=status.HTTP_200_OK)

        else:
            response = {
                "status": 400,
                "message": "Something is not working",
                "data": serializer.errors,
            }
            return Response(data=response, status=status.HTTP_400_BAD_REQUEST)


class VerifyOTP(APIView):
    def post(self, request):
        try:
            data = request.data
            serializer = VerifyOTPSerializer(data=data)

            if serializer.is_valid():
                email = serializer.data["email"]
                otp = serializer.data["otp"]

                user = authenticate(email=email)

                user = User.objects.filter(email=email)

                if not user.exists():
                    return Response(
                        {
                            "status": 400,
                            "message": "Something went wrong!",
                            "data": "Invalid Email",
                        }
                    )

                if user[0].otp != otp:
                    return Response(
                        {
                            "status": 400,
                            "message": "Something went wrong!",
                            "data": "Invalid OTP",
                        }
                    )

                user = user.first()
                user.is_verified = True
                user.save()

                tokens = create_jwt_pair_for_user(user)

                response = {
                    "status": 200,
                    "message": "Account verified and loggedin successfully.",
                    "data": tokens,
                }
                return Response(data=response, status=status.HTTP_200_OK)

            return Response(
                {
                    "status": 400,
                    "message": "Something went wrong!",
                    "data": serializer.errors,
                }
            )

        except Exception as e:
            print(f"Exception: {e}")


@api_view(["GET"])
@permission_classes([IsAuthenticated])
def User_logout(request):
    request.user.auth_token.delete()

    logout(request)

    return Response("User logged out successfully")


@api_view(["GET"])
@permission_classes([IsAuthenticated])
def get_user_type(request):
    type = {
        "talent": request.user.is_talent,
        "client": request.user.is_client,
    }

    return Response(data=type, status=status.HTTP_200_OK)


class TalentProfileView(
    generics.GenericAPIView,
    mixins.RetrieveModelMixin,
    mixins.UpdateModelMixin,
):
    serializer_class = TalentSerializer
    permission_classes = [IsAuthenticated]

    def get_object(self):
        user = self.request.user.id

        talent = Talent.objects.get(user=user)

        if talent != None:
            return talent

        else:
            return Response("Account not found")

    def get(self, request: Request, *args, **kwargs):
        return self.retrieve(request, *args, **kwargs)

    def put(self, request: Request, *args, **kwargs):
        return self.update(request, *args, **kwargs)


class ClientProfileView(
    generics.GenericAPIView,
    mixins.RetrieveModelMixin,
    mixins.UpdateModelMixin,
):
    serializer_class = ClientSerializer
    permission_classes = [IsAuthenticated]

    def get_object(self):
        user = self.request.user.id

        client = Client.objects.get(user=user)

        if client != None:
            return client

        else:
            return Response("Account not found")

    def get(self, request: Request, *args, **kwargs):
        return self.retrieve(request, *args, **kwargs)

    def put(self, request: Request, *args, **kwargs):
        return self.update(request, *args, **kwargs)
