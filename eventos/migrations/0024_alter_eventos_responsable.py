# Generated by Django 3.2.5 on 2023-08-30 18:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('eventos', '0023_eventos_responsable'),
    ]

    operations = [
        migrations.AlterField(
            model_name='eventos',
            name='responsable',
            field=models.CharField(max_length=200, verbose_name='responsable'),
        ),
    ]
