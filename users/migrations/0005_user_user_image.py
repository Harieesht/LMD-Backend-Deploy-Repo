# Generated by Django 4.2.13 on 2024-06-10 10:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0004_user_name_alter_user_username'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='user_image',
            field=models.FileField(default=1, upload_to='path-to-upload'),
            preserve_default=False,
        ),
    ]
