from django.db import models

from tehnikum.abstract_models import BaseModel
from tehnikum.enums import Language, Type


class User(BaseModel):
    id = models.IntegerField(unique=True, primary_key=True)
    username = models.CharField(max_length=30)
    first_name = models.CharField(max_length=30)
    phone_number = models.CharField(max_length=30, blank=True, null=True)
    language = models.IntegerField(choices=Language.choices, default=Language.UNKNOWN)
    type = models.IntegerField(choices=Type.choices, default=Type.UNKNOWN)
    additional_data = models.CharField(max_length=511, blank=True, null=True)

    def __str__(self) -> str:
        return f"{self.username} - {self.first_name}"
