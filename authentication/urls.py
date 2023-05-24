from django.urls import path


from .views import *

urlpatterns = [
    path("api/auth/signup/", SignUpView.as_view(), name="signup"),
    path("api/auth/signin/", SignInView.as_view(), name="signin"),
    path("api/auth/verify/", VerifyOTP.as_view(), name="verify"),
    path("api/auth/logout/", User_logout, name="logout"),
    path(
        "api/auth/client/account/", ClientProfileView.as_view(), name="client-account"
    ),
    path(
        "api/auth/talent/profile/", TalentProfileView.as_view(), name="client-account"
    ),
    path("api/auth/getusertype/", get_user_type, name="getusertype"),
]
