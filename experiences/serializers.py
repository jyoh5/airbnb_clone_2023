from rest_framework.serializers import ModelSerializer
from .models import Perk, Experience
from users.serializers import TinyUserSerializer
from categories.serializers import CategorySerializer


class PerkSerializer(ModelSerializer):
    class Meta:
        model = Perk
        fields = (
            "name",
            "detail",
            "explanation",
        )


class ExperienceListSerializer(ModelSerializer):
    class Meta:
        model = Experience
        fields = (
            "name",
            "description",
            "country",
            "city",
            "price",
            "start",
            "end",
        )


class ExperienceDetailSerializer(ModelSerializer):
    host = TinyUserSerializer(read_only=True)
    perks = PerkSerializer(read_only=True, many=True)
    category = CategorySerializer(read_only=True)

    class Meta:
        model = Experience
        fields = "__all__"
