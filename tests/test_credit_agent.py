
from agents.credit_agent import CreditAgent

def test_emi_calculation():
    agent = CreditAgent()

    result = agent.calculate_emi(
        principal=200000,
        annual_interest_rate=10,
        tenure_months=36
    )

    assert result["success"] is True
    assert 6450 < result["monthly_emi"] < 6460


def test_emi_rejects_zero_principal():
    agent = CreditAgent()

    result = agent.calculate_emi(
        principal=0,
        annual_interest_rate=10,
        tenure_months=36
    )

    assert result["success"] is False


def test_loan_eligibility_for_valid_customer():
    agent = CreditAgent()

    result = agent.check_loan_eligibility(
        customer_id="CUST001",
        loan_amount=200000
    )

    assert result["success"] is True
    assert result["eligible"] is True


def test_loan_rejects_invalid_customer():
    agent = CreditAgent()

    result = agent.check_loan_eligibility(
        customer_id="CUST999",
        loan_amount=200000
    )

    assert result["success"] is False