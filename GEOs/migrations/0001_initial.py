# Generated by Django 4.1 on 2023-01-16 02:15

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = []

    operations = [
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
                (
                    "Name",
                    models.CharField(
                        blank=True, default=None, max_length=25, null=True
                    ),
                ),
                ("Type", models.CharField(max_length=15, null=True)),
                ("Parish", models.CharField(max_length=25, null=True)),
                ("ParishCode", models.CharField(max_length=25, null=True)),
                ("Longitude", models.CharField(blank=True, max_length=50, null=True)),
                ("Latitude", models.CharField(blank=True, max_length=50, null=True)),
            ],
        ),
    ]
