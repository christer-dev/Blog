# Generated by Django 4.0.5 on 2022-06-15 16:30

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blogs', '0002_comment'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='post',
            name='authorName',
        ),
    ]