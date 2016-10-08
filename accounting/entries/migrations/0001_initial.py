# -*- coding: utf-8 -*-
# Generated by Django 1.10.2 on 2016-10-08 17:48
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('suppliers', '0001_initial'),
        ('clients', '0001_initial'),
        ('accounts', '0001_initial'),
        ('currencies', '0001_initial'),
        ('companies', '0001_initial'),
        ('fiscalPeriods', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Entry',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('entry_number', models.PositiveIntegerField(verbose_name='Consecutivo')),
                ('date', models.DateField(verbose_name='Fecha')),
                ('cost_center', models.PositiveIntegerField(verbose_name='Centro de Costos')),
                ('exchange_rate', models.DecimalField(decimal_places=6, max_digits=10, verbose_name='Tipo de Cambio')),
                ('status', models.CharField(max_length=255, verbose_name='Estado')),
                ('typing_user', models.PositiveIntegerField(verbose_name='Registrador')),
                ('auth_user', models.PositiveIntegerField(verbose_name='Integrador')),
                ('company', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='companies.Company', verbose_name='Empresa')),
                ('currency', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='currencies.Currency', verbose_name='Moneda')),
                ('fiscal_period', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='fiscalPeriods.FiscalPeriod', verbose_name='Periodo Fiscal')),
            ],
            options={
                'ordering': ['id'],
                'verbose_name': 'Asiento',
                'verbose_name_plural': 'Asientos',
            },
        ),
        migrations.CreateModel(
            name='EntryDetail',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('cash_flow', models.CharField(max_length=255, verbose_name='Flujo de Caja')),
                ('document', models.PositiveIntegerField(verbose_name='Documento')),
                ('reference', models.PositiveIntegerField(verbose_name='Referencia')),
                ('credit', models.FloatField(verbose_name='Debe')),
                ('debit', models.FloatField(verbose_name='Haber')),
                ('balance', models.FloatField(verbose_name='Diferencia')),
                ('account', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='accounts.Account', verbose_name='Cuenta')),
                ('client', models.ManyToManyField(blank=True, to='clients.Client', verbose_name='Cliente')),
                ('entry', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='entries.Entry', verbose_name='Asiento')),
                ('supplier', models.ManyToManyField(blank=True, to='suppliers.Supplier', verbose_name='Proveedor')),
            ],
            options={
                'ordering': ['id'],
                'verbose_name': 'Detalle de Asiento',
                'verbose_name_plural': 'Detalles de Asiento',
            },
        ),
    ]
