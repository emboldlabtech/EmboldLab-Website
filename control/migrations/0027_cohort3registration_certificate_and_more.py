# Generated by Django 4.2.13 on 2024-11-12 16:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('control', '0026_alter_cohort3registration_profile_picture'),
    ]

    operations = [
        migrations.AddField(
            model_name='cohort3registration',
            name='certificate',
            field=models.FileField(blank=True, null=True, upload_to='certificates/'),
        ),
        migrations.AddField(
            model_name='cohort3registration',
            name='week_1',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='cohort3registration',
            name='week_2',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='cohort3registration',
            name='week_3',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='cohort3registration',
            name='week_4',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='cohort3registration',
            name='week_5',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='cohort3registration',
            name='week_6',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='cohort3registration',
            name='week_7',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='cohort3registration',
            name='week_8',
            field=models.BooleanField(default=False),
        ),
    ]