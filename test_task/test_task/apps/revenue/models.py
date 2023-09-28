from django.db import models

from test_task.apps.spend.models import SpendStatistic


class RevenueStatistic(models.Model):
    name = models.CharField(max_length=255)
    spend = models.ForeignKey(
        SpendStatistic, on_delete=models.SET_NULL, null=True)
    date = models.DateField()
    revenue = models.DecimalField(max_digits=9, decimal_places=2, default=0)
