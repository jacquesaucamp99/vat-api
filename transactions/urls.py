"""Application URL configuration for the transactions app."""

from django.urls import include, path
from rest_framework.routers import DefaultRouter

from .views import TransactionViewSet, dashboard

router = DefaultRouter()
router.register(r"transactions", TransactionViewSet, basename="transaction")

urlpatterns = [
    path("", dashboard, name="dashboard"),
    path("", include(router.urls)),
]