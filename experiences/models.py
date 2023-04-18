from django.db import models
from common.models import CommonModel


class Experience(CommonModel):

    """Experiences Definition"""

    name = models.CharField(max_length=250)
    description = models.TextField()
    country = models.CharField(max_length=50, default="한국")
    city = models.CharField(max_length=80, default=" 서울")
    host = models.ForeignKey(
        "users.User",
        on_delete=models.CASCADE,
        related_name="experiences",
    )
    price = models.PositiveIntegerField()
    address = models.CharField(max_length=250)
    start = models.TimeField()
    end = models.TimeField()
    perks = models.ManyToManyField(
        "experiences.Perk",
        related_name="experiences",
    )
    category = models.ForeignKey(
        "categories.Category",
        null=True,
        blank=True,
        on_delete=models.SET_NULL,
        related_name="experiences",
    )

    def __str__(self):
        return self.name


class Perk(CommonModel):

    """What is inclued on an Experience"""

    name = models.CharField(max_length=100)
    detail = models.CharField(max_length=250, null=True, blank=True)
    explanation = models.TextField(null=True, blank=True)

    def __str__(self):
        return self.name
