# Generated by Django 5.0.4 on 2024-11-24 15:09

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('App', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='user_login',
            old_name='senha',
            new_name='password',
        ),
    ]
