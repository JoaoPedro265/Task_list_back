# Generated by Django 5.0.4 on 2024-11-24 15:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('App', '0002_rename_senha_user_login_password'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user_login',
            name='email',
            field=models.EmailField(default='', max_length=500, unique=True),
        ),
    ]
