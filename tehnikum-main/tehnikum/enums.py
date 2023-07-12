from django.db import models


class Language(models.IntegerChoices):
    UNKNOWN = 0
    UZ = 1
    RU = 2


class Type(models.IntegerChoices):
    UNKNOWN = 0
    STUDENT = 1
    PARENT = 2
    PUPIL = 3
    JOB_SEEKER = 4
