from rest_framework.permissions import IsAuthenticated
from rest_framework.request import Request
from rest_framework import generics, mixins


from authentication.models import Talent

from .models import *
from .serializers import *


class EducationCreateListView(
    generics.GenericAPIView, mixins.ListModelMixin, mixins.CreateModelMixin
):
    serializer_class = EducationSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        talent = Talent.objects.get(user=self.request.user.id)
        return Education.objects.filter(education_for=talent)

    def get(self, request: Request, *args, **kwargs):
        return self.list(request, *args, **kwargs)

    def post(self, request: Request, *args, **kwargs):
        return self.create(request, *args, **kwargs)


class ExperienceCreateListView(
    generics.GenericAPIView, mixins.ListModelMixin, mixins.CreateModelMixin
):
    serializer_class = ExperienceSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        talent = Talent.objects.get(user=self.request.user.id)
        return Experience.objects.filter(experience_for=talent)

    def get(self, request: Request, *args, **kwargs):
        return self.list(request, *args, **kwargs)

    def post(self, request: Request, *args, **kwargs):
        return self.create(request, *args, **kwargs)


class CertificateCreateListView(
    generics.GenericAPIView, mixins.ListModelMixin, mixins.CreateModelMixin
):
    serializer_class = CertificateSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        talent = Talent.objects.get(user=self.request.user.id)
        return Certificate.objects.filter(certificate_for=talent)

    def get(self, request: Request, *args, **kwargs):
        return self.list(request, *args, **kwargs)

    def post(self, request: Request, *args, **kwargs):
        return self.create(request, *args, **kwargs)


class GetTalents(mixins.ListModelMixin, generics.GenericAPIView):
    queryset = Talent.objects.all()
    serializer_class = GetTalentSerializer

    def get(self, request, *args, **kwargs):
        return self.list(request, *args, **kwargs)


class GetTalentById(mixins.ListModelMixin, generics.GenericAPIView):
    serializer_class = GetTalentSerializer

    def get_queryset(self):
        talent = self.kwargs.get("pk")
        return Talent.objects.filter(id=talent)

    def get(self, request, *args, **kwargs):
        return self.list(request, *args, **kwargs)


class GetTalentExperiences(mixins.ListModelMixin, generics.GenericAPIView):
    serializer_class = ExperienceSerializer

    def get_queryset(self):
        talent = self.request.query_params.get("talent") or None
        return Experience.objects.filter(experience_for=talent)

    def get(self, request, *args, **kwargs):
        return self.list(request, *args, **kwargs)


class GetTalentEducations(mixins.ListModelMixin, generics.GenericAPIView):
    serializer_class = EducationSerializer

    def get_queryset(self):
        talent = self.request.query_params.get("talent") or None
        return Education.objects.filter(education_for=talent)

    def get(self, request, *args, **kwargs):
        return self.list(request, *args, **kwargs)


class GetTalentCertificates(mixins.ListModelMixin, generics.GenericAPIView):
    serializer_class = CertificateSerializer

    def get_queryset(self):
        talent = self.request.query_params.get("talent") or None
        return Certificate.objects.filter(certificate_for=talent)

    def get(self, request, *args, **kwargs):
        return self.list(request, *args, **kwargs)
