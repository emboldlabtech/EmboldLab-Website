# Generated by Django 4.2.13 on 2024-12-04 14:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('control', '0043_alter_contact_message_alter_contact_time_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='cohort3registration',
            name='location',
            field=models.CharField(max_length=250),
        ),
    ]