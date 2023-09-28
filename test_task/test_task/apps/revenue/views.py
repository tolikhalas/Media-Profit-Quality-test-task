from rest_framework.views import APIView
from rest_framework.response import Response
from django.db.models import Sum
from rest_framework import status

from .models import RevenueStatistic
from test_task.apps.spend.models import SpendStatistic
from .serializers import RevenueStatisticRerializer


class RevenueList(APIView):

    def get(self, request, format=None):
        revenue_list = RevenueStatistic.objects.values('date', 'name').annotate(
            total_spend=Sum('spend_id__spend'),
            total_revenue=Sum('revenue'),
            total_impressions=Sum('spend_id__impressions'),
            total_clicks=Sum('spend_id__clicks'),
            total_conversion=Sum('spend_id__conversion')
        )
        serializer = RevenueStatisticRerializer(revenue_list, many=True)

        return Response(serializer.data, status=status.HTTP_200_OK)
