# Generated by Django 3.2.2 on 2021-06-21 15:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Dummy_app', '0007_diet'),
    ]

    operations = [
        migrations.AlterField(
            model_name='personal',
            name='BloodPressure',
            field=models.CharField(max_length=100, null='True'),
        ),
        migrations.AlterField(
            model_name='personal',
            name='Foodhabit',
            field=models.CharField(max_length=30, null='True'),
        ),
        migrations.AlterField(
            model_name='personal',
            name='Glucose',
            field=models.CharField(max_length=100, null='True'),
        ),
        migrations.AlterField(
            model_name='personal',
            name='Height',
            field=models.IntegerField(default=0),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='personal',
            name='Weight',
            field=models.IntegerField(),
        ),
        migrations.AlterField(
            model_name='personal',
            name='Worktype',
            field=models.CharField(max_length=20, null='True'),
        ),
    ]
