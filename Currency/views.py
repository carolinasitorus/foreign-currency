from .models import Currency
from .repositories import CurrencyRepository
from .serializers import CurrencySerializer
from datetime import datetime
from django.http import Http404
from rest_framework.views import APIView
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework.pagination import PageNumberPagination

class CurrencyList(APIView):
    def get(self, request, format=None):
        paginator = PageNumberPagination()
        queryset = CurrencyRepository.getCurrencies()
        context = paginator.paginate_queryset(queryset, request)
        serializer = CurrencySerializer(context, many=True)
        return paginator.get_paginated_response(serializer.data)

    def post(self, request, format=None):
        serializer = CurrencySerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class CurrencyDetail(APIView):
    def get_object(self, pk):
        try:
            return Currency.objects.get(pk=pk)
        except Currency.DoesNotExist:
            raise Http404

    def get(self, request, pk, format=None):
        currency = self.get_object(pk)
        serializer = CurrencySerializer(currency)
        return Response(serializer.data)

    def put(self, request, pk, format=None):
        currency = self.get_object(pk)
        serializer = CurrencySerializer(currency, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk, format=None):
        currency = self.get_object(pk)
        currency.deleted_at = datetime.now()
        currency.save()
        serializer = CurrencySerializer(currency)
        return Response(serializer.data)