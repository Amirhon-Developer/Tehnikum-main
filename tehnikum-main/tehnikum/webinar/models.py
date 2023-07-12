from django.db import models
from django.utils.safestring import mark_safe

from tehnikum.abstract_models import BaseModel

from ..user.models import User
from .validators import validate_image


class Webinar(BaseModel):
    name_uz = models.CharField(
        max_length=511,
        blank=True,
        null=True,
    )
    description_uz = models.TextField(blank=True, null=True)
    name_ru = models.CharField(max_length=511, blank=True, null=True)
    description_ru = models.TextField(blank=True, null=True)
    forward_uz = models.TextField(blank=True, null=True)
    forward_ru = models.TextField(blank=True, null=True)
    photo = models.ImageField(upload_to="pics", null=True, blank=True, validators=[validate_image])
    date = models.DateTimeField("Webinar date", null=True, blank=True)

    def image_tag(self):
        return mark_safe(f'<img src="/../../media/{self.photo}" width="150" height="150" />')


class Subscription(BaseModel):
    webinar = models.ForeignKey(Webinar, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    is_sent = models.BooleanField(default=False)

    class Meta:
        # does not make sense to have the same user to be subscribed to the same webinar
        unique_together = (
            "webinar",
            "user",
        )

    def __str__(self) -> str:
        return f"{self.user.username} - {self.webinar.id}"
