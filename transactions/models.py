import uuid

from django.db import models


class Transaction(models.Model):
    """Represents a VAT transaction captured by the application."""

    transaction_id = models.UUIDField(
        default=uuid.uuid4,
        editable=False,
        unique=True,
        help_text="Unique identifier for the transaction.",
    )
    invoice_number = models.CharField(max_length=50, unique=True)
    transaction_date = models.DateField()
    country = models.CharField(max_length=2)
    currency = models.CharField(max_length=3)
    net_amount = models.DecimalField(max_digits=10, decimal_places=2)
    vat_rate = models.DecimalField(max_digits=5, decimal_places=4)
    vat_amount = models.DecimalField(max_digits=10, decimal_places=2)
    gross_amount = models.DecimalField(max_digits=10, decimal_places=2)
    status = models.CharField(max_length=50)
    created_at = models.DateField(help_text="Date the transaction record was created.")

    class Meta:
        ordering = ["-transaction_date", "-created_at"]
        verbose_name = "Transaction"
        verbose_name_plural = "Transactions"

    def __str__(self):
        return f"{self.invoice_number} ({self.country})"
