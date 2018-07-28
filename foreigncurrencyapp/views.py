from django.http import HttpResponseRedirect
from django.shortcuts import get_object_or_404, render
from django.urls import reverse
from django.core.paginator import EmptyPage, PageNotAnInteger, Paginator
from django.views import generic
from .models import ForeignCurrency

class IndexView(generic.ListView):
    template_name = 'foreigncurrencyapp/index.html'
    context_object_name = 'foreignCurrencies'
    paginate_by = 1

    def get_queryset(self):
        return ForeignCurrency.objects.order_by('currency_name')