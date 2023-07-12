import requests
from decouple import config
from django.contrib import admin
from django.http import HttpResponseRedirect

from ..enums import Language
from ..user.models import User
from ..webinar.utils import send_telegram_webinar
from .models import Subscription, Webinar


@admin.register(Webinar)
class WebinarAdmin(admin.ModelAdmin):
    change_form_template = "webinar/webinar_send.html"

    list_display = ["name_uz", "description_uz", "name_ru", "description_ru", "image_tag", "date"]

    def response_change(self, request, obj):
        if "_webinar_send" in request.POST:
            all_users = User.objects.all()
            for user in all_users:
                send_telegram_webinar(user=user, webinar=obj)
            self.message_user(request, f"Webinar is sent to all users")
            return HttpResponseRedirect(".")
        return super().response_change(request, obj)


@admin.register(Subscription)
class SubscriptionAdmin(admin.ModelAdmin):
    pass
