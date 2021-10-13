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

    # READ all groceries
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

    # UPDATE
    def put(self, request, pk=None, format=None):
            # Get the todo to update
        todo_to_update = groceries.objects.get(pk=pk)

        # Pass the instance to update to the serializer, and the data and also partial to the serializer
        # Passing partial will allow us to update without passing the entire Todo object
        serializer = TodoSerializer(
            instance=todo_to_update, data=request.data, partial=True)

        serializer.is_valid(raise_exception=True)
        serializer.save()
        response = Response()

        response.data = {
            'message': 'Item Updated Successfully',
            'data': serializer.data
        }

        return response

    # DELETED
    def delete(self, request, pk, format=None):
        todo_to_delete =  groceries.objects.get(pk=pk)

        # delete the todo
        todo_to_delete.delete()

        return Response({
            'message': 'Item Deleted Successfully'
        })

        
