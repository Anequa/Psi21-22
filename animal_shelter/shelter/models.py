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
    cage_number = models.IntegerField()
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

    @property
    def cage_identyficator(self):
        return f"{self.section}-{self.cage_number}"

    def __str__(self):
        return self.cage_identyficator


class Animal(models.Model):
    species = models.CharField(
        max_length=3,
        verbose_name="species",
        choices=Species.choices,
    )
    name = models.TextField(
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
    date_of_arrival = models.DateField(
        auto_now_add=True,
        verbose_name="date of arrival",
    )
    estimate_year_of_birth = models.IntegerField(
        verbose_name="estimate year of birth",
    )

    class Status(models.TextChoices):
        ADDOPTED = "addopted"
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
        related_name="animals",
        null=True,
        on_delete=models.SET_NULL,
    )

    @property
    def reservations(self):
        animal = Animal.objects.get(name=self.name)
        return Reservation.objects.filter(animal=animal)

    @property
    def adoptions(self):
        animal = Animal.objects.get(name=self.name)
        return Adoption.objects.filter(animal=animal)

    @property
    def photos(self):
        animal = Animal.objects.get(name=self.name)
        return Photo.objects.filter(animal=animal)

    def __str__(self):
        return self.name


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
        return self.alter


class MeetingInfo(models.Model):
    create_date = models.DateField(
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
        on_delete=models.SET_NULL,
    )

    def __str__(self):
        return f"{self.create_date} | {self.user} | {self.animal}"


class Reservation(MeetingInfo):
    reservation_date = models.DateField(
        verbose_name="reservation date",
    )

    @property
    def reservation_info(self):
        return f"{self.animal.name}-{self.reservation_date}"

    def __str__(self):
        return f"{super().animal} | {self.reservation_date}"


class Adoption(MeetingInfo):
    adoption_date = models.DateField(
        verbose_name="adoption date",
    )
    ID_series_and_number_regex = RegexValidator(
        regex=r"^[A-Z]{3} [0-9]{6}",
        message=(
            "Phone number must be entered in the format: '19012345678'. Up to 11 digits allowed."
        ),
    )
    ID_series_and_number = models.TextField(
        max_length=9,
        verbose_name="ID card series and number",
        unique=True,
    )
    agreement = models.BooleanField(
        verbose_name="agreement",
    )

    class Status(models.TextChoices):
        ACCEPTED = "accepted"
        DECLINED = "declined"
        READY_FOR_CONSIDERATION = "ready for consideration"

    status = models.CharField(
        max_length=30,
        verbose_name="adoption status",
        choices=Status.choices,
        default=Status.READY_FOR_CONSIDERATION,
    )

    @property
    def adoption_info(self):
        return f"{self.animal.name}-{self.adoption_date}"

    def __str__(self):
        return f"{super().animal} | {self.adoption_date}"
