from django.test import TestCase
from rest_framework import status
from ..repositories import CurrencyPairRepository

class ViewTestCase(TestCase):

    def testCurrencyPairListGet(self):
        response = self.client.get('/api/v1/currency-pairs/')
        self.assertEqual(response.status_code, 200)
        self.assertEqual(len(response.data['results']), len(CurrencyPairRepository.getCurrencyPairs()))
