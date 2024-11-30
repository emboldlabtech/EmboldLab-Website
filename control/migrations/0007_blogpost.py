# Generated by Django 4.2.13 on 2024-06-30 03:23

import ckeditor.fields
import cloudinary.models
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('control', '0006_bootcamp_course_content_desc_1_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='Blogpost',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=555)),
                ('Cover_image', cloudinary.models.CloudinaryField(max_length=255, verbose_name='image')),
                ('subtitle', models.CharField(max_length=555)),
                ('slug', models.SlugField(unique=True)),
                ('post_detail1', ckeditor.fields.RichTextField(blank=True, null=True)),
                ('desc_image1', cloudinary.models.CloudinaryField(max_length=255, verbose_name='image')),
                ('post_detail2', ckeditor.fields.RichTextField(blank=True, null=True)),
                ('desc_image2', cloudinary.models.CloudinaryField(max_length=255, verbose_name='image')),
                ('num_views', models.IntegerField(default=0)),
                ('last_visit', models.DateTimeField(blank=True, null=True)),
                ('thumbnail', cloudinary.models.CloudinaryField(max_length=255, verbose_name='image')),
                ('date_added', models.DateTimeField(auto_now_add=True)),
            ],
            options={
                'ordering': ('-date_added',),
            },
        ),
    ]