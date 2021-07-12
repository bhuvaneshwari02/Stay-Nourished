# Generated by Django 3.2.2 on 2021-06-18 18:00

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('Dummy_app', '0003_auto_20210528_2224'),
    ]

    operations = [
        migrations.CreateModel(
            name='personal',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('Gender', models.CharField(choices=[('male', 'Male'), ('female', 'Female')], max_length=12)),
                ('Worktype', models.CharField(choices=[('sedentary', 'Sedentary'), ('moderate', 'Moderate'), ('heavywork', 'Heavywork')], max_length=12)),
                ('Foodhabit', models.CharField(choices=[('veg', 'Veg'), ('non-veg', 'Non-Veg')], max_length=12)),
            ],
        ),
    ]
