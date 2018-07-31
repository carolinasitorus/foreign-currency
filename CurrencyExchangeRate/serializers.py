from rest_framework import serializers
from .models import CurrencyExchangeRate
from .repositories import CurrencyExchangeRateRepository
from CurrencyPair.repositories import CurrencyPairRepository
from CurrencyPair.serializers import CurrencyPairSerializer
from CurrencyPair.models import CurrencyPair

class CurrencyExchangeRateSerializer(serializers.ModelSerializer):
    class Meta:
        model=CurrencyExchangeRate
        fields=('id','currency_pair_id','exchange_date', 'rate', 'deleted_at')

    def to_representation(self, instance):
        self.fields['currency_pair_id'] =  CurrencyPairSerializer(read_only=True)
        return super(CurrencyExchangeRateSerializer, self).to_representation(instance)

class CurrencyExchangeRateByExchangeDateSerializer(serializers.ModelSerializer):
    avg_rate_of_7_latest_days = serializers.SerializerMethodField('getDaysRateAvg')
    currency_from_name = serializers.SerializerMethodField('getCurrencyFromName')
    currency_to_name = serializers.SerializerMethodField('getCurrencyToName')
    date = serializers.SerializerMethodField('getExchangeDate')
    rate = serializers.SerializerMethodField('getRate')

    def getCurrencyPairId(self, rates):
        return rates['currency_pair_id']

    def getCurrencyFromName(self, rates):
        currencyPairId = self.getCurrencyPairId(rates)
        currencies = CurrencyPairRepository.getCurrencyById(currencyPairId)
        serializer = CurrencyPairSerializer(currencies)
        return serializer.data['from_id']['name']

    def getCurrencyToName(self, rates):
        currencyPairId = rates['currency_pair_id']
        currencyPair = CurrencyPairRepository.getCurrencyById(currencyPairId)
        serializer = CurrencyPairSerializer(currencyPair)
        return serializer.data['to_id']['name']

    def getDaysRateAvg(self, rates):
        currencyPairId = rates['currency_pair_id']
        currentDate = self.getExchangeDate(rates)
        days = 7
        currency = CurrencyExchangeRateRepository.getCurrencyExchangeRateBylastDays(currencyPairId, currentDate, days)
        return currency[0]['days_rate_avg']

    def getExchangeDate(self, rates):
        return rates['latest_rate'].date()

    def getRate(self, rates):
        currencyPairId = self.getCurrencyPairId(rates)
        exchangeDate = rates['latest_rate']
        currencyExchangeRate = CurrencyExchangeRateRepository.getRateByCurrencyPairIdByExchangeDate(currencyPairId, exchangeDate)
        serializer = CurrencyExchangeRateSerializer(currencyExchangeRate)
        return serializer.data['rate']

    class Meta:
        model=CurrencyExchangeRate
        fields=('id','currency_from_name', 'currency_to_name', 'rate', 'date', 'avg_rate_of_7_latest_days')

class CurrencyExchangeRateTrendSerializer(serializers.ModelSerializer):
    date = serializers.SerializerMethodField('getExchangeDate')

    def getExchangeDate(self, rates):
        return rates.exchange_date.date()

    class Meta:
        model=CurrencyExchangeRate
        fields=('date', 'rate')

class SectionSerializer(serializers.ModelSerializer):
    avg = serializers.SerializerMethodField('getAvg')
    currency_from = serializers.SerializerMethodField('getCurrencyFromName')
    currency_to = serializers.SerializerMethodField('getCurrencyToName')
    date = serializers.SerializerMethodField('getDate')
    variance = serializers.SerializerMethodField('getVariance')
    
    def getAvg(self, instance):
        return self.context['avg']

    def getCurrencyFromName(self, rates):
        return rates.currency_pair_id.from_id.name

    def getCurrencyToName(self, rates):
        return rates.currency_pair_id.to_id.name

    def getDate(selft, rates):
        return rates.exchange_date.date()

    def getVariance(self, instance):
        return self.context['variance']

    class Meta:
        model = CurrencyExchangeRate
        fields=('id', 'currency_from', 'currency_to', 'rate', 'date', 'avg', 'variance')

