# Generated by Django 3.2.2 on 2021-06-20 16:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Dummy_app', '0006_auto_20210620_1507'),
    ]

    operations = [
        migrations.CreateModel(
            name='Diet',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Nameofthediet', models.CharField(max_length=50)),
                ('DietImage', models.ImageField(upload_to='pics')),
            ],
        ),
    ]