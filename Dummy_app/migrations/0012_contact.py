# Generated by Django 3.2.2 on 2021-07-10 10:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Dummy_app', '0011_food'),
    ]

    operations = [
        migrations.CreateModel(
            name='Contact',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Name', models.CharField(max_length=50)),
                ('Email', models.CharField(max_length=50)),
                ('Phone', models.CharField(max_length=50)),
                ('Query', models.TextField()),
            ],
        ),
    ]