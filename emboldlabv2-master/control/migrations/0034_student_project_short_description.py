# Generated by Django 4.2.13 on 2024-11-19 04:09

import ckeditor.fields
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('control', '0033_alter_author_color'),
    ]

    operations = [
        migrations.AddField(
            model_name='student_project',
            name='short_description',
            field=ckeditor.fields.RichTextField(blank=True, null=True),
        ),
    ]
