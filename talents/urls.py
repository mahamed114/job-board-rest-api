from django.urls import path


from .views import *

urlpatterns = [
    path(
        "api/talents/educations/",
        EducationCreateListView.as_view(),
        name="educations",
    ),
    path(
        "api/talents/experiences/",
        ExperienceCreateListView.as_view(),
        name="experiences",
    ),
    path(
        "api/talents/certificates/",
        CertificateCreateListView.as_view(),
        name="certificate",
    ),
    path("api/talents/get-talents/", GetTalents.as_view(), name="get-talents"),
    path("api/talents/get-talent/<pk>/", GetTalentById.as_view(), name="get-talent"),
    path(
        "api/talents/get-experiences/",
        GetTalentExperiences.as_view(),
        name="get-experiences",
    ),
    path(
        "api/talents/get-educations/",
        GetTalentEducations.as_view(),
        name="get-educations",
    ),
    path(
        "api/talents/get-certificates/",
        GetTalentCertificates.as_view(),
        name="get-ertificates",
    ),
]
