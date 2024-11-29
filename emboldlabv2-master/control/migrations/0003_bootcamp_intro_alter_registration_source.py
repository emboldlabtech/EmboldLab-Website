# Generated by Django 4.2.13 on 2024-06-27 14:31

import ckeditor.fields
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('control', '0002_registration'),
    ]

    operations = [
        migrations.AddField(
            model_name='bootcamp',
            name='intro',
            field=ckeditor.fields.RichTextField(blank=True),
        ),
        migrations.AlterField(
            model_name='registration',
            name='source',
            field=models.CharField(blank=True, choices=[('SM', 'Social Media'), ('FL', 'Futlink Hardwares'), ('SI', 'Splash Initiative'), ('R', 'Referral'), ('N', 'NAUS'), ('O', 'Others')], max_length=2, null=True),
        ),
    ]
