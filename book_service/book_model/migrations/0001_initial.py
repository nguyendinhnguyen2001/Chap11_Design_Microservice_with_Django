# Generated by Django 4.1.7 on 2023-03-29 12:46

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="Book",
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
                ("book_id", models.CharField(max_length=200)),
                ("title", models.CharField(max_length=200)),
                ("auther", models.CharField(max_length=200)),
                ("description", models.CharField(max_length=200)),
                ("availability", models.CharField(max_length=200)),
                ("publisher", models.CharField(max_length=200)),
                ("publish_Date", models.CharField(max_length=200)),
                ("price", models.CharField(max_length=200)),
            ],
        ),
    ]