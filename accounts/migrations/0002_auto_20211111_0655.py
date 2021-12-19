# Generated by Django 3.2.9 on 2021-11-11 06:55

import accounts.models
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='main_app_details',
            name='logo',
            field=models.ImageField(default='[Original size] Smart Tech(1).png', upload_to=accounts.models.path_and_rename),
        ),
        migrations.AlterField(
            model_name='main_app_details',
            name='name',
            field=models.CharField(max_length=60, primary_key=True, serialize=False),
        ),
    ]
