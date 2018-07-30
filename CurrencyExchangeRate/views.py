from .models import CurrencyExchangeRate
from .repositories import CurrencyExchangeRateRepository
from .serializers import CurrencyExchangeRateSerializer, CurrencyExchangeRateByExchangeDateSerializer
from datetime import datetime, date, time
from django.http import Http404
from rest_framework.views import APIView
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework.pagination import PageNumberPagination


class CurrencyExchangeRateList(APIView):
    def get(self, request, format=None):
        paginator = PageNumberPagination()
        queryset = CurrencyExchangeRateRepository.getCurrencyExchangeRates()
        context = paginator.paginate_queryset(queryset, request)
        serializer = CurrencyExchangeRateSerializer(context, many=True)
        return paginator.get_paginated_response(serializer.data)

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

class CurrencyExchangeRateByExchangeDate(APIView):
    def get(self, request, exchange_date, format=None):
        paginator = PageNumberPagination()
        queryset =  CurrencyExchangeRateRepository.getLatestExchangeRate(exchange_date)
        context = paginator.paginate_queryset(queryset, request)
        serializer = CurrencyExchangeRateByExchangeDateSerializer(context, many=True)
        return paginator.get_paginated_response(serializer.data)