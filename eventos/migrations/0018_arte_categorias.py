# Generated by Django 3.2.5 on 2023-06-26 18:01

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('eventos', '0017_auto_20230626_1031'),
    ]

    operations = [
        migrations.CreateModel(
            name='arte_categorias',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('text', models.CharField(max_length=100)),
                ('categoria', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='eventos.catalogo_categorias2')),
            ],
        ),
    ]
