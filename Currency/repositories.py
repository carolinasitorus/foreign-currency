from .models import Currency

class CurrencyRepository:

    def getCurrencies():
        return Currency.objects.exclude(deleted_at__isnull=False)