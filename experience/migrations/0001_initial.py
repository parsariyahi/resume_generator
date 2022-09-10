# Generated by Django 4.1.1 on 2022-09-10 14:04

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ("prof", "__first__"),
    ]

    operations = [
        migrations.CreateModel(
            name="Experience",
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
                ("job_position", models.CharField(max_length=150)),
                ("company_name", models.CharField(max_length=150)),
                ("start_date", models.DateField()),
                ("end_date", models.DateField()),
                ("description", models.TextField(null=True)),
                ("type", models.IntegerField(choices=[(1, "Education"), (2, "Work")])),
                (
                    "user_profile",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="experiences",
                        to="prof.prof",
                    ),
                ),
            ],
        ),
    ]
