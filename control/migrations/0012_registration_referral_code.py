# Generated by Django 4.2.13 on 2024-07-07 05:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('control', '0011_student_project'),
    ]

    operations = [
        migrations.AddField(
            model_name='registration',
            name='referral_code',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
    ]
