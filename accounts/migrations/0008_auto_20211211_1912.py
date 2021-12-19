# Generated by Django 3.2.9 on 2021-12-11 19:12

import accounts.models
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0007_auto_20211113_2011'),
    ]

    operations = [
        migrations.AlterField(
            model_name='main_app_details',
            name='logo',
            field=models.ImageField(default='[Original size] Smart Tech(1).png', upload_to=accounts.models.path_and_rename),
        ),
        migrations.AlterField(
            model_name='site_contacts',
            name='site_name',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='accounts.main_app_details'),
        ),
    ]
