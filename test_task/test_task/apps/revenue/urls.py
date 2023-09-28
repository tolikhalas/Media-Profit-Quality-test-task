from django.urls import path

from . import views

urlpatterns = [
    path("", views.RevenueList.as_view())
]
