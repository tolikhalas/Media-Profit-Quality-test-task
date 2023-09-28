from rest_framework.views import APIView
from rest_framework.response import Response
from django.db.models import Sum

from .serializers import SpendStatisticSerializer
from .models import SpendStatistic
from test_task.apps.revenue.models import RevenueStatistic


class SpendStatisticView(APIView):
    def get(self, request, format=None):
        spend_list = SpendStatistic.objects.values('date', 'name').annotate(
            total_spend=Sum('spend'),
            total_impressions=Sum('impressions'),
            total_clicks=Sum('clicks'),
            total_conversion=Sum('conversion'),
            total_related_revenue=Sum('revenuestatistic__revenue')
        )

        serializer = SpendStatisticSerializer(spend_list, many=True)
        return Response(serializer.data, status=200)