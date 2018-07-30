from rest_framework import serializers
from .models import CurrencyExchangeRate
from Currency.serializers import CurrencySerializer

class CurrencyExchangeRateSerializer(serializers.ModelSerializer):
    class Meta:
        model=CurrencyExchangeRate
        fields=('id','from_id','to_id','exchange_date', 'rate', 'deleted_at')

    def create(self, validated_data):
        print(direction=validated_data['non_field'])

    def to_representation(self, instance):
        self.fields['from_id'] =  CurrencySerializer(read_only=True)
        self.fields['to_id'] =  CurrencySerializer(read_only=True)
        return super(CurrencyExchangeRateSerializer, self).to_representation(instance)

class CurrencyExchangeRateByExchangeDateSerializer(serializers.ModelSerializer):
    class Meta:
        model=CurrencyExchangeRate
        fields=('id','from_id','to_id','exchange_date', 'rate', 'deleted_at')

    def create(self, validated_data):
        print(direction=validated_data['non_field'])

    def to_representation(self, instance):
        self.fields['from_id'] =  CurrencySerializer(read_only=True)
        self.fields['to_id'] =  CurrencySerializer(read_only=True)
        return super(CurrencyExchangeRateByExchangeDateSerializer, self).to_representation(instance)