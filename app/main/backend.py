from django.http.response import Http404
from django.shortcuts import render
from rest_framework.views import APIView
from .models import groceries
from .serializers import TodoSerializer
from rest_framework.response import Response


class CrudAPIView(APIView):
    # READ a single groceries
    def get_object(self, pk):
        try:
            return groceries.objects.get(pk=pk)
        except groceries.DoesNotExist:
            raise Http404

    def get(self, request, pk=None, format=None):
        if pk:
            data = self.get_object(pk)
            serializer = TodoSerializer(data)

        else:
            data = groceries.objects.all()
            serializer = TodoSerializer(data, many=True)

            return Response(serializer.data)

    # CREATE
    def post(self, request, format=None):
        data = request.data
        serializer = TodoSerializer(data=data)

        serializer.is_valid(raise_exception=True)

        serializer.save()

        response = Response()

        response.data = {
            'message': 'Item Added Successfully',
            'data': serializer.data
        }

        return response
