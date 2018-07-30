from rest_framework import serializers
from .models import CurrencyPair
from Currency.serializers import CurrencySerializer

class CurrencyPairSerializer(serializers.ModelSerializer):
    class Meta:
        model=CurrencyPair
        fields=('id','from_id','to_id', 'deleted_at')

    def to_representation(self, instance):
        self.fields['from_id'] =  CurrencySerializer(read_only=True)
        self.fields['to_id'] =  CurrencySerializer(read_only=True)
        return super(CurrencyPairSerializer, self).to_representation(instance)