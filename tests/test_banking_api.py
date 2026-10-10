
from banking.banking_api import (
    get_customer,
    get_balance,
    get_transactions,
    get_transaction_by_id,
)


def test_get_existing_customer():
    customer = get_customer("CUST001")

    assert customer is not None
    assert customer["name"] == "Arun Kumar"


def test_get_unknown_customer():
    customer = get_customer("CUST999")

    assert customer is None


def test_get_customer_balance():
    balance = get_balance("CUST001")

    assert balance == 25000.00


def test_get_transaction_history():
    transactions = get_transactions("CUST001")

    assert transactions is not None
    assert len(transactions) == 3


def test_get_existing_transaction():
    transaction = get_transaction_by_id("TXN104")

    assert transaction is not None
    assert transaction["suspicious"] is True


def test_get_unknown_transaction():
    transaction = get_transaction_by_id("TXN999")

    assert transaction is None