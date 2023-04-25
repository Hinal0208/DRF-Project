# Generated by Django 4.2 on 2023-04-25 06:01

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("app", "0009_mentor_feedback_and_more"),
    ]

    operations = [
        migrations.CreateModel(
            name="Feees",
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
                ("amount", models.CharField(max_length=100)),
                ("payment_id", models.CharField(max_length=100)),
                ("paid", models.BooleanField(default=False)),
            ],
        ),
    ]
