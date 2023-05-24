from rest_framework import generics, mixins
from rest_framework.permissions import IsAuthenticated
from rest_framework.request import Request
from rest_framework.parsers import MultiPartParser, FormParser


from authentication.models import Client

from .serializers import *


class JobCreateListView(
    generics.GenericAPIView, mixins.ListModelMixin, mixins.CreateModelMixin
):
    serializer_class = JobSerializer
    permission_classes = [IsAuthenticated]
    parser_classes = (MultiPartParser, FormParser)

    def get_queryset(self):
        client = Client.objects.get(user=self.request.user)

        return Job.objects.filter(posted_by=client).order_by("-created_at")

    def perform_create(self, serializer):
        client = Client.objects.get(user=self.request.user)

        serializer.save(posted_by=client)
        return super().perform_create(serializer)

    def get(self, request: Request, *args, **kwargs):
        return self.list(request, *args, **kwargs)

    def post(self, request: Request, *args, **kwargs):
        return self.create(request, *args, **kwargs)


class JobRetrieveUpdateView(
    generics.GenericAPIView,
    mixins.RetrieveModelMixin,
    mixins.UpdateModelMixin,
):
    serializer_class = JobSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        client = Client.objects.get(user=self.request.user)

        return Job.objects.filter(posted_by=client)

    def perform_update(self, serializer):
        serializer.save()
        return super().perform_update(serializer)

    def get(self, request: Request, *args, **kwargs):
        return self.retrieve(request, *args, **kwargs)

    def put(self, request: Request, *args, **kwargs):
        return self.update(request, *args, **kwargs)


class GetJobs(mixins.ListModelMixin, generics.GenericAPIView):
    queryset = Job.objects.filter(job_status="Running")
    serializer_class = GetJobSerializer

    def get(self, request, *args, **kwargs):
        return self.list(request, *args, **kwargs)


class GetJobsById(mixins.ListModelMixin, generics.GenericAPIView):
    serializer_class = GetJobSerializer

    def get_queryset(self):
        job = self.kwargs.get("pk")
        return Job.objects.filter(job_status="Running").filter(id=job)

    def get(self, request, *args, **kwargs):
        return self.list(request, *args, **kwargs)
