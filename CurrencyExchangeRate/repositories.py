from .models import CurrencyExchangeRate
from django.db.models import Avg, Count, Max, Q
from datetime import date, datetime, timedelta

class CurrencyExchangeRateRepository:

    def getCurrencyExchangeRates():
        return CurrencyExchangeRate.objects.exclude(deleted_at__isnull=False)

    def getCurrencyExchangeRateBylastDays(currencyPairId, currentDate, daysParam):
        currentDateMaxDatetime = datetime.combine(currentDate, datetime.max.time());
        currentDateMinDatetime = datetime.combine(currentDate, datetime.min.time());
        return CurrencyExchangeRate.objects.\
            filter(currency_pair_id =  currencyPairId).\
            filter(exchange_date__lte = currentDateMaxDatetime, exchange_date__gt = currentDateMinDatetime - timedelta(days = daysParam)).\
            values('currency_pair_id').\
            annotate(days_rate_avg=Avg('rate'))

    def getCurrencyExchangeRateByDate(currentDate, daysParam):
        currentDateMaxDatetime = datetime.combine(currentDate, datetime.max.time());
        currentDateMinDatetime = datetime.combine(currentDate, datetime.min.time());
        return CurrencyExchangeRate.objects.\
            filter(currency_pair_id =  currencyPairId).\
            filter(exchange_date__lte = currentDateMaxDatetime, exchange_date__gt = currentDateMinDatetime - timedelta(days = daysParam)).\
            values('currency_pair_id').\
            annotate(days_rate_avg=Avg('rate'))

    def getCurrencyExchangeRateAverageByDate():
    	return CurrencyExchangeRate.objects.\
    	    filter(exchange_date__date=date.today()).\
    	    values('currency_pair_id').\
    	    annotate(avg_rate=Avg('rate'))

    def getLatestExchangeRate():
    	return CurrencyExchangeRate.objects.aggregate(Max('exchange_date'));

    def getLatestExchangeRate(exchange_date):
        return CurrencyExchangeRate.objects.filter(exchange_date__date=exchange_date).\
            values('currency_pair_id').\
            annotate(latest_rate=Max('exchange_date'))

    def getRateByCurrencyPairIdByExchangeDate(currencyPairId, exchangeDate):
        return CurrencyExchangeRate.objects.filter(currency_pair_id=currencyPairId).\
            filter(exchange_date=exchangeDate).\
            first()

    def getLatestExchangeRateByCurrencyPairId(currencyPairId):
        return CurrencyExchangeRate.objects.\
            filter(currency_pair_id = currencyPairId).\
            order_by('-exchange_date')[:7]
