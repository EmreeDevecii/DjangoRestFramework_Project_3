# Generated by Django 5.1.1 on 2024-09-23 13:09

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("profiller", "0001_initial"),
    ]

    operations = [
        migrations.AlterField(
            model_name="profil",
            name="foto",
            field=models.ImageField(
                blank=True, null=True, upload_to="profil_fotolari/%Y/%m/"
            ),
        ),
    ]
