from rest_framework import serializers
from rest_framework.serializers import ModelSerializer
from .models import User
from rooms.models import Room


class TinyUserSerializer(ModelSerializer):
    class Meta:
        model = User
        fields = ("name", "avatar", "username")


class PrivateUserSerializer(ModelSerializer):
    class Meta:
        model = User
        exclude = (
            "password",
            "id",
            "is_superuser",
            "is_staff",
            "is_active",
            "first_name",
            "last_name",
            "groups",
            "user_permissions",
        )


class PublicUserSerializer(ModelSerializer):
    owned_rooms = serializers.SerializerMethodField()

    def get_owned_rooms(self, user):
        return Room.objects.filter(owner=user).count()

    class Meta:
        model = User
        # exclude = (
        #     "password",
        #     "id",
        #     "is_superuser",
        #     "is_staff",
        #     "is_active",
        #     "first_name",
        #     "last_name",
        #     "groups",
        #     "user_permissions",
        # )
        fields = (
            "username",
            "email",
            "name",
            "is_host",
            "gender",
            "language",
            "currency",
            "owned_rooms",
        )
