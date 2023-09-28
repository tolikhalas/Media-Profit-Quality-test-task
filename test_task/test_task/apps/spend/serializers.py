from rest_framework import serializers
from .models import SpendStatistic


class SpendStatisticSerializer(serializers.ModelSerializer):

    total_spend = serializers.IntegerField(read_only=True)
    total_impressions = serializers.IntegerField(read_only=True)
    total_clicks = serializers.IntegerField(read_only=True)
    total_conversion = serializers.IntegerField(read_only=True)
    total_related_revenue = serializers.IntegerField(read_only=True)

    class Meta:
        model = SpendStatistic
        fields = ['id', 'name', 'date', 'spend', 'impressions',
                  'clicks', 'conversion', 'total_spend', 'total_impressions', 'total_clicks',
                  'total_conversion', 'total_related_revenue']
