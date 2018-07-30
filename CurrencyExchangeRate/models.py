from CurrencyPair.models import CurrencyPair
from django.db import models

class CurrencyExchangeRate(models.Model):
    currency_pair_id = models.ForeignKey(CurrencyPair, on_delete=models.CASCADE)
    exchange_date = models.DateTimeField(blank=True, null=True)
    rate = models.FloatField(blank=True, null=True)
    deleted_at = models.DateTimeField(blank=True, null=True)

    class Meta:
        db_table = 'currency_exchange_rates'
