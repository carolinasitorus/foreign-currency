# Generated by Django 2.0.7 on 2018-07-30 18:31

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('CurrencyPair', '0001_create_currency_pairs_table'),
    ]

    operations = [
        migrations.CreateModel(
            name='CurrencyExchangeRate',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('exchange_date', models.DateTimeField(blank=True, null=True)),
                ('rate', models.FloatField(blank=True, null=True)),
                ('deleted_at', models.DateTimeField(blank=True, null=True)),
                ('currency_pair_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='CurrencyPair.CurrencyPair')),
            ],
            options={
                'db_table': 'currency_exchange_rates',
            },
        ),
    ]
