# Generated by Django 4.2.13 on 2024-10-24 18:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('control', '0014_rename_is_masterlass_bootcamp_is_masterclass'),
    ]

    operations = [
        migrations.CreateModel(
            name='BootcampRegistration',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('email', models.EmailField(max_length=254)),
                ('phone', models.CharField(max_length=20)),
                ('laptop_access', models.CharField(choices=[('Yes', 'Yes'), ('No', 'No')], max_length=3)),
                ('program', models.CharField(choices=[('Bootcamp', 'Bootcamp'), ('Accelerator', 'Accelerator Program'), ('Masterclass', 'Masterclass')], max_length=20)),
                ('course', models.CharField(max_length=50)),
                ('level', models.CharField(choices=[('Fresher', 'Fresher'), ('Beginner', 'Beginner'), ('Intermediate', 'Intermediate'), ('Advanced', 'Advanced')], max_length=20)),
                ('source', models.CharField(choices=[('Twitter', 'Twitter'), ('Facebook', 'Facebook'), ('LinkedIn', 'LinkedIn'), ('Referral', 'Referral'), ('NAUS', 'NAUS')], max_length=20)),
                ('location', models.TextField()),
                ('proof_of_payment', models.FileField(upload_to='payments/')),
                ('referral_code', models.CharField(blank=True, max_length=50, null=True)),
            ],
        ),
    ]
