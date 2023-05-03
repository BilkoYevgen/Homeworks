from rest_framework import serializers
from .models import Purchase, Book, User


class PurchaseSerializer(serializers.ModelSerializer):
    user = serializers.PrimaryKeyRelatedField(queryset=User.objects.all())
    book = serializers.PrimaryKeyRelatedField(queryset=Book.objects.all())

    class Meta:
        model = Purchase
        fields = ('user', 'book', 'date')