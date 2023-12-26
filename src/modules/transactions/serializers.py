from rest_framework import serializers
from .models import Transactions


class TransactionsSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Transactions
        fields = ("id", "url", "sender", "receiver", "amount", "created_at", "updated_at")