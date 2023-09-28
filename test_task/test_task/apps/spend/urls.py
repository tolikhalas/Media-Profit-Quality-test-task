from django.urls import path
from . import views

urlpatterns = [
    path('', views.SpendStatisticView.as_view())
]

