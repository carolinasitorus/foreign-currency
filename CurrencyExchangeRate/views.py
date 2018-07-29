from .models import CurrencyExchangeRate
from .serializers import CurrencyExchangeRateSerializer
from django.http import Http404
from rest_framework.views import APIView
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

class CurrencyExchangeRateList(APIView):
    def get(self, request, format=None):
        currencies = CurrencyExchangeRate.objects.all()
        serializer = CurrencyExchangeRateSerializer(currencies, many=True)
        return Response(serializer.data)

    def post(self, request, format=None):
        serializer = CurrencyExchangeRateSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class CurrencyExchangeRateDetail(APIView):
    def get_object(self, pk):
        try:
            return CurrencyExchangeRate.objects.get(pk=pk)
        except CurrencyExchangeRate.DoesNotExist:
            raise Http404

    def get(self, request, pk, format=None):
        currency = self.get_object(pk)
        serializer = CurrencyExchangeRateSerializer(currency)
        return Response(serializer.data)

    def put(self, request, pk, format=None):
        currency = self.get_object(pk)
        serializer = CurrencyExchangeRateSerializer(currency, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk, format=None):
        currency = self.get_object(pk)
        currency.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)