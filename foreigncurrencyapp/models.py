from django.db import models

class ForeignCurrency(models.Model):
    currency_name = models.CharField(max_length=25, blank=True, null=True)
    description = models.CharField(max_length=225, blank=True, null=True)
    deleted_at = models.DateTimeField(blank=True, null=True)

    class Meta:
        db_table = 'foreign_currencies'

    def __str__(self):
        return self.currency_name
