# from django.conf.urls import url, include
# from foreigncurrencyapp.models import ForeignCurrency
# from rest_framework import routers, serializers, viewsets

# # Serializers define the API representation.
# class UserSerializer(serializers.HyperlinkedModelSerializer):
#     class Meta:
#         model = ForeignCurrency
#         fields = ('id', 'currency_name', 'description', 'deleted_at')

# # ViewSets define the view behavior.
# class ForeignCurrencyViewSet(viewsets.ModelViewSet):
#     queryset = ForeignCurrency.objects.all()
#     serializer_class = UserSerializer

# # Routers provide an easy way of automatically determining the URL conf.
# router = routers.DefaultRouter()
# router.register(r'foreign-currencies', ForeignCurrencyViewSet)

# # Wire up our API using automatic URL routing.
# # Additionally, we include login URLs for the browsable API.
# urlpatterns = [
#     url(r'^/', include(router.urls))
# ]

from django.conf.urls import url
from rest_framework.urlpatterns import format_suffix_patterns
from foreigncurrencyapi import views

urlpatterns = [
    url(r'^/$', views.ForeignCurrencyList.as_view()),
    url(r'^/(?P<pk>[0-9]+)/$', views.ForeignCurrencyDetail.as_view()),
]
urlpatterns = format_suffix_patterns(urlpatterns)