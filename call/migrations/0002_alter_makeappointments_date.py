# Generated by Django 3.2.9 on 2021-12-08 12:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('call', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='makeappointments',
            name='date',
            field=models.DateField(),
        ),
    ]
