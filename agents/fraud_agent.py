
# agents/fraud_agent.py

from banking.banking_api import get_transaction_by_id


class FraudAgent:
    """Checks transactions for suspicious activity."""

    def check_transaction(self, transaction_id):
        transaction = get_transaction_by_id(transaction_id)

        # Check whether the transaction exists
        if transaction is None:
            return {
                "success": False,
                "risk_level": "UNKNOWN",
                "message": (
                    f"Transaction {transaction_id} was not found."
                )
            }

        # Start with a low risk score
        risk_score = 0
        reasons = []

        # Rule 1: Check the simulated fraud flag
        if transaction["suspicious"]:
            risk_score += 70
            reasons.append(
                "Transaction is flagged as suspicious in the sample data."
            )

        # Rule 2: Flag unusually large transactions
        if transaction["amount"] >= 10000:
            risk_score += 30
            reasons.append(
                "Transaction amount is unusually large (₹10,000 or more)."
            )

        # Determine the risk category
        if risk_score >= 70:
            risk_level = "HIGH"
        elif risk_score >= 30:
            risk_level = "MEDIUM"
        else:
            risk_level = "LOW"

        if not reasons:
            reasons.append("No suspicious indicators found by the demo rules.")

        return {
            "success": True,
            "transaction_id": transaction["id"],
            "description": transaction["description"],
            "amount": transaction["amount"],
            "risk_score": min(risk_score, 100),
            "risk_level": risk_level,
            "reasons": reasons,
            "message": (
                f"Transaction {transaction['id']} "
                f"has {risk_level} risk "
                f"(score: {min(risk_score, 100)}/100)."
            )
        }