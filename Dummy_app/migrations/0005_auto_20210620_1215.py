# Generated by Django 3.2.2 on 2021-06-20 06:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Dummy_app', '0004_personal'),
    ]

    operations = [
        migrations.AlterField(
            model_name='personal',
            name='Foodhabit',
            field=models.CharField(max_length=12),
        ),
        migrations.AlterField(
            model_name='personal',
            name='Gender',
            field=models.CharField(max_length=12),
        ),
        migrations.AlterField(
            model_name='personal',
            name='Worktype',
            field=models.CharField(max_length=12),
        ),
    ]
