from django.urls import reverse
from django.test import TestCase
from rest_framework import status
from rest_framework.test import APITestCase
from ..models import Currency
from ..repositories import CurrencyRepository

class ViewTestCase(TestCase):

    def testCurrencyListGet(self):
        response = self.client.get('/api/v1/currencies/')
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.data, CurrencyRepository.getCurrencies())

    def testCurrencyListPost(self):
        data = {'currency_name': 'USD'}
        response = self.client.post('api/v1/currencies', data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(Currency.objects.count(), 1)
        self.assertEqual(Currency.objects.get().name, 'USD')