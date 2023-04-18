from django.db import models
from django.contrib.auth.models import AbstractUser


class User(AbstractUser):

    """User Models"""

    GENDER = (("male", "Male"), ("female", "Female"))

    class GenderChoices(models.TextChoices):
        MALE = (
            "male",
            "Male",
        )  # db value(=> max_length보다 작아야 함), label for admin panel
        FEMALE = ("female", "Female")

    class LanguageChoices(models.TextChoices):
        KR = ("kr", "Korean")
        EN = ("en", "English")

    class CurrencyChoices(models.TextChoices):
        WON = "won", "Korean Won"
        USD = ("usd", "Dollar")

    first_name = models.CharField(max_length=150, editable=False)
    last_name = models.CharField(max_length=150, editable=False)
    avatar = models.URLField(blank=True)
    name = models.CharField(max_length=150, default="")
    is_host = models.BooleanField(default=False)
    gender = models.CharField(max_length=10, choices=GENDER)
    language = models.CharField(max_length=2, choices=LanguageChoices.choices)
    currency = models.CharField(max_length=5, choices=CurrencyChoices.choices)
