from rest_framework import serializers
from foreigncurrencyapp.models import ForeignCurrency


class ForeignCurrencySerializer(serializers.Serializer):
    id = serializers.IntegerField(read_only=True)
    currency_name = serializers.CharField(max_length=25, allow_blank=True)
    description = serializers.CharField(required=False, max_length=225, allow_blank=True)
    deleted_at = serializers.DateTimeField(required=False)

    def create(self, validated_data):
        """
        Create and return a new `ForeignCurrency` instance, given the validated data.
        """
        return ForeignCurrency.objects.create(**validated_data)

    def update(self, instance, validated_data):
        """
        Update and return an existing `ForeignCurrency` instance, given the validated data.
        """
        instance.currency_name = validated_data.get('currency_name', instance.currency_name)
        instance.description = validated_data.get('description', instance.description)
        instance.deleted_at = validated_data.get('deleted_at', instance.deleted_at)
        instance.save()
        return instance
