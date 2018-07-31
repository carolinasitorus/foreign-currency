from .models import CurrencyPair

class CurrencyPairRepository:

    def getCurrencyPairs():
        return CurrencyPair.objects.exclude(deleted_at__isnull=False)

    def getCurrencyById(currencyPairId):
    	return CurrencyPair.objects.get(pk=currencyPairId)