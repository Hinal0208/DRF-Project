# Generated by Django 4.2 on 2023-04-24 08:26

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):
    dependencies = [
        ("app", "0007_session_year_session_name_alter_trainee_course_id"),
    ]

    operations = [
        migrations.CreateModel(
            name="Attendance",
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
                ("attendace_data", models.DateField()),
                ("created_at", models.DateTimeField(auto_now_add=True)),
                ("updated_at", models.DateTimeField(auto_now=True)),
                (
                    "course_id",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.DO_NOTHING, to="app.course"
                    ),
                ),
                (
                    "session_year_id",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.DO_NOTHING,
                        to="app.session_year",
                    ),
                ),
            ],
        ),
        migrations.AlterField(
            model_name="trainee",
            name="session_year_id",
            field=models.ForeignKey(
                on_delete=django.db.models.deletion.CASCADE, to="app.session_year"
            ),
        ),
        migrations.CreateModel(
            name="Attendance_Report",
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
                ("created_at", models.DateTimeField(auto_now_add=True)),
                ("updated_at", models.DateTimeField(auto_now=True)),
                (
                    "attendace_id",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE, to="app.attendance"
                    ),
                ),
                (
                    "trainee_id",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.DO_NOTHING, to="app.trainee"
                    ),
                ),
            ],
        ),
    ]
