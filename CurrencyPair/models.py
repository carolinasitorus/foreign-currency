from Currency.models import Currency
from django.db import models

class CurrencyPair(models.Model):
    from_id = models.ForeignKey(Currency, on_delete=models.CASCADE, related_name='currency_from_id')
    to_id = models.ForeignKey(Currency, on_delete=models.CASCADE, related_name='currency_to_id')
    deleted_at = models.DateTimeField(blank=True, null=True)

    class Meta:
        db_table = 'currency_pairs'
