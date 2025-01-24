# Generated by Django 5.0.4 on 2024-11-24 14:41

import django.db.models.deletion
import django.utils.timezone
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='User_Login',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(default='', max_length=200)),
                ('last_name', models.CharField(default='', max_length=200)),
                ('email', models.EmailField(default='', max_length=500)),
                ('senha', models.CharField(max_length=200)),
            ],
        ),
        migrations.CreateModel(
            name='Task_List',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('descrition', models.CharField(default='', max_length=500)),
                ('text', models.CharField(default='', max_length=500)),
                ('data', models.DateTimeField(default=django.utils.timezone.now)),
                ('completed', models.BooleanField(default=False)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='App.user_login')),
            ],
        ),
    ]
