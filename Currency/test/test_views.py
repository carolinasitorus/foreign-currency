from django.urls import reverse
from django.test import TestCase
from rest_framework import status
from rest_framework.test import APITestCase
from ..models import Currency
from ..repositories import CurrencyRepository
from ..views import CurrencyList
from rest_framework.test import APIRequestFactory
import json as simplejson

class ViewTestCase(TestCase):

    def testCurrencyListGet(self):
        response = self.client.get('/api/v1/currencies/')
        self.assertEqual(response.status_code, 200)
        self.assertEqual(len(response.data['results']), len(CurrencyRepository.getCurrencies()))

    def testCurrencyListPost(self):
        factory = APIRequestFactory()
        request = factory.post('/api/v1/currencies/', {"currency_name": "USD"} , content_type='application/json')
        view = CurrencyList.as_view()
        response = view(request)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(Currency.objects.count(), 1)
        self.assertEqual(Currency.objects.get().name, 'USD')