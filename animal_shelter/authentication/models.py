from django.contrib.auth.models import AbstractUser
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
    phone = models.TextField(
        max_length=11,
        verbose_name="phone",
        unique=True,
    )
    city = models.TextField(
        verbose_name="city",
        max_length=30,
    )
    zip_code = models.TextField(
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
