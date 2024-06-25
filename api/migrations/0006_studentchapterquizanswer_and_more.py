# Generated by Django 4.2.13 on 2024-06-16 11:38

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0007_alter_user_user_image'),
        ('api', '0005_alter_chapteritem_chapter'),
    ]

    operations = [
        migrations.CreateModel(
            name='StudentChapterQuizAnswer',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('is_correct', models.BooleanField(default=False)),
                ('student', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='users.student')),
                ('subjectquiz', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='api.chapterquiz')),
            ],
        ),
        migrations.CreateModel(
            name='StudentChapterQuizProgressPercent',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('progress', models.SmallIntegerField()),
                ('chapter', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='api.chapter')),
                ('chapterquiz', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='api.chapterquiz')),
                ('student', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='users.student')),
            ],
        ),
        migrations.CreateModel(
            name='SubjectNotes',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100)),
                ('description', models.TextField()),
            ],
        ),
        migrations.DeleteModel(
            name='ChapterQuizAnswer',
        ),
    ]
