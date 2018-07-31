from django.test import TestCase
from rest_framework import status
from ..repositories import CurrencyExchangeRateRepository

class ViewTestCase(TestCase):

    def testCurrencyExchangeRateListGet(self):
        response = self.client.get('/api/v1/currency-exchange-rates/')
        self.assertEqual(response.status_code, 200)
        self.assertEqual(len(response.data['results']), len(CurrencyExchangeRateRepository.getCurrencyExchangeRates()))
