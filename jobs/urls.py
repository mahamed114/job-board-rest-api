from django.urls import path


from .views import *

urlpatterns = [
    path("api/jobs/", JobCreateListView.as_view(), name="jobs-createlist"),
    path("api/job/<pk>/", JobRetrieveUpdateView.as_view(), name="update-job"),
    path("api/jobs/get-jobs/", GetJobs.as_view(), name="get-jobs"),
    path("api/jobs/get-job/<pk>/", GetJobsById.as_view(), name="get-job"),
]
