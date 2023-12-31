# Generated by Django 3.2.5 on 2021-10-05 00:48

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('eventos', '0007_auto_20211001_2145'),
        ('Alumnos', '0002_alter_alumnos_carrera'),
        ('FormacionIntegral', '0005_auto_20211004_1947'),
    ]

    operations = [
        migrations.AlterField(
            model_name='formacionintegral',
            name='alumno',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='Alumnos.alumnos', verbose_name='alumno_id'),
        ),
        migrations.AlterField(
            model_name='formacionintegral',
            name='evento',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='eventos.eventos', verbose_name='evento_id'),
        ),
    ]
