"""Views for the VAT transaction API and dashboard."""

from django.shortcuts import render
from rest_framework import permissions, viewsets

from .models import Transaction
from .serializers import TransactionSerializer


class TransactionViewSet(viewsets.ModelViewSet):
    """Provide CRUD access to transaction records via the REST API."""

    queryset = Transaction.objects.all()
    serializer_class = TransactionSerializer
    permission_classes = [permissions.AllowAny]

    def perform_create(self, serializer):
        """Populate calculated VAT summary fields before persisting a new record."""
        net_amount = serializer.validated_data.get("net_amount")
        vat_rate = serializer.validated_data.get("vat_rate")
        vat_amount = net_amount * vat_rate
        gross_amount = net_amount + vat_amount
        created_date = serializer.validated_data.get("transaction_date")

        serializer.save(
            status="Pending",
            vat_amount=vat_amount,
            gross_amount=gross_amount,
            created_at=created_date,
        )


def dashboard(request):
    """Render the dashboard with all stored transactions for review."""
    transactions = Transaction.objects.all()
    return render(request, "transactions/dashboard.html", {"transactions": transactions})