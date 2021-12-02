# Generated by Django 3.2.5 on 2021-11-22 18:36

import django.contrib.auth.models
import django.contrib.auth.validators
import django.db.models.deletion
import django.utils.timezone
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ("auth", "0012_alter_user_first_name_max_length"),
    ]

    operations = [
        migrations.CreateModel(
            name="User",
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
                ("password", models.CharField(max_length=128, verbose_name="password")),
                (
                    "last_login",
                    models.DateTimeField(
                        blank=True, null=True, verbose_name="last login"
                    ),
                ),
                (
                    "is_superuser",
                    models.BooleanField(
                        default=False,
                        help_text="Designates that this user has all permissions without explicitly assigning them.",
                        verbose_name="superuser status",
                    ),
                ),
                (
                    "username",
                    models.CharField(
                        error_messages={
                            "unique": "A user with that username already exists."
                        },
                        help_text="Required. 150 characters or fewer. Letters, digits and @/./+/-/_ only.",
                        max_length=150,
                        unique=True,
                        validators=[
                            django.contrib.auth.validators.UnicodeUsernameValidator()
                        ],
                        verbose_name="username",
                    ),
                ),
                (
                    "first_name",
                    models.CharField(
                        blank=True, max_length=150, verbose_name="first name"
                    ),
                ),
                (
                    "last_name",
                    models.CharField(
                        blank=True, max_length=150, verbose_name="last name"
                    ),
                ),
                (
                    "is_staff",
                    models.BooleanField(
                        default=False,
                        help_text="Designates whether the user can log into this admin site.",
                        verbose_name="staff status",
                    ),
                ),
                (
                    "is_active",
                    models.BooleanField(
                        default=True,
                        help_text="Designates whether this user should be treated as active. Unselect this instead of deleting accounts.",
                        verbose_name="active",
                    ),
                ),
                (
                    "date_joined",
                    models.DateTimeField(
                        default=django.utils.timezone.now, verbose_name="date joined"
                    ),
                ),
                (
                    "email",
                    models.EmailField(
                        error_messages={"unique": "Osoba o takim emailu już istnieje."},
                        max_length=255,
                        unique=True,
                        verbose_name="email",
                    ),
                ),
                (
                    "phone",
                    models.TextField(max_length=11, unique=True, verbose_name="phone"),
                ),
                ("city", models.TextField(max_length=30, verbose_name="city")),
                ("zip_code", models.TextField(max_length=6, verbose_name="zip code")),
                (
                    "address_line1",
                    models.TextField(max_length=45, verbose_name="address"),
                ),
                (
                    "address_line2",
                    models.TextField(
                        blank=True,
                        max_length=45,
                        null=True,
                        verbose_name="correspondence address",
                    ),
                ),
                (
                    "groups",
                    models.ManyToManyField(
                        blank=True,
                        help_text="The groups this user belongs to. A user will get all permissions granted to each of their groups.",
                        related_name="user_set",
                        related_query_name="user",
                        to="auth.Group",
                        verbose_name="groups",
                    ),
                ),
                (
                    "user_permissions",
                    models.ManyToManyField(
                        blank=True,
                        help_text="Specific permissions for this user.",
                        related_name="user_set",
                        related_query_name="user",
                        to="auth.Permission",
                        verbose_name="user permissions",
                    ),
                ),
            ],
            options={
                "verbose_name": "user",
                "verbose_name_plural": "users",
                "abstract": False,
            },
            managers=[
                ("objects", django.contrib.auth.models.UserManager()),
            ],
        ),
        migrations.CreateModel(
            name="Worker",
            fields=[
                (
                    "user_ptr",
                    models.OneToOneField(
                        auto_created=True,
                        on_delete=django.db.models.deletion.CASCADE,
                        parent_link=True,
                        primary_key=True,
                        serialize=False,
                        to="authentication.user",
                    ),
                ),
                (
                    "employment_date",
                    models.DateField(auto_now_add=True, verbose_name="employment date"),
                ),
                (
                    "position",
                    models.CharField(
                        choices=[
                            ("cleaner", "Cleaner"),
                            ("administrator", "Administrator"),
                            ("volunteer", "Volunteer"),
                        ],
                        max_length=20,
                        verbose_name="position",
                    ),
                ),
                (
                    "contract_expiration_date",
                    models.DateTimeField(
                        blank=True, null=True, verbose_name="contract expiration date"
                    ),
                ),
                (
                    "bank_account_number",
                    models.TextField(max_length=26, verbose_name="bank account number"),
                ),
                ("wage", models.IntegerField(default=0, verbose_name="wage")),
                (
                    "status",
                    models.CharField(
                        choices=[
                            ("trial", "Trial"),
                            ("expired", "Expired"),
                            ("employed", "Employed"),
                        ],
                        max_length=15,
                        verbose_name="status",
                    ),
                ),
            ],
            options={
                "verbose_name": "user",
                "verbose_name_plural": "users",
                "abstract": False,
            },
            bases=("authentication.user",),
            managers=[
                ("objects", django.contrib.auth.models.UserManager()),
            ],
        ),
    ]
