from django.conf.urls import url
from rest_framework.urlpatterns import format_suffix_patterns
from . import views

urlpatterns = [
    url(r'^/$', views.CurrencyExchangeRateList.as_view()),
    url(r'^/(?P<exchange_date>\d{4}-\d{2}-\d{2})/$', views.CurrencyExchangeRateByExchangeDate.as_view()),
    # url(r'^/(?P<pk>[0-9]+)/$', views.CurrencyExchangeRateDetail.as_view()),
]
urlpatterns = format_suffix_patterns(urlpatterns)