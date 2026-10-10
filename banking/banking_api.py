
# banking/banking_api.py

# Simulated customer database
CUSTOMERS = {
    "CUST001": {
        "name": "Arun Kumar",
        "account_number": "XXXX1234",
        "balance": 25000.00,
        "monthly_income": 45000.00,
        "credit_score": 750,
        "existing_monthly_emi": 5000.00
    },
    "CUST002": {
        "name": "Priya Sharma",
        "account_number": "XXXX5678",
        "balance": 8000.00,
        "monthly_income": 25000.00,
        "credit_score": 620,
        "existing_monthly_emi": 3000.00
    }
}

# Simulated transaction database
TRANSACTIONS = {
    "CUST001": [
        {
            "id": "TXN101",
            "description": "Grocery Store",
            "amount": 1200.00,
            "type": "debit",
            "status": "completed",
            "suspicious": False
        },
        {
            "id": "TXN102",
            "description": "Salary Credit",
            "amount": 45000.00,
            "type": "credit",
            "status": "completed",
            "suspicious": False
        },
        {
            "id": "TXN104",
            "description": "Unknown Online Payment",
            "amount": 18000.00,
            "type": "debit",
            "status": "flagged",
            "suspicious": True
        }
    ],
    "CUST002": [
        {
            "id": "TXN201",
            "description": "Electricity Bill",
            "amount": 1500.00,
            "type": "debit",
            "status": "completed",
            "suspicious": False
        },
        {
            "id": "TXN202",
            "description": "Online Shopping",
            "amount": 2500.00,
            "type": "debit",
            "status": "completed",
            "suspicious": False
        }
    ]
}


def get_customer(customer_id):
    """Return customer details for a valid customer ID."""
    return CUSTOMERS.get(customer_id)


def get_balance(customer_id):
    """Return the customer's account balance."""
    customer = get_customer(customer_id)

    if customer is None:
        return None

    return customer["balance"]


def get_transactions(customer_id):
    """Return the customer's transaction history."""
    return TRANSACTIONS.get(customer_id)


def get_transaction_by_id(transaction_id):
    """Find a transaction using its transaction ID."""
    for customer_transactions in TRANSACTIONS.values():
        for transaction in customer_transactions:
            if transaction["id"] == transaction_id:
                return transaction

    return None