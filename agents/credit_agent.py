
# agents/credit_agent.py

from banking.banking_api import get_customer


class CreditAgent:
    """Handles simulated loan eligibility and EMI calculations."""

    def check_loan_eligibility(self, customer_id, loan_amount):
        customer = get_customer(customer_id)

        if customer is None:
            return {
                "success": False,
                "message": "Customer account not found."
            }

        if loan_amount <= 0:
            return {
                "success": False,
                "message": "Loan amount must be greater than zero."
            }

        monthly_income = customer["monthly_income"]
        credit_score = customer["credit_score"]
        existing_emi = customer["existing_monthly_emi"]

        # Simple demonstration affordability rule:
        # Total monthly EMI should not exceed 40% of income.
        max_total_emi = monthly_income * 0.40
        available_emi = max_total_emi - existing_emi

        reasons = []

        if credit_score < 650:
            reasons.append("Credit score is below the demo threshold of 650.")

        if available_emi <= 0:
            reasons.append(
                "Existing monthly EMI leaves no capacity under the demo rule."
            )

        if loan_amount > 500000:
            reasons.append(
                "Requested loan exceeds the demo limit of ₹5,00,000."
            )

        eligible = (
            credit_score >= 650
            and available_emi > 0
            and loan_amount <= 500000
        )

        if eligible:
            message = (
                f"{customer['name']} meets the basic demo eligibility rules "
                f"for a ₹{loan_amount:,.2f} loan. "
                f"Estimated available monthly EMI capacity: "
                f"₹{available_emi:,.2f}."
            )
        else:
            message = (
                f"{customer['name']} does not meet all the demo eligibility "
                f"rules for a ₹{loan_amount:,.2f} loan."
            )

        return {
            "success": True,
            "eligible": eligible,
            "customer_id": customer_id,
            "loan_amount": loan_amount,
            "credit_score": credit_score,
            "monthly_income": monthly_income,
            "available_monthly_emi": max(0, available_emi),
            "reasons": reasons,
            "message": message
        }

    def calculate_emi(self, principal, annual_interest_rate, tenure_months):
        if principal <= 0:
            return {
                "success": False,
                "message": "Loan amount must be greater than zero."
            }

        if annual_interest_rate < 0:
            return {
                "success": False,
                "message": "Interest rate cannot be negative."
            }

        if tenure_months <= 0:
            return {
                "success": False,
                "message": "Tenure must be greater than zero months."
            }

        monthly_rate = annual_interest_rate / (12 * 100)

        if monthly_rate == 0:
            emi = principal / tenure_months
        else:
            factor = (1 + monthly_rate) ** tenure_months
            emi = principal * monthly_rate * factor / (factor - 1)

        total_payment = emi * tenure_months
        total_interest = total_payment - principal

        return {
            "success": True,
            "principal": principal,
            "annual_interest_rate": annual_interest_rate,
            "tenure_months": tenure_months,
            "monthly_emi": round(emi, 2),
            "total_payment": round(total_payment, 2),
            "total_interest": round(total_interest, 2),
            "message": (
                f"Estimated monthly EMI: ₹{emi:,.2f}. "
                f"Total interest: ₹{total_interest:,.2f}."
            )
        }