# Generated by Django 4.1.7 on 2023-03-29 12:55

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ("book_model", "0001_initial"),
    ]

    operations = [
        migrations.RemoveField(
            model_name="book",
            name="book_id",
        ),
    ]