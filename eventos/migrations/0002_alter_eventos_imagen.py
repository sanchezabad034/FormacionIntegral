# Generated by Django 3.2.5 on 2021-07-08 17:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('eventos', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='eventos',
            name='imagen',
            field=models.ImageField(max_length=254, upload_to=None),
        ),
    ]