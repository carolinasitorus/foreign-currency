from rest_framework import serializers
from .models import CurrencyExchangeRate


class CurrencyExchangeRateSerializer(serializers.Serializer):
    exchange_date = serializers.DateTimeField(required=True)
    from_id = serializers.StringRelatedField()
    to_id = serializers.StringRelatedField()
    rate = serializers.FloatField()
    deleted_at = serializers.DateTimeField(required=False)

    def create(self, validated_data):
        return CurrencyExchangeRate.objects.create(**validated_data)

    def update(self, instance, validated_data):
        instance.date = validated_data.get('exchange_date', instance.date)
        instance.from_id = validated_data.get('from_id', instance.from_id)
        instance.to_id = validated_data.get('to_id', instance.to_id)
        instance.rate = validated_data.get('rate', instance.rate)
        instance.deleted_at = validated_data.get('deleted_at', instance.deleted_at)
        instance.save()
        return instance
