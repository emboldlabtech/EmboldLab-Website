# Generated by Django 4.2.13 on 2024-10-24 18:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('control', '0012_registration_referral_code'),
    ]

    operations = [
        migrations.AddField(
            model_name='bootcamp',
            name='is_masterlass',
            field=models.BooleanField(default=False),
        ),
    ]
