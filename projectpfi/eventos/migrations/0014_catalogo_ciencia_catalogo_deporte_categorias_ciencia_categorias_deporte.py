# Generated by Django 3.2.5 on 2023-06-23 18:27

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('eventos', '0013_catalogo_registro_civismo_catalogo'),
    ]

    operations = [
        migrations.CreateModel(
            name='catalogo_ciencia',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('text', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='catalogo_deporte',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('text', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='categorias_deporte',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('text', models.CharField(max_length=100)),
                ('catalogo', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='eventos.catalogo_deporte')),
            ],
        ),
        migrations.CreateModel(
            name='categorias_ciencia',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('text', models.CharField(max_length=100)),
                ('catalogo', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='eventos.catalogo_ciencia')),
            ],
        ),
    ]