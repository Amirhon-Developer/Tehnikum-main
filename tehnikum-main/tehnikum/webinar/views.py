from rest_framework import permissions, viewsets
from rest_framework.response import Response
from rest_framework.views import APIView

from tehnikum.enums import Language
from tehnikum.user.models import User

from .models import Subscription, Webinar
from .serializers import SubscriptionSerializer, WebinarSerializer


class WebinarViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """

    queryset = Webinar.objects.all()
    serializer_class = WebinarSerializer
    permission_classes = [permissions.IsAuthenticated]


class SubscriptionViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """

    permission_classes = [permissions.IsAuthenticated]
    queryset = Subscription.objects.all()
    serializer_class = SubscriptionSerializer
