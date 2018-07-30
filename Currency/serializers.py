from rest_framework import serializers
from .models import Currency


class CurrencySerializer(serializers.Serializer):
    id = serializers.IntegerField(read_only=True)
    name = serializers.CharField(max_length=25, allow_blank=True)
    description = serializers.CharField(required=False, max_length=225, allow_blank=True)
    deleted_at = serializers.DateTimeField(required=False)

    def create(self, validated_data):
        return Currency.objects.create(**validated_data)

    def update(self, instance, validated_data):
        instance.name = validated_data.get('name', instance.name)
        instance.description = validated_data.get('description', instance.description)
        instance.deleted_at = validated_data.get('deleted_at', instance.deleted_at)
        instance.save()
        return instance
