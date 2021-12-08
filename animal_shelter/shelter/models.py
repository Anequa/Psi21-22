# from django.contrib.auth.models import AbstractUser
from authentication.models import User, Worker
from django.core.validators import RegexValidator
from django.db import models

# from django.utils.translation import gettext_lazy as _


class Species(models.TextChoices):
    DOG = "Dog"
    CAT = "Cat"


class Section(models.TextChoices):
    A = "A"
    B = "B"
    C = "C"
    D = "D"


class Cage(models.Model):
    section = models.CharField(
        max_length=3,
        verbose_name="section",
        choices=Section.choices,
    )
    space = models.IntegerField(
        verbose_name="space",
        default=1,
    )
    species = models.CharField(
        max_length=3,
        verbose_name="species",
        choices=Species.choices,
    )

    def __str__(self):
        return (
            str(self.pk)
            + ":"
            + str(self.species)
            + " - "
            + str(self.section)
            + ":"
            + str(self.space)
        )


class Animal(models.Model):
    species = models.CharField(
        max_length=3,
        verbose_name="species",
        choices=Species.choices,
    )
    name_regex = RegexValidator(
        regex=r"^[A-Z][a-z]+$",
        message="Name must start with upper letter and can not have numbers",
    )
    name = models.TextField(
        validators=[name_regex],
        verbose_name="name",
        max_length=45,
    )
    age = models.IntegerField(
        verbose_name="age",
    )

    class Gender(models.TextChoices):
        FEMALE = "female"
        MALE = "male"

    gender = models.CharField(
        max_length=6,
        verbose_name="gender",
        choices=Gender.choices,
    )

    class Size(models.TextChoices):
        SMALL = "Small"
        MEDIUM = "Medium"
        BIG = "Big"

    size = models.CharField(
        max_length=10,
        verbose_name="size",
        choices=Size.choices,
    )
    description = models.TextField(
        verbose_name="description",
        null=True,
        blank=True,
        default="Opis jeszcze nie zamieszczony",
    )
    date_of_arrival = models.DateTimeField(
        auto_now_add=True,
        verbose_name="date of arrival",
    )
    estimate_year_of_birth = models.IntegerField(
        verbose_name="estimate year of birth",
    )

    class Status(models.TextChoices):
        ADDOPTED = "addopted"
        RESERVED = "reserved"
        UNAVAILABLE = "unavailable"
        AVAILABLE = "available"

    status = models.CharField(
        max_length=15,
        verbose_name="status",
        choices=Status.choices,
        default=Status.AVAILABLE,
    )

    cage = models.ForeignKey(
        Cage,
        verbose_name="cage",
        null=True,
        on_delete=models.SET_NULL,
    )

    def __str__(self):
        return (
            str(self.pk)
            + " | "
            + self.name
            + " | "
            + self.species
            + " | "
            + self.gender
        )


class Photo(models.Model):
    alter = models.TextField(
        max_length=30,
        verbose_name="alternativer description",
    )
    photo = models.ImageField(
        upload_to="animal",
        verbose_name="photo",
    )

    animal = models.ForeignKey(
        Animal,
        verbose_name="animal",
        on_delete=models.SET_NULL,
        null=True,
    )

    def __str__(self):
        return str(self.pk) + " | " + self.zwierze + " | " + self.alter


class MeetingInfo(models.Model):
    create_date = models.DateTimeField(
        verbose_name="create date",
        auto_now_add=True,
    )
    animal = models.ForeignKey(
        Animal,
        verbose_name="animal",
        on_delete=models.CASCADE,
    )
    user = models.ForeignKey(
        User,
        null=True,
        related_name="%(class)s_user",
        on_delete=models.CASCADE,
    )
    worker = models.ForeignKey(
        Worker,
        null=True,
        related_name="%(class)s_worker",
        on_delete=models.DO_NOTHING,
    )

    def __str__(self):
        return (
            str(self.pk)
            + " | "
            + str(self.create_date.date)
            + " | "
            + str(self.user)
            + " | "
            + str(self.animal)
        )


class Reservation(MeetingInfo):
    reservation_date = models.DateTimeField(
        verbose_name="reservation date",
    )

    def __str__(self):
        return str(self.pk) + " | " + super.__str__ + " | " + str(self.reservation_date)


class Adoption(MeetingInfo):
    adoption_date = models.DateTimeField(
        verbose_name="adoption date",
    )
    ID_series_and_number = models.TextField(
        max_length=9,
        verbose_name="ID car series and number",
        unique=True,
    )
    agreement = models.BooleanField(
        verbose_name="agreement",
    )
    # status = models.CharChoices - active, unactive, declined

    def __str__(self):
        return (
            str(self.pk)
            + " | "
            # + super(MeetingInfo, self).__str__()
            + self.user.first_name
            + " "
            + self.user.last_name
            + " | "
            + str(self.animal.name)
            + " | "
            + str(self.adoption_date.date())
        )
