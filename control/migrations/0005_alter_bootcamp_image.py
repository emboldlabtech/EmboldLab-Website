# Generated by Django 4.2.13 on 2024-06-28 17:15

import cloudinary.models
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('control', '0004_registration_phone_alter_registration_first_name_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='bootcamp',
            name='image',
            field=cloudinary.models.CloudinaryField(blank=True, max_length=255, null=True, verbose_name='image'),
        ),
    ]