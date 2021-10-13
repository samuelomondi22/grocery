from rest_framework import serializers
from .models import groceries

# helps convert complex data types to python data types and then to convert back to JSON or XML
class TodoSerializer(serializers.ModelSerializer):
    class Meta:
        model = groceries
        fields = "__all__"
