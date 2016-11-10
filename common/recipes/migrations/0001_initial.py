# -*- coding: utf-8 -*-
# Generated by Django 1.10.2 on 2016-11-08 21:52
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('products', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Recipe',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('productForSale', models.OneToOneField(null=True, on_delete=django.db.models.deletion.CASCADE, to='products.ProductForSale', verbose_name='Producto de Venta')),
            ],
            options={
                'ordering': ['id'],
                'verbose_name': 'Receta',
                'verbose_name_plural': 'Recetas',
            },
        ),
        migrations.CreateModel(
            name='RecipeDetail',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('qty', models.FloatField(verbose_name='Cantidad')),
                ('from_recipe', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='from_recipe', to='recipes.Recipe')),
                ('to_recipe', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='to_recipe', to='recipes.Recipe')),
            ],
            options={
                'ordering': ['id'],
                'verbose_name': 'Detalle de Receta',
                'verbose_name_plural': 'Detalles de Receta',
            },
        ),
        migrations.CreateModel(
            name='SubRecipe',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('qty', models.FloatField(default=1, null=True, verbose_name='Cantidad')),
                ('product', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='products.Product', verbose_name='Producto Bodega')),
                ('recipe', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='recipes.Recipe', verbose_name='Receta')),
            ],
            options={
                'ordering': ['id'],
                'verbose_name': 'Sub-Receta',
                'verbose_name_plural': 'Sub-Recetas',
            },
        ),
        migrations.AddField(
            model_name='recipe',
            name='recipes',
            field=models.ManyToManyField(blank=True, through='recipes.RecipeDetail', to='recipes.Recipe'),
        ),
        migrations.AlterUniqueTogether(
            name='recipedetail',
            unique_together=set([('from_recipe', 'to_recipe')]),
        ),
    ]
