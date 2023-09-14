# Generated by Django 3.2.5 on 2021-10-12 01:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('eventos', '0008_eventoscalendario'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='eventoscalendario',
            name='timeEnd',
        ),
        migrations.RemoveField(
            model_name='eventoscalendario',
            name='timeStart',
        ),
        migrations.AlterField(
            model_name='eventoscalendario',
            name='end',
            field=models.CharField(max_length=50, verbose_name='end'),
        ),
        migrations.AlterField(
            model_name='eventoscalendario',
            name='start',
            field=models.CharField(max_length=50, verbose_name='start'),
        ),
    ]