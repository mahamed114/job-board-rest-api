from django.urls import path


from .views import *

urlpatterns = [
    path("api/subscribe-talent/", SubscriberAddView.as_view(), name="subscribe-talent"),
    path("api/unsubscribe-talent/", unsubscribe_talent, name="unsubscribe-talent"),
]
