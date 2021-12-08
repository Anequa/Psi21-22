from datetime import datetime as dt

from authentication.models import User, Worker
from pytz import UTC
from rest_framework import serializers
from shelter.models import Adoption, Animal, Cage, MeetingInfo, Photo, Reservation


class UserSerializer(serializers.ModelSerializer):

    email = serializers.EmailField()

    class Meta:
        model = User
        fields = "__all__"

    # def validate_email(self, values):
    #     if values != self.email:
    #         raise serializers.ValidationError(
    #             "You can't change your email.",
    #         )
    #     return values


class WorkerSerializer(serializers.ModelSerializer):

    contract_expiration_date = serializers.DateTimeField()
    bank_account_number = serializers.CharField(max_length=26)
    wage = serializers.IntegerField()

    class Meta:
        model = Worker
        fields = "__all__"

    def validate_contract_expiration_date(self, value):
        if value.replace(tzinfo=UTC) == dt.now().replace(tzinfo=UTC) or value.replace(
            tzinfo=UTC
        ) < dt.now().replace(tzinfo=UTC):
            raise serializers.ValidationError(
                "Contract expiration date can't be set on this date.",
            )
        return value

    def validate_bank_account_number(self, value):
        """Check if bank account number has correct length."""
        if len(value) != 26:
            raise serializers.ValidationError(
                "Length of bank account number is incorrect.",
            )
        return value

    def validate_wage(self, value):
        """Check if wage is not below 0."""
        if value < 0:
            raise serializers.ValidationError("Wage can't be below 0.")
        return value


class CageSerializer(serializers.ModelSerializer):
    space = serializers.IntegerField()

    class Meta:
        model = Cage
        fields = "__all__"


class AnimalSerializer(serializers.ModelSerializer):
    age = serializers.IntegerField()
    description = serializers.CharField(max_length=255)

    class Meta:
        model = Animal
        fields = "__all__"


class PhotoSerializer(serializers.ModelSerializer):
    alter = serializers.CharField(max_length=30)

    class Meta:
        model = Photo
        fields = "__all__"


class MeetingInfoSerializer(serializers.ModelSerializer):
    alter = serializers.CharField(max_length=30)
    # worker = serializers.PrimaryKeyRelatedField()
    # animal = serializers.PKOnlyObject

    # do spr co ktore robi

    class Meta:
        model = MeetingInfo
        fields = "__all__"


class ReservationSerializer(serializers.ModelSerializer):
    reservation_date = serializers.DateTimeField()

    class Meta:
        model = Reservation
        fields = "__all__"


class AdoptionSerializer(serializers.ModelSerializer):
    adoption_date = serializers.DateTimeField()
    ID_series_and_number = serializers.CharField(max_length=9)
    agreement = serializers.BooleanField()

    class Meta:
        model = Adoption
        fields = "__all__"
