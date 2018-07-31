from django.test import TestCase
from ..models import Currency

class ModelTestCase(TestCase):

    def setUp(self):
        self.currency_name = "IDR"
        self.currency = Currency(name=self.currency_name)

    def testModelCanCreateCurrency(self):
        old_count = Currency.objects.count()
        self.currency.save()
        new_count = Currency.objects.count()
        self.assertNotEqual(old_count, new_count)