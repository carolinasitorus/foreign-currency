from rest_framework import serializers
from .models import CurrencyExchangeRate
from CurrencyPair.serializers import CurrencyPairSerializer

class CurrencyExchangeRateSerializer(serializers.ModelSerializer):
    class Meta:
        model=CurrencyExchangeRate
        fields=('id','currency_pair_id','exchange_date', 'rate', 'deleted_at')

    def to_representation(self, instance):
        self.fields['currency_pair_id'] =  CurrencyPairSerializer(read_only=True)
        return super(CurrencyExchangeRateSerializer, self).to_representation(instance)

class CurrencyExchangeRateByExchangeDateSerializer(serializers.ModelSerializer):
    class Meta:
        model=CurrencyExchangeRate
        fields=('id','currency_pair_id','exchange_date', 'rate', 'deleted_at')

    def to_representation(self, instance):
        self.fields['currency_pair_id'] =  CurrencyPairSerializer(read_only=True)
        return super(CurrencyExchangeRateByExchangeDateSerializer, self).to_representation(instance)