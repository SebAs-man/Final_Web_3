# Generated by Django 5.1.2 on 2024-12-02 03:49

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='carta',
            name='image',
        ),
    ]
