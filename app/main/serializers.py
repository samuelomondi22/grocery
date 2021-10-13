from rest_framework import serializers
from .models import groceries


class TodoSerializer(serializers.ModelSerializer):
    class Meta:
        model = groceries
        fields = "__all__"
