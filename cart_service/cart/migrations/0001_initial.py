# Generated by Django 4.1.7 on 2023-03-29 17:08

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="Cart",
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
                ("uname", models.CharField(max_length=200)),
                ("product_id", models.IntegerField()),
                ("quantity", models.IntegerField()),
            ],
        ),
    ]
