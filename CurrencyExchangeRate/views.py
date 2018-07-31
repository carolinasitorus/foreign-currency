from .models import CurrencyExchangeRate
from .repositories import CurrencyExchangeRateRepository
from .serializers import SectionSerializer, CurrencyExchangeRateSerializer, CurrencyExchangeRateByExchangeDateSerializer, CurrencyExchangeRateTrendSerializer
from datetime import datetime, date, time
from django.http import Http404
from rest_framework.views import APIView
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework.pagination import PageNumberPagination
from rest_framework.viewsets import ModelViewSet


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

class CurrencyExchangeRateTrend(APIView):
    def get(self, request, currency_pair_id, format=None):
        paginator = PageNumberPagination()
        queryset =  CurrencyExchangeRateRepository.getLatestExchangeRateByCurrencyPairId(currency_pair_id)
        context = paginator.paginate_queryset(queryset, request)
        serializer =  CurrencyExchangeRateTrendSerializer(context, many=True)
        return paginator.get_paginated_response(serializer.data)

class CurrencyExchangeRateViewSet(ModelViewSet):
    serializer_class = SectionSerializer
    def get_queryset(self):
        currencyPairId = self.kwargs['currency_pair_id']
        return CurrencyExchangeRateRepository.getLatestExchangeRateByCurrencyPairId(currencyPairId)

    def get_serializer_context(self):
        context = super(CurrencyExchangeRateViewSet, self).get_serializer_context()
        currencyPairId = self.kwargs['currency_pair_id'] 
        rates = CurrencyExchangeRateRepository.getLatestExchangeRateByCurrencyPairId(currencyPairId)
        avg = self.getAverage(rates)
        variance = self.getVariance(rates)
        context.update({'avg': avg, 'variance' : variance})
        return context

    def getAverage(self, rates):
        rowsTotal = 0;
        rateTotal = 0;
        for rateObj in rates:
            rowsTotal = rowsTotal + 1
            rateTotal = rateTotal + rateObj.rate
        return rateTotal/rowsTotal

    def getVariance(self, rates):
        avg = self.getAverage(rates)
        temp = 0;
        rowsTotal = 0
        for rateObj in rates:
            temp = temp + (rateObj.rate - avg) * (rateObj.rate - avg)
            rowsTotal = rowsTotal + 1
        try:
            variance = temp/(rowsTotal-1)
        except ZeroDivisionError:
            variance =0
        return variance





