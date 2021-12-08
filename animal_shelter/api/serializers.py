from datetime import datetime as dt

from authentication.models import User, Worker
from django.db.models import Q
from profanity_check import predict
from pytz import UTC
from rest_framework import serializers
from shelter.models import Adoption, Animal, Cage, MeetingInfo, Photo, Reservation


class CustomSerializer(serializers.HyperlinkedModelSerializer):
    """Is adding extra fields to fields."""

    def get_field_names(self, declared_fields, info):
        expanded_fields = super(CustomSerializer, self).get_field_names(
            declared_fields, info
        )

        if getattr(self.Meta, "extra_fields", None):
            return expanded_fields + self.Meta.extra_fields
        else:
            return expanded_fields


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = [
            "url",
            "pk",
            "password",
            "username",
            "email",
            "first_name",
            "last_name",
            "phone",
            "city",
            "zip_code",
            "address_line1",
            "address_line2",
            "is_staff",
        ]

    def validate_first_name(self, value):
        """Check if first name has only letters and fist latter is capital."""
        if value.capitalize() != value:
            raise serializers.ValidationError(
                "First name should start with a capital letter.",
            )
        if not value.isalpha():
            raise serializers.ValidationError(
                "First name can not contain any digits.",
            )
        return value

    def validate_last_name(self, value):
        """Check if last name has only letters and fist latter is capital."""
        if value.capitalize() != value:
            raise serializers.ValidationError(
                "Last name should start with a capital letter.",
            )
        if not value.isalpha():
            raise serializers.ValidationError(
                "Last name can not contain any digits.",
            )
        return value

    def validate_city(self, value):
        """Check if city has only letters and fist latter is capital."""
        if value.capitalize() != value:
            raise serializers.ValidationError(
                "City should start with a capital letter.",
            )
        if not value.isalpha():
            raise serializers.ValidationError(
                "City can not contain any digits.",
            )
        return value


class UserSerializerWhenUpdate(UserSerializer):
    email = serializers.EmailField(read_only=True)

    class Meta:
        model = User
        fields = [
            "url",
            "pk",
            "password",
            "username",
            "email",
            "first_name",
            "last_name",
            "phone",
            "city",
            "zip_code",
            "address_line1",
            "address_line2",
        ]


class WorkerSerializer(UserSerializer):
    class Meta:
        model = Worker
        fields = [
            "url",
            "pk",
            "password",
            "username",
            "email",
            "first_name",
            "last_name",
            "phone",
            "city",
            "zip_code",
            "address_line1",
            "address_line2",
            "employment_date",
            "position",
            "contract_expiration_date",
            "bank_account_number",
            "wage",
            "status",
            "is_superuser",
            "is_staff",
        ]

    def validate_contract_expiration_date(self, value):
        """Check if contract expiration date is not before today."""
        if value.replace(tzinfo=UTC) == dt.now().replace(tzinfo=UTC) or value.replace(
            tzinfo=UTC
        ) < dt.now().replace(tzinfo=UTC):
            raise serializers.ValidationError(
                "Contract expiration date can't be set on this date.",
            )
        return value

    def validate_bank_account_number(self, value):
        """Check if bank account number has correct length and if have olny digitals."""
        if len(value) != 26:
            raise serializers.ValidationError(
                "Length of bank account number is incorrect.",
            )
        if not value.isdigit():
            raise serializers.ValidationError(
                "Bank account number sould have only numbers.",
            )
        return value

    def validate_wage(self, value):
        """Check if wage is not below 0."""
        if value < 0:
            raise serializers.ValidationError("Wage can't be below 0.")
        return value


class WorkerSerializerWhenUpdate(UserSerializerWhenUpdate, WorkerSerializer):
    class Meta:
        model = Worker
        fields = [
            "url",
            "pk",
            "password",
            "username",
            "email",
            "first_name",
            "last_name",
            "phone",
            "city",
            "zip_code",
            "address_line1",
            "address_line2",
            "employment_date",
            "position",
            "contract_expiration_date",
            "bank_account_number",
            "wage",
            "status",
            "is_superuser",
        ]


class CageSerializer(serializers.HyperlinkedModelSerializer):
    animals = serializers.HyperlinkedRelatedField(
        many=True, read_only=True, view_name="animal-detail"
    )

    class Meta:
        model = Cage
        fields = [
            "pk",
            "url",
            "cage_number",
            "space",
            "section",
            "species",
            "animals",
        ]

    def validate_cage_number(self, value):
        """Check if cage number 'x' not exist in specified section.
        Check if there is free space in that cage"""
        section = self.initial_data["section"][0]
        if Cage.objects.filter(section=section, cage_number=value).exists():
            raise serializers.ValidationError(
                f"Cage number {value} already exist in sector {self.initial_data['section'][0]}.",
            )
        return value


class AnimalSerializer(CustomSerializer):
    reservations = serializers.HyperlinkedRelatedField(
        many=True, read_only=True, view_name="reservation-detail"
    )
    adoptions = serializers.HyperlinkedRelatedField(
        many=True, read_only=True, view_name="adoption-detail"
    )
    photos = serializers.HyperlinkedRelatedField(
        many=True, read_only=True, view_name="photo-detail"
    )
    cage = serializers.SlugRelatedField(queryset=Cage.objects.all(), slug_field="name")
    cage = serializers.HyperlinkedRelatedField(
        many=False, read_only=True, view_name="animal-detail"
    )

    class Meta:
        model = Animal
        fields = "__all__"
        extra_fields = ["pk", "url"]

    def validate_name(self, value):
        """Check if name has only letters and fist latter is capital.
        Check if animal already exist."""
        if not value[0].isupper():
            raise serializers.ValidationError(
                "Name should start with a capital letter.",
            )
        if not all(x.isalpha() or x.isspace() for x in value):
            raise serializers.ValidationError(
                "Name can not contain any digits.",
            )
        if Animal.objects.filter(name=value).filter(~Q(pk=self.instance.pk)).exists():
            raise serializers.ValidationError(
                "Animal with that name already exist.",
            )
        return value

    def validate_age(self, value):
        """Check if age is not below 0 and not higher than 30."""
        if value < 0:
            raise serializers.ValidationError("Age can't be below 0.")
        if value > 30:
            raise serializers.ValidationError("Age can't be higher than 30.")
        return value

    def validate_description(self, value):
        values = value.split(" ")
        if sum(predict(values)) > 0:
            raise serializers.ValidationError("Description contains offensive words")
        return value

    def validate_estimate_year_of_birth(self, value):
        """Check if estimate year is 2000 or higher."""
        if value < 2000:
            raise serializers.ValidationError(
                "Year should be higher or equal to 2000.",
            )
        return value

    def validate_cage(self, value):
        link = self.initial_data["cage"]
        print(link)
        id = link[len(link) - 2 : len(link) - 1]
        initial_cage = Cage.objects.get(pk=id)
        how_many_cages = Animal.objects.filter(cage=initial_cage).filter(
            ~Q(pk=self.instance.pk)
        )
        if len(how_many_cages) >= initial_cage.space:
            raise serializers.ValidationError(
                f"Cage number {initial_cage.cage_number} in sector {initial_cage.section} has no free space.",
            )
        if self.initial_data["species"] != initial_cage.species:
            raise serializers.ValidationError(
                f"Can not put {self.initial_data['species']} in {initial_cage.species} cage.",
            )
        return value

    def validate_status(self, value):
        if value == Animal.Status.ADDOPTED or value == Animal.Status.UNAVAILABLE:
            adoptions = Adoption.objects.filter(
                animal__name=self.instance.name,
                status=Adoption.Status.READY_FOR_CONSIDERATION,
            )
            print(adoptions)
            for adopt in adoptions:
                adopt.status = Adoption.Status.DECLINED
                adopt.save()
        return value


class PhotoSerializer(serializers.ModelSerializer):
    animal = serializers.SlugRelatedField(
        queryset=Animal.objects.all(), slug_field="name"
    )
    animal = serializers.HyperlinkedRelatedField(
        many=False, read_only=True, view_name="animal-detail"
    )

    class Meta:
        model = Photo
        fields = "__all__"
        extra_fields = ["pk", "url"]

    def validate_alter(self, value):
        """Check if alter already exist"""
        if Photo.objects.filter(alter=value).exists():
            raise serializers.ValidationError(
                "Alter already exist.",
            )
        return value


class MeetingInfoSerializer(serializers.ModelSerializer):
    class Meta:
        model = MeetingInfo
        fields = "__all__"
        extra_fields = ["pk", "url"]


class ReservationSerializer(CustomSerializer):
    animal = serializers.SlugRelatedField(
        queryset=Animal.objects.all(),
        slug_field="name",
    )
    user = serializers.SlugRelatedField(
        queryset=User.objects.all(), slug_field="full_name"
    )
    worker = serializers.SlugRelatedField(
        queryset=Worker.objects.all(), slug_field="full_name"
    )
    animal = serializers.HyperlinkedRelatedField(
        many=False, read_only=True, view_name="animal-detail"
    )
    user = serializers.HyperlinkedRelatedField(
        many=False, read_only=True, view_name="user-detail"
    )
    worker = serializers.HyperlinkedRelatedField(
        many=False, read_only=True, view_name="worker-detail"
    )

    class Meta:
        model = Reservation
        fields = "__all__"
        extra_fields = ["pk", "url"]

    def validate_reservation_date(self, value):
        """Check reservation date is not before today."""
        if value.replace(tzinfo=UTC) == dt.now().replace(tzinfo=UTC) or value.replace(
            tzinfo=UTC
        ) < dt.now().replace(tzinfo=UTC):
            raise serializers.ValidationError(
                "Reservation date can't be set on this date.",
            )
        animal = Animal.objects.get(name=self.instance.animal.name)
        if (
            animal.status == Animal.Status.ADDOPTED
            or animal.status == Animal.Status.UNAVAILABLE
        ):
            raise serializers.ValidationError(
                "Can not set a meeting, animal is addopted or unavailable.",
            )
        reservations = (
            Reservation.objects.filter(reservation_date=value, animal=animal)
            .filter(~Q(pk=self.instance.pk))
            .exists()
        )
        adoptions = Adoption.objects.filter(adoption_date=value, animal=animal).exists()
        if reservations or adoptions:
            raise serializers.ValidationError(
                "Animal has meeting in that date.",
            )
        return value


class AdoptionSerializer(CustomSerializer):
    animal = serializers.SlugRelatedField(
        queryset=Animal.objects.all(),
        slug_field="name",
    )
    user = serializers.SlugRelatedField(
        queryset=User.objects.all(), slug_field="full_name"
    )
    worker = serializers.SlugRelatedField(
        queryset=Worker.objects.all(), slug_field="full_name"
    )
    animal = serializers.HyperlinkedRelatedField(
        many=False, read_only=True, view_name="animal-detail"
    )
    user = serializers.HyperlinkedRelatedField(
        many=False, read_only=True, view_name="user-detail"
    )
    worker = serializers.HyperlinkedRelatedField(
        many=False, read_only=True, view_name="worker-detail"
    )
    agreement = serializers.BooleanField(read_only=True)
    ID_series_and_number = serializers.CharField(max_length=9, read_only=True)

    class Meta:
        model = Adoption
        fields = "__all__"
        extra_fields = ["pk", "url"]

    def validate_adoption_date(self, value):
        """Check if adoption date is not before today.
        Also check animal don't have an adoption or reservation
        in that day."""
        if value.replace(tzinfo=UTC) == dt.now().replace(tzinfo=UTC) or value.replace(
            tzinfo=UTC
        ) < dt.now().replace(tzinfo=UTC):
            raise serializers.ValidationError(
                "Adoption date can't be set on this date.",
            )
        animal = Animal.objects.get(name=self.instance.animal.name)
        if (
            animal.status == Animal.Status.ADDOPTED
            or animal.status == Animal.Status.UNAVAILABLE
        ):
            raise serializers.ValidationError(
                "Can not set a meeting, animal is addopted or unavailable.",
            )
        reservations = Reservation.objects.filter(
            reservation_date=value, animal=animal
        ).exists()
        adoptions = (
            Adoption.objects.filter(adoption_date=value, animal=animal)
            .filter(~Q(pk=self.instance.pk))
            .exists()
        )
        if reservations or adoptions:
            raise serializers.ValidationError(
                "Animal has meeting in that date.",
            )
        return value
