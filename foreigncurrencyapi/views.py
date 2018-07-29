from foreigncurrencyapp.models import ForeignCurrency
from foreigncurrencyapi.serializers import ForeignCurrencySerializer
from django.http import Http404
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

class ForeignCurrencyList(APIView):
    """
    List all snippets, or create a new snippet.
    """
    def get(self, request, format=None):
        snippets = ForeignCurrency.objects.all()
        serializer = ForeignCurrencySerializer(snippets, many=True)
        return Response(serializer.data)

    def post(self, request, format=None):
        serializer = ForeignCurrencySerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class ForeignCurrencyDetail(APIView):
    """
    Retrieve, update or delete a snippet instance.
    """
    def get_object(self, pk):
        try:
            return ForeignCurrency.objects.get(pk=pk)
        except ForeignCurrency.DoesNotExist:
            raise Http404

    def get(self, request, pk, format=None):
        snippet = self.get_object(pk)
        serializer = ForeignCurrencySerializer(snippet)
        return Response(serializer.data)

    def put(self, request, pk, format=None):
        snippet = self.get_object(pk)
        serializer = ForeignCurrencySerializer(snippet, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk, format=None):
        snippet = self.get_object(pk)
        snippet.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

# @api_view(['GET', 'POST'])
# def foreigncurrency_list(request):
#     """
#     List all code snippets, or create a new snippet.
#     """
#     if request.method == 'GET':
#         foreigncurrencies = ForeignCurrency.objects.all()
#         serializer = ForeignCurrencySerializer(foreigncurrencies, many=True)
#         # return JsonResponse(serializer.data, safe=False)
#         return Response(serializer.data)

#     elif request.method == 'POST':
#         serializer = ForeignCurrencySerializer(data=request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data, status=status.HTTP_201_CREATED)
#         return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

# @api_view(['GET', 'PUT', 'DELETE'])
# def foreigncurrency_detail(request, pk):
#     """
#     Retrieve, update or delete a code snippet.
#     """
#     try:
#         foreigncurrency = ForeignCurrency.objects.get(pk=pk)
#     except ForeignCurrency.DoesNotExist:
#         return Response(status=status.HTTP_404_NOT_FOUND)

#     if request.method == 'GET':
#         serializer = ForeignCurrencySerializer(foreigncurrency)
#         return Response(serializer.data)

#     elif request.method == 'PUT':
#         serializer = SnippetSerializer(snippet, data=request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data)
#         return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

#     elif request.method == 'DELETE':
#         foreigncurrency.delete()
#         return Response(status=status.HTTP_204_NO_CONTENT)