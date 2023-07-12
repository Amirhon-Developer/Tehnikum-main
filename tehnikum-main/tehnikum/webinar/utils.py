from datetime import datetime, timedelta
from logging import getLogger

import requests
from decouple import config

from ..enums import Language
from ..user.models import User
from .models import Subscription, Webinar

TELEGRAM_BOT_TOKEN: str = config("TELEGRAM_BOT_TOKEN")
BASE_URL: str = config("BASE_URL")
logger = getLogger(__name__)


def send_telegram_webinar(user: User, webinar: Webinar):
    # photo_url: str = request.build_absolute_uri(webinar.photo.url)
    photo_url: str = f"{BASE_URL}{webinar.photo.url}"
    description = webinar.forward_uz if user.language == Language.UZ else webinar.forward_ru
    params = f"chat_id={user.id}&photo={photo_url}&caption={description}"
    base_url: str = f"https://api.telegram.org/bot{TELEGRAM_BOT_TOKEN}/sendPhoto?{params}"
    r = requests.post(url=base_url)
    logger.debug(r.text)
    logger.debug(r.status_code)


def notify_webinars():
    logger.debug(f"Sending subscriptions to users")
    subscriptions = Subscription.objects.filter(is_sent=False, webinar__date__gt=datetime.now() - timedelta(hours=24))
    logger.debug(f"Sending {len(subscriptions)} subscriptions to users")

    for subscription in subscriptions:
        user = User.objects.get(id=subscription.user.id)
        webinar = Webinar.objects.get(id=subscription.webinar.id)

        send_telegram_webinar(user=user, webinar=webinar)
        subscription.is_sent = True
        subscription.save()
