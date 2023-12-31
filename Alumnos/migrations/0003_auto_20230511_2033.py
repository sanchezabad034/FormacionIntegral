# Generated by Django 3.2.5 on 2023-05-12 02:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Alumnos', '0002_alter_alumnos_carrera'),
    ]

    operations = [
        migrations.AlterField(
            model_name='alumnos',
            name='apellidos',
            field=models.CharField(max_length=80, verbose_name='apellidos'),
        ),
        migrations.AlterField(
            model_name='alumnos',
            name='carrera',
            field=models.CharField(max_length=50, verbose_name='carrera'),
        ),
        migrations.AlterField(
            model_name='alumnos',
            name='correo',
            field=models.EmailField(max_length=50, verbose_name='correo'),
        ),
        migrations.AlterField(
            model_name='alumnos',
            name='matricula',
            field=models.CharField(max_length=50, verbose_name='matricula'),
        ),
        migrations.AlterField(
            model_name='alumnos',
            name='nombres',
            field=models.CharField(max_length=80, verbose_name='nombres'),
        ),
    ]
