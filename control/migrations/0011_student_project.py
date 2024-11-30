# Generated by Django 4.2.13 on 2024-07-05 06:49

import cloudinary.models
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('control', '0010_alter_blogpost_slug'),
    ]

    operations = [
        migrations.CreateModel(
            name='Student_project',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=3700)),
                ('Cover_image', cloudinary.models.CloudinaryField(max_length=255, verbose_name='image')),
                ('subtitle', models.CharField(max_length=20000)),
                ('link', models.URLField()),
            ],
        ),
    ]