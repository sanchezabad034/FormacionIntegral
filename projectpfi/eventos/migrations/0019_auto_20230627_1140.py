# Generated by Django 3.2.5 on 2023-06-27 17:40

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('eventos', '0018_arte_categorias'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='eventos',
            name='subCategoria',
        ),
        migrations.AddField(
            model_name='eventos',
            name='subCategoria1',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='categorias1', to='eventos.catalogo_categorias'),
        ),
        migrations.AddField(
            model_name='eventos',
            name='subCategoria2',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='categorias2', to='eventos.catalogo_categorias2'),
        ),
        migrations.AddField(
            model_name='eventos',
            name='subCategoriaArte',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='categoriasArte', to='eventos.arte_categorias'),
        ),
        migrations.AlterField(
            model_name='eventos',
            name='categorias',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='categorias', to='eventos.clasifi_cat'),
        ),
    ]
