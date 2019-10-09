from rest_framework import serializers
from .models import Stock


class StockSerializer(serializers.ModelSerializer):
    class Meta:
        model = Stock
        # fiels = ('ticker', 'volume')
        fields = '__all__'
