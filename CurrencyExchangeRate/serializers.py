from rest_framework import serializers
from .models import CurrencyExchangeRate
from Currency.serializers import CurrencySerializer

class CurrencyExchangeRateSerializer(serializers.ModelSerializer):
    class Meta:
        model=CurrencyExchangeRate
        fields=('id','from_id','to_id','exchange_date','rate','deleted_at')

    def to_representation(self, instance):
        self.fields['from_id'] =  CurrencySerializer(read_only=True)
        self.fields['to_id'] =  CurrencySerializer(read_only=True)
        return super(CurrencyExchangeRateSerializer, self).to_representation(instance)