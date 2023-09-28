from rest_framework import serializers
from .models import RevenueStatistic


class RevenueStatisticRerializer(serializers.ModelSerializer):

    total_spend = serializers.IntegerField()
    total_revenue = serializers.IntegerField()
    total_impressions = serializers.IntegerField()
    total_clicks = serializers.IntegerField()
    total_conversion = serializers.IntegerField()

    class Meta:
        model = RevenueStatistic
        fields = ['name', 'spend', 'date', 'revenue', 'total_spend', 'total_revenue', 'total_impressions', 'total_clicks',
                  'total_conversion']
