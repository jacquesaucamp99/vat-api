"""Serializers for VAT transaction data."""

from rest_framework import serializers

from .models import Transaction


class TransactionSerializer(serializers.ModelSerializer):
    """Validate and serialize transaction payloads for the API."""

    class Meta:
        model = Transaction
        fields = [
            "transaction_id",
            "invoice_number",
            "transaction_date",
            "country",
            "currency",
            "net_amount",
            "vat_rate",
            "vat_amount",
            "gross_amount",
            "status",
            "created_at",
        ]
        read_only_fields = [
            "transaction_id",
            "vat_amount",
            "gross_amount",
            "status",
            "created_at",
        ]

    def validate_net_amount(self, value):
        """Ensure the net amount is positive before saving."""
        if value <= 0:
            raise serializers.ValidationError("Net amount must be greater than zero.")
        return value

    def validate_vat_rate(self, value):
        """Allow only rates between 0 and 1, matching a decimal percentage."""
        if value < 0 or value > 1:
            raise serializers.ValidationError("VAT rate must be between 0 and 1.")
        return value
