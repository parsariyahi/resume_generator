# Generated by Django 4.1.1 on 2022-09-19 07:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("prof", "0002_alter_prof_bio_alter_prof_job_position_and_more"),
    ]

    operations = [
        migrations.AddField(
            model_name="prof",
            name="link",
            field=models.CharField(default="afsharsharifi", max_length=250),
            preserve_default=False,
        ),
    ]