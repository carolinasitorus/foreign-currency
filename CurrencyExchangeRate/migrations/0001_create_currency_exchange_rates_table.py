# Generated by Django 2.0.7 on 2018-07-29 17:25

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='CurrencyExchangeRate',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('from_id', models.IntegerField()),
                ('to_id', models.IntegerField()),
                ('date', models.DateTimeField(blank=True, null=True)),
                ('rate', models.FloatField(blank=True, null=True)),
                ('deleted_at', models.DateTimeField(blank=True, null=True)),
            ],
            options={
                'db_table': 'currency_exchange_rates',
            },
        ),
    ]
