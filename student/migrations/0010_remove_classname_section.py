# Generated by Django 4.1.6 on 2023-05-15 03:03

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('student', '0009_reviews'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='classname',
            name='section',
        ),
    ]
