# Generated by Django 4.1.7 on 2023-03-16 03:12

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="payment_status",
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
                ("username", models.CharField(max_length=10)),
                ("product_id", models.CharField(max_length=10)),
                ("price", models.CharField(max_length=10)),
                ("quantity", models.CharField(max_length=5)),
                ("mode_of_payment", models.CharField(max_length=20)),
                ("mobile", models.CharField(max_length=12)),
                ("status", models.CharField(max_length=15)),
            ],
        ),
    ]
