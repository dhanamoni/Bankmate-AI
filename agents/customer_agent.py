
# agents/customer_agent.py

from banking.banking_api import (
    get_customer,
    get_balance,
    get_transactions
)


class CustomerAgent:
    """Handles customer account and transaction queries."""

    def get_account_information(self, customer_id):
        customer = get_customer(customer_id)

        if customer is None:
            return {
                "success": False,
                "message": "Customer account not found."
            }

        return {
            "success": True,
            "message": (
                f"Account holder: {customer['name']}\n"
                f"Account number: {customer['account_number']}\n"
                f"Account balance: ₹{customer['balance']:,.2f}"
            ),
            "data": customer
        }

    def check_balance(self, customer_id):
        balance = get_balance(customer_id)

        if balance is None:
            return {
                "success": False,
                "message": "Unable to find the customer's balance."
            }

        return {
            "success": True,
            "message": f"Your current balance is ₹{balance:,.2f}."
        }

    def get_transaction_history(self, customer_id):
        transactions = get_transactions(customer_id)

        if transactions is None:
            return {
                "success": False,
                "message": "Customer account not found."
            }

        if not transactions:
            return {
                "success": True,
                "message": "No transactions found.",
                "data": []
            }

        lines = []

        for transaction in transactions:
            line = (
                f"{transaction['id']} | "
                f"{transaction['description']} | "
                f"{transaction['type'].upper()} | "
                f"₹{transaction['amount']:,.2f} | "
                f"{transaction['status']}"
            )
            lines.append(line)

        return {
            "success": True,
            "message": "\n".join(lines),
            "data": transactions
        }