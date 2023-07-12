from rest_framework import serializers

from .models import Subscription, Webinar


class WebinarSerializer(serializers.ModelSerializer):
    class Meta:
        model = Webinar
        fields = "__all__"


class SubscriptionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Subscription
        fields = "__all__"
