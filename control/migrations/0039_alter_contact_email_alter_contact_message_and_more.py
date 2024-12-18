# Generated by Django 4.2.13 on 2024-12-01 22:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('control', '0038_rename_ship_dropshipping'),
    ]

    operations = [
        migrations.AlterField(
            model_name='contact',
            name='email',
            field=models.CharField(max_length=150),
        ),
        migrations.AlterField(
            model_name='contact',
            name='message',
            field=models.CharField(max_length=150),
        ),
        migrations.AlterField(
            model_name='contact',
            name='name',
            field=models.CharField(max_length=150),
        ),
        migrations.AlterField(
            model_name='contact',
            name='reason',
            field=models.CharField(blank=True, max_length=150, null=True),
        ),
        migrations.AlterField(
            model_name='dropshipping',
            name='email',
            field=models.CharField(max_length=150),
        ),
    ]
