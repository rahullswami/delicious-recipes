# Generated by Django 5.0.4 on 2024-06-04 07:56

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('vege', '0002_receipe_user'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='receipe',
            name='user',
        ),
    ]
