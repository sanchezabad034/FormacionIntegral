# Generated by Django 3.2.5 on 2022-01-13 02:36

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('Alumnos', '0002_alter_alumnos_carrera'),
        ('eventos', '0009_auto_20211011_2042'),
    ]

    operations = [
        migrations.CreateModel(
            name='eventosSubirevidenciasAlumno',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('img', models.ImageField(upload_to='EvidenciasAlumnos/images')),
                ('alumno', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Alumnos.alumnos')),
                ('evento', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='eventos.eventos')),
            ],
        ),
    ]
