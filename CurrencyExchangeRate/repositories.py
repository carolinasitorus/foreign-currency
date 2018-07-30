from .models import CurrencyExchangeRate
from django.db.models import Avg, Max, Q
from datetime import date, datetime, timedelta

class CurrencyExchangeRateRepository:

    def getCurrencyExchangeRates():
        return CurrencyExchangeRate.objects.all()

    def getCurrencyExchangeRateBylastDays(daysParam):
        return CurrencyExchangeRate.objects.\
            filter(exchange_date__lte=datetime.today(), exchange_date__gt=datetime.today()-timedelta(days=daysParam)).\
            values('from_id', 'to_id', 'exchange_date')

    def getCurrencyExchangeRateAverageByDate():
    	return CurrencyExchangeRate.objects.\
    	    filter(exchange_date__date=date.today()).\
    	    values('from_id', 'to_id').\
    	    annotate(avg_rate=Avg('rate'))

    def getLatestExchangeRate():
    	return CurrencyExchangeRate.objects.aggregate(Max('exchange_date'));