# Generated by Django 3.2.5 on 2023-09-13 19:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Alumnos', '0010_auto_20230913_1900'),
    ]

    operations = [
        migrations.AddField(
            model_name='customuser',
            name='cve_escuela',
            field=models.CharField(max_length=8, null=True),
        ),
        migrations.AddField(
            model_name='customuser',
            name='is_coordinator',
            field=models.BooleanField(default=False),
        ),
    ]
