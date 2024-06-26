# Generated by Django 4.2.13 on 2024-07-01 07:00

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0007_alter_user_user_image'),
        ('api', '0016_delete_subjectprogress'),
    ]

    operations = [
        migrations.CreateModel(
            name='SubjectProgress',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('progress', models.PositiveSmallIntegerField()),
                ('student', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='progress', to='users.student')),
                ('subject', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='api.subject')),
            ],
        ),
    ]
