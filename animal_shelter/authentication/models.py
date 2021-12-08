from django.contrib.auth.models import AbstractUser
from django.core.validators import RegexValidator
from django.db import models

# from django.utils.translation import gettext_lazy as _

# Create your models here.


class User(AbstractUser):
    email = models.EmailField(
        max_length=255,
        unique=True,
        verbose_name="email",
        error_messages={
            "unique": ("Osoba o takim emailu już istnieje."),
        },
    )
    phone_number_regex = RegexValidator(
        regex=r"^([1-9][0-9])?[1-9][0-9]{8}",
        message=(
            "Phone number must be entered in the format: '19012345678'. Up to 11 digits allowed."
        ),
    )
    phone = models.TextField(
        validators=[phone_number_regex],
        max_length=11,
        verbose_name="phone",
        unique=True,
    )
    city = models.TextField(
        verbose_name="city",
        max_length=30,
    )
    zip_code_regax = RegexValidator(
        regex=r"^[0-9]{2}-[0-9]{3}",
        message="Zip code must be entered in format: '12-345' Up to 5 digits allowed.",
    )
    zip_code = models.TextField(
        validators=[zip_code_regax],
        verbose_name="zip code",
        max_length=6,
    )
    address_line1 = models.TextField(
        verbose_name="address",
        max_length=45,
    )
    address_line2 = models.TextField(
        verbose_name="correspondence address",
        null=True,
        blank=True,
        max_length=45,
    )

    class Meta:
        verbose_name = "user"
        verbose_name_plural = "users"
        # ordering = ("first_name",)

    def __str__(self):
        return str(self.pk) + " | " + self.first_name + " " + self.last_name


class Worker(User):
    employment_date = models.DateField(
        auto_now_add=True,
        verbose_name="employment date",
    )

    class Position(models.TextChoices):
        CLEANER = "cleaner"
        ADMINISTRATOR = "administrator"
        VOLUNTEER = "volunteer"

    position = models.CharField(
        max_length=20,
        verbose_name="position",
        choices=Position.choices,
    )
    contract_expiration_date = models.DateTimeField(
        verbose_name="contract expiration date",
        blank=True,
        null=True,
    )
    bank_account_number = models.TextField(
        max_length=26,
        verbose_name="bank account number",
    )
    wage = models.IntegerField(
        verbose_name="wage",
        default=0,
    )

    class Status(models.TextChoices):
        TRIAL = "trial"
        EXPIRED = "expired"
        EMPLOYED = "employed"

    status = models.CharField(
        max_length=15,
        verbose_name="status",
        choices=Status.choices,
    )

    class Meta:
        verbose_name = "worker"
        verbose_name_plural = "workers"

    def __str__(self):
        return (
            str(self.pk)
            + " | "
            + self.first_name
            + " "
            + self.last_name
            + " | "
            + self.position
            + " | "
            + self.status
        )
