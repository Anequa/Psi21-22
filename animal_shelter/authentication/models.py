from django.contrib.auth.models import AbstractUser
from django.core.validators import RegexValidator
from django.db import models


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

    @property
    def full_name(self):
        return f"{self.first_name} {self.last_name}"

    def __str__(self):
        return f"{self.pk} {self.full_name}"


class Worker(User):
    employment_date = models.DateField(
        auto_now_add=True,
        verbose_name="employment date",
    )

    bank_account_number = models.TextField(
        max_length=26,
        verbose_name="bank account number",
    )
    wage = models.IntegerField(
        verbose_name="wage",
        default=0,
    )

    class Meta:
        verbose_name = "worker"
        verbose_name_plural = "workers"

    @property
    def full_name(self):
        return super().full_name

    def __str__(self):
        return f"{super().full_name}"
