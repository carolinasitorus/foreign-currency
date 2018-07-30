from Currency.models import Currency
from django.db import models

class CurrencyExchangeRate(models.Model):
    from_id = models.ForeignKey(Currency, on_delete=models.CASCADE, related_name='currency_from_id')
    to_id = models.ForeignKey(Currency, on_delete=models.CASCADE, related_name='currency_to_id')
    exchange_date = models.DateTimeField(blank=True, null=True)
    rate = models.FloatField(blank=True, null=True)
    deleted_at = models.DateTimeField(blank=True, null=True)

    class Meta:
        db_table = 'currency_exchange_rates'
