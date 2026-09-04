"""Admin configuration for the VAT transactions app."""

from django.contrib import admin

from .models import Transaction


@admin.register(Transaction)
class TransactionAdmin(admin.ModelAdmin):
    """Expose transaction records in the Django admin dashboard."""

    list_display = (
        "invoice_number",
        "transaction_date",
        "country",
        "currency",
        "net_amount",
        "status",
    )
    list_filter = ("country", "currency", "status")
    search_fields = ("invoice_number", "country", "currency")