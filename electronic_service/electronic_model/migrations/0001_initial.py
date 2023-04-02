# Generated by Django 4.1.7 on 2023-03-29 14:51

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="Electronic_detail",
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
                ("name", models.CharField(max_length=200)),
                ("sku", models.CharField(max_length=200)),
                ("description", models.CharField(max_length=200)),
                ("availability", models.CharField(max_length=200)),
                ("price", models.CharField(max_length=200)),
            ],
        ),
    ]