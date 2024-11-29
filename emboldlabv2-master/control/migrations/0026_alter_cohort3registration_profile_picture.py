# Generated by Django 4.2.13 on 2024-11-12 14:41

import cloudinary.models
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('control', '0025_alter_cohort3registration_profile_picture'),
    ]

    operations = [
        migrations.AlterField(
            model_name='cohort3registration',
            name='profile_picture',
            field=cloudinary.models.CloudinaryField(blank=True, max_length=255, null=True, verbose_name='image'),
        ),
    ]
