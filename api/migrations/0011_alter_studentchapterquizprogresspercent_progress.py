# Generated by Django 4.2.13 on 2024-06-19 16:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0010_alter_studentchapterquizprogresspercent_progress'),
    ]

    operations = [
        migrations.AlterField(
            model_name='studentchapterquizprogresspercent',
            name='progress',
            field=models.IntegerField(),
        ),
    ]
