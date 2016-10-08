# -*- coding: utf-8 -*-
# Generated by Django 1.10.2 on 2016-10-08 17:48
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('companies', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Client',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255, verbose_name='Nombre')),
                ('last_name', models.CharField(blank=True, max_length=255, null=True)),
                ('id_type', models.CharField(choices=[('per', 'C\xe9dula F\xedsica'), ('jur', 'C\xe9dula Jur\xeddica'), ('pas', 'Pasaporte')], default='per', max_length=3, verbose_name='Tipo de Identificaci\xf3n')),
                ('id_num', models.CharField(blank=True, max_length=255, null=True, verbose_name='Num Identificaci\xf3n')),
                ('address', models.CharField(blank=True, max_length=255, null=True, verbose_name='Direcci\xf3n')),
                ('phone', models.CharField(blank=True, max_length=20, null=True, verbose_name='Tel\xe9fono')),
                ('email', models.EmailField(blank=True, max_length=254, null=True, verbose_name='Email')),
                ('has_credit', models.BooleanField(default=False, verbose_name='Tiene Cr\xe9dito?')),
                ('credit_limit', models.DecimalField(blank=True, decimal_places=2, max_digits=11, null=True, verbose_name='L\xedmite de Cr\xe9dito')),
                ('debt', models.DecimalField(blank=True, decimal_places=2, max_digits=11, null=True, verbose_name='Saldo')),
                ('credit_days', models.PositiveIntegerField(blank=True, default=30, null=True, verbose_name='D\xedas de Cr\xe9dito')),
                ('company', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='companies.Company', verbose_name='Empresa')),
            ],
            options={
                'ordering': ['id'],
                'verbose_name': 'Cliente',
                'verbose_name_plural': 'Clientes',
            },
        ),
    ]
