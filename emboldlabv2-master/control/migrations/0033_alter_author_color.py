# Generated by Django 4.2.13 on 2024-11-13 19:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('control', '0032_alter_author_color'),
    ]

    operations = [
        migrations.AlterField(
            model_name='author',
            name='color',
            field=models.CharField(choices=[('#e3811d', 'Orange'), ('#890fcc', 'Purple'), ('#8378f8', 'Lavender'), ('#000000', 'Black')], help_text='Select a color', max_length=7),
        ),
    ]
