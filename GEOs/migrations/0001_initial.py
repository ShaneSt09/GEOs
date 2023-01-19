# Generated by Django 4.1 on 2023-01-19 14:41

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="CommunityType",
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
                ("name", models.CharField(max_length=100, unique=True)),
            ],
            options={
                "verbose_name": "Community Type",
            },
        ),
        migrations.CreateModel(
            name="Parish",
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
                ("code", models.CharField(max_length=10)),
                ("name", models.CharField(max_length=100, unique=True)),
            ],
            options={
                "verbose_name": "Parish",
                "verbose_name_plural": "Parishes",
            },
        ),
        migrations.CreateModel(
            name="Community",
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
                ("name", models.CharField(max_length=100)),
                (
                    "lng",
                    models.DecimalField(
                        blank=True,
                        decimal_places=8,
                        max_digits=15,
                        null=True,
                        verbose_name="Longitude",
                    ),
                ),
                (
                    "lat",
                    models.DecimalField(
                        blank=True,
                        decimal_places=8,
                        max_digits=15,
                        null=True,
                        verbose_name="Latitude",
                    ),
                ),
                (
                    "parish",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.PROTECT, to="geos.parish"
                    ),
                ),
                (
                    "type",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.PROTECT,
                        to="geos.communitytype",
                    ),
                ),
            ],
            options={
                "verbose_name": "Community",
                "verbose_name_plural": "Communities",
            },
        ),
    ]