# Generated by Django 4.2.13 on 2024-10-24 22:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('control', '0015_bootcampregistration'),
    ]

    operations = [
        migrations.AlterField(
            model_name='registration',
            name='source',
            field=models.CharField(blank=True, choices=[('Twitter', 'Twitter'), ('Facebook', 'Facebook'), ('LinkedIn', 'LinkedIn'), ('Referral', 'Referral'), ('NAUS', 'NAUS')], max_length=205, null=True),
        ),
    ]