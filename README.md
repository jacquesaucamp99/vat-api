# VAT API

A lightweight Django REST API and dashboard for tracking VAT transactions.

## Overview

This project stores transaction records with VAT calculations and exposes them through a REST API. It also includes a simple dashboard view for reviewing the current set of transactions in the database.

## Features

- Create, read, update, and delete transaction records through a DRF `ModelViewSet`
- Automatic VAT and gross amount calculation on create
- Validation for positive net amounts and VAT rate bounds
- Simple HTML dashboard for viewing all transactions
- Django admin integration for transaction management

## Tech Stack

- Python
- Django
- Django REST Framework
- SQLite (default development database)

## Local setup

1. Create and activate a virtual environment.
2. Install dependencies:

   ```bash
   pip install -r requirements.txt
   ```

3. Apply migrations:

   ```bash
   python manage.py migrate
   ```

4. Run the development server:

   ```bash
   python manage.py runserver
   ```

5. Open the app at:
   - Dashboard: `http://127.0.0.1:8000/`
   - API root: `http://127.0.0.1:8000/api/`

## Example API behaviour

The application uses the following `transaction` payload shape:

```json
{
  "invoice_number": "INV-1001",
  "transaction_date": "2026-09-04",
  "country": "GB",
  "currency": "GBP",
  "net_amount": "1200.00",
  "vat_rate": "0.2"
}
```

The system automatically calculates:

- `vat_amount = net_amount * vat_rate`
- `gross_amount = net_amount + vat_amount`
- `status = "Pending"`
- `created_at = transaction_date`

## Project structure

```text
vat-api/
├── config/
│   ├── __init__.py
│   ├── settings.py
│   ├── urls.py
│   ├── asgi.py
│   └── wsgi.py
├── transactions/
│   ├── admin.py
│   ├── apps.py
│   ├── migrations/
│   ├── models.py
│   ├── serializers.py
│   ├── static/
│   ├── templates/
│   ├── tests.py
│   ├── urls.py
│   └── views.py
├── manage.py
├── README.md
├── requirements.txt
└── .gitignore
```
