from django.utils import timezone
from rest_framework import serializers
from rest_framework.serializers import ModelSerializer
from .models import Booking


class PublicBookingSerializer(ModelSerializer):
    class Meta:
        model = Booking
        fields = (
            "pk",
            "check_in",
            "check_out",
            "experience_time",
            "guests",
        )


class CreateRoomBookingSerializer(ModelSerializer):
    check_in = serializers.DateField()
    check_out = serializers.DateField()

    def validate_check_in(self, value):
        now = timezone.localdate(timezone.now())
        print(value, now)
        if value <= now:
            raise serializers.ValidationError("Can't book in the past!")
        return value

    def validate_check_out(self, value):
        now = timezone.localdate(timezone.now())
        if value <= now:
            raise serializers.ValidationError("Can't book in the past!")
        return value

    def validate(self, attrs):
        room = self.context.get("room")
        if attrs["check_in"] >= attrs["check_out"]:
            raise serializers.ValidationError(
                "Check in should be smaller than check out."
            )

        if Booking.objects.filter(
            room=room,
            check_in__lte=attrs["check_out"],
            check_out__gte=attrs["check_in"],
        ).exists():
            raise serializers.ValidationError("Some of dates are already taken.")
        return super().validate(attrs)

    class Meta:
        model = Booking
        fields = (
            "check_in",
            "check_out",
            "guests",
        )
