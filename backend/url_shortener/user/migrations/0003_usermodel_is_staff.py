# Generated by Django 5.0.6 on 2024-06-16 08:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0002_usermodel_is_active'),
    ]

    operations = [
        migrations.AddField(
            model_name='usermodel',
            name='is_staff',
            field=models.BooleanField(default=True),
        ),
    ]
