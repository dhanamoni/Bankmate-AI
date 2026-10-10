
import re

from agents.customer_agent import CustomerAgent
from agents.fraud_agent import FraudAgent
from agents.credit_agent import CreditAgent
from agents.llm_agent import LLMAgent


class SupervisorAgent:
    def __init__(self):
        self.customer_agent = CustomerAgent()
        self.fraud_agent = FraudAgent()
        self.credit_agent = CreditAgent()
        self.llm_agent = LLMAgent()

    def process_request(self, question, customer_id="CUST001"):
        question = question.strip()

        if not question:
            return {
                "success": False,
                "agent": "Supervisor",
                "message": "Please enter a banking question."
            }

        # Extract an optional customer ID.
        customer_match = re.search(
            r"\bCUST\d+\b", question, re.IGNORECASE
        )
        if customer_match:
            customer_id = customer_match.group().upper()

        # Ask Groq to classify the user's intent.
        try:
            intent = self.llm_agent.classify_request(question)
        except Exception:
            # Fall back to keyword routing if the API is unavailable.
            intent = self._fallback_intent(question)

        lower_question = question.lower()

        if intent == "fraud":
            txn_match = re.search(
                r"\bTXN\d+\b", question, re.IGNORECASE
            )

            if not txn_match:
                return {
                    "success": False,
                    "agent": "Fraud Agent",
                    "message": (
                        "Please include a transaction ID, "
                        "for example TXN104."
                    )
                }

            result = self.fraud_agent.check_transaction(
                txn_match.group().upper()
            )
            result["agent"] = "Fraud Agent"
            return result

        if intent == "emi":
            # Use a clearly specified amount, or a demo default.
            amount_match = re.search(
                r"(?:₹|rs\.?\s*)?\s*"
                r"(\d[\d,]*(?:\.\d+)?)\s*"
                r"(lakh|lakhs|lac|lacs|thousand|k)?",
                lower_question
            )

            principal = 200000.0
            if amount_match:
                principal = float(
                    amount_match.group(1).replace(",", "")
                )
                unit = amount_match.group(2)
                if unit in ("lakh", "lakhs", "lac", "lacs"):
                    principal *= 100000
                elif unit in ("thousand", "k"):
                    principal *= 1000

            rate_match = re.search(
                r"(\d+(?:\.\d+)?)\s*%\s*"
                r"(?:interest|rate)?",
                lower_question
            )
            rate = float(rate_match.group(1)) if rate_match else 10.0

            tenure_match = re.search(
                r"(\d+)\s*(months?|years?)",
                lower_question
            )
            tenure = 36
            if tenure_match:
                tenure = int(tenure_match.group(1))
                if tenure_match.group(2).startswith("year"):
                    tenure *= 12

            result = self.credit_agent.calculate_emi(
                principal, rate, tenure
            )
            result["agent"] = "Credit Agent"
            return result

        if intent == "loan":
            amount_match = re.search(
                r"(?:₹|rs\.?\s*)?\s*"
                r"(\d[\d,]*(?:\.\d+)?)\s*"
                r"(lakh|lakhs|lac|lacs|thousand|k)?",
                lower_question
            )

            loan_amount = 200000.0
            if amount_match:
                loan_amount = float(
                    amount_match.group(1).replace(",", "")
                )
                unit = amount_match.group(2)
                if unit in ("lakh", "lakhs", "lac", "lacs"):
                    loan_amount *= 100000
                elif unit in ("thousand", "k"):
                    loan_amount *= 1000

            result = self.credit_agent.check_loan_eligibility(
                customer_id, loan_amount
            )
            result["agent"] = "Credit Agent"
            return result

        if intent == "transactions":
            result = self.customer_agent.get_transaction_history(
                customer_id
            )
            result["agent"] = "Customer Agent"
            return result

        if intent == "balance":
            result = self.customer_agent.get_account_information(
                customer_id
            )
            result["agent"] = "Customer Agent"
            return result

        return {
            "success": False,
            "agent": "Supervisor",
            "message": (
                "I couldn't identify a supported banking request. "
                "Try asking about your balance, transactions, "
                "fraud, loan eligibility, or EMI."
            )
        }

    @staticmethod
    def _fallback_intent(question):
        """Keyword fallback if the LLM API fails."""
        q = question.lower()

        if any(word in q for word in (
            "fraud", "suspicious", "scam", "risk"
        )):
            return "fraud"

        if any(word in q for word in (
            "emi", "installment", "monthly payment"
        )):
            return "emi"

        if any(word in q for word in (
            "loan", "eligibility", "eligible", "borrow"
        )):
            return "loan"

        if any(word in q for word in (
            "transaction", "payment history", "recent payments"
        )):
            return "transactions"

        if any(word in q for word in (
            "balance", "account details", "account information"
        )):
            return "balance"

        return "unknown"