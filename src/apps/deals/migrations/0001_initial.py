# Generated by Django 4.1.7 on 2023-02-15 22:20

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="Deal",
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
                    "customer",
                    models.CharField(max_length=120, verbose_name="Login of Customer"),
                ),
                ("item", models.CharField(max_length=120, verbose_name="Name of Good")),
                (
                    "total",
                    models.DecimalField(
                        decimal_places=2,
                        max_digits=10,
                        verbose_name="Total Price of Good",
                    ),
                ),
                (
                    "quantity",
                    models.PositiveSmallIntegerField(verbose_name="Quantity of Goods"),
                ),
                (
                    "date",
                    models.DateTimeField(verbose_name="Date of Deal registration"),
                ),
            ],
        ),
    ]