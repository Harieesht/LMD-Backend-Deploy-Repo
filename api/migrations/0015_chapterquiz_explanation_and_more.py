# Generated by Django 4.2.13 on 2024-06-29 03:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0014_studentchapterquizanswer_selected_answer_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='chapterquiz',
            name='Explanation',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='studentchapterquizanswer',
            name='selected_answer',
            field=models.CharField(blank=True, max_length=1, null=True),
        ),
    ]
