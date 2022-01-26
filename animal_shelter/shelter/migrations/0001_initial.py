# Generated by Django 3.2.5 on 2022-01-26 16:00

import django.core.validators
import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ("authentication", "0001_initial"),
    ]

    operations = [
        migrations.CreateModel(
            name="Animal",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                (
                    "species",
                    models.CharField(
                        choices=[("Dog", "Dog"), ("Cat", "Cat")],
                        max_length=3,
                        verbose_name="species",
                    ),
                ),
                (
                    "name",
                    models.TextField(
                        max_length=45,
                        validators=[
                            django.core.validators.RegexValidator(
                                message="Name must start with upper letter and can not have numbers",
                                regex="^[A-Z][a-z]+$",
                            )
                        ],
                        verbose_name="name",
                    ),
                ),
                ("age", models.IntegerField(verbose_name="age")),
                (
                    "gender",
                    models.CharField(
                        choices=[("female", "Female"), ("male", "Male")],
                        max_length=6,
                        verbose_name="gender",
                    ),
                ),
                (
                    "size",
                    models.CharField(
                        choices=[
                            ("Small", "Small"),
                            ("Medium", "Medium"),
                            ("Big", "Big"),
                        ],
                        max_length=10,
                        verbose_name="size",
                    ),
                ),
                (
                    "description",
                    models.TextField(
                        blank=True,
                        default="Opis jeszcze nie zamieszczony",
                        null=True,
                        verbose_name="description",
                    ),
                ),
                (
                    "date_of_arrival",
                    models.DateField(auto_now_add=True, verbose_name="date of arrival"),
                ),
                (
                    "status",
                    models.CharField(
                        choices=[
                            ("addopted", "Addopted"),
                            ("unavailable", "Unavailable"),
                            ("available", "Available"),
                        ],
                        default="available",
                        max_length=15,
                        verbose_name="status",
                    ),
                ),
            ],
        ),
        migrations.CreateModel(
            name="Cage",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("cage_number", models.IntegerField()),
                (
                    "section",
                    models.CharField(
                        choices=[("A", "A"), ("B", "B"), ("C", "C"), ("D", "D")],
                        max_length=3,
                        verbose_name="section",
                    ),
                ),
                ("space", models.IntegerField(default=1, verbose_name="space")),
                (
                    "species",
                    models.CharField(
                        choices=[("Dog", "Dog"), ("Cat", "Cat")],
                        max_length=3,
                        verbose_name="species",
                    ),
                ),
            ],
        ),
        migrations.CreateModel(
            name="Reservation",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                (
                    "create_date",
                    models.DateField(auto_now_add=True, verbose_name="create date"),
                ),
                ("reservation_date", models.DateField(verbose_name="reservation date")),
                (
                    "animal",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to="shelter.animal",
                        verbose_name="animal",
                    ),
                ),
                (
                    "owner",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="reservation",
                        to="authentication.user",
                    ),
                ),
                (
                    "user",
                    models.ForeignKey(
                        null=True,
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="reservation_user",
                        to="authentication.user",
                    ),
                ),
            ],
            options={
                "verbose_name": "reservation",
                "verbose_name_plural": "reservations",
            },
        ),
        migrations.CreateModel(
            name="Photo",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                (
                    "alter",
                    models.TextField(
                        max_length=30, verbose_name="alternativer description"
                    ),
                ),
                ("photo", models.ImageField(upload_to="animal", verbose_name="photo")),
                (
                    "animal",
                    models.ForeignKey(
                        null=True,
                        on_delete=django.db.models.deletion.SET_NULL,
                        to="shelter.animal",
                        verbose_name="animal",
                    ),
                ),
            ],
        ),
        migrations.AddField(
            model_name="animal",
            name="cage",
            field=models.ForeignKey(
                null=True,
                on_delete=django.db.models.deletion.PROTECT,
                related_name="animals",
                to="shelter.cage",
                verbose_name="cage",
            ),
        ),
        migrations.CreateModel(
            name="Adoption",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                (
                    "create_date",
                    models.DateField(auto_now_add=True, verbose_name="create date"),
                ),
                ("adoption_date", models.DateField(verbose_name="adoption date")),
                (
                    "ID_series_and_number",
                    models.TextField(
                        max_length=9,
                        unique=True,
                        verbose_name="ID card series and number",
                    ),
                ),
                ("agreement", models.BooleanField(verbose_name="agreement")),
                (
                    "status",
                    models.CharField(
                        choices=[
                            ("accepted", "Accepted"),
                            ("declined", "Declined"),
                            ("ready for consideration", "Ready For Consideration"),
                        ],
                        default="ready for consideration",
                        max_length=30,
                        verbose_name="adoption status",
                    ),
                ),
                (
                    "animal",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to="shelter.animal",
                        verbose_name="animal",
                    ),
                ),
                (
                    "owner",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="adoptions",
                        to="authentication.user",
                    ),
                ),
                (
                    "user",
                    models.ForeignKey(
                        null=True,
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="adoption_user",
                        to="authentication.user",
                    ),
                ),
            ],
            options={
                "verbose_name": "adoption",
                "verbose_name_plural": "adoptions",
            },
        ),
    ]
