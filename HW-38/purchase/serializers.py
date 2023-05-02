from rest_framework import serializers
from .models import Purchase


class PurchaseSerializer(serializers.ModelSerializer):
    user = serializers.SerializerMethodField()
    book = serializers.SerializerMethodField()

    def get_user(self, obj):
        return f"{obj.user.first_name} {obj.user.last_name}"

    def get_book(self, obj):
        return f"{obj.book.title} by {obj.book.author}"

    class Meta:
        model = Purchase
        fields = ('user', 'book', 'date')