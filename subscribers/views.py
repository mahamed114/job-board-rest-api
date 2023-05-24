from rest_framework import generics, mixins
from rest_framework.request import Request
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import generics, status, mixins
from .serializers import SubscriberSerializer
from .models import Subscriber


class SubscriberAddView(generics.GenericAPIView, mixins.CreateModelMixin):
    serializer_class = SubscriberSerializer

    def post(self, request: Request, *args, **kwargs):
        return self.create(request, *args, **kwargs)


@api_view(["POST"])
def unsubscribe_talent(request):
    subscriber = Subscriber.objects.filter(email=request.data["email"])
    if subscriber.exists():
        Subscriber.objects.filter(email=request.data["email"]).delete()
        return Response(data="subscriber removed", status=status.HTTP_204_NO_CONTENT)

    return Response(data="Bad Request", status=status.HTTP_400_BAD_REQUEST)
