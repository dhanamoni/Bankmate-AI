# BankMate AI — Multi-Agent Banking Assistant

## Overview

BankMate AI is a simulated banking assistant built with Python and Streamlit. It uses a Large Language Model (LLM) through the Groq API to classify natural-language banking requests and route them to specialized agents.

The project demonstrates multi-agent orchestration, simulated banking APIs, fraud-risk rules, loan eligibility checks, and EMI calculations.

**Disclaimer:** This is an educational MVP using sample data. It is not connected to real banking systems and must not be used for real financial decisions.

## Key Features

* **Supervisor Agent:** Coordinates incoming requests and selects a suitable specialist.
* **LLM Agent:** Uses Groq to classify user intent.
* **Customer Agent:** Retrieves simulated account information, balances, and transaction history.
* **Fraud Agent:** Assigns a demo risk score using predefined rules.
* **Credit Agent:** Evaluates basic demo loan eligibility and calculates monthly EMI.
* **Streamlit UI:** Provides an interactive banking chat interface.

## Supported Use Cases

1. **Account balance:** Retrieve a sample customer's account information.
2. **Transaction history:** View simulated transactions.
3. **Fraud detection:** Check a transaction ID for suspicious indicators.
4. **Loan eligibility:** Apply predefined credit-score, income-capacity, and loan-limit rules.
5. **EMI calculation:** Estimate monthly instalments, total repayment, and interest.

## Technology Stack

* Python
* Streamlit
* Groq API
* `groq` Python SDK
* `python-dotenv`
* pytest

## Architecture

```text
User
 |
 v
Streamlit UI
 |
 v
Supervisor Agent
 |
 v
LLM Agent (Groq)
 |
 v
Intent Classification
 |
 +---- Customer Agent
 |       |
 |       v
 |   Simulated Banking API
 |
 +---- Fraud Agent
 |       |
 |       v
 |   Rule-Based Risk Scoring
 |
 +---- Credit Agent
         |
         v
     Loan Eligibility / EMI
```

The LLM classifies the request. Deterministic Python functions handle sample banking data, fraud rules, and financial calculations.

If the LLM API fails, the Supervisor can attempt keyword-based intent routing.

## Project Structure

```text
Bankmate-AI/
├── agents/
│   ├── customer_agent.py
│   ├── fraud_agent.py
│   ├── credit_agent.py
│   ├── supervisor_agent.py
│   └── llm_agent.py
├── banking/
│   └── banking_api.py
├── tests/
│   ├── test_banking_api.py
│   ├── test_credit_agent.py
│   ├── test_customer_agent.py
│   ├── test_llm_agent.py
│   └── test_supervisor_agent.py
├── app.py
├── test_groq.py
├── .env
├── .gitignore
└── README.md
```

## Setup Instructions

### 1. Create and activate a virtual environment

```powershell
python -m venv .venv
.\.venv\Scripts\Activate.ps1
```

### 2. Install dependencies

```powershell
python -m pip install streamlit groq python-dotenv pytest
```

### 3. Configure the API key

Create a `.env` file in the project root:

```text
GROQ_API_KEY=your_groq_api_key
```

Obtain an API key from the Groq Console. Never publish your actual API key.

### 4. Run the application

```powershell
python -m streamlit run app.py
```

### 5. Run automated tests

```powershell
python -m pytest -v
```

Tests that make live API calls require a valid key and may consume API quota.

## Sample Questions

* What is my account balance?
* Show my transaction history.
* Is transaction TXN104 suspicious?
* Am I eligible for a loan of 2 lakh?
* Calculate EMI for 2 lakh at 10% interest for 36 months.

Sample customer IDs: `CUST001` and `CUST002`.

## EMI Calculation

For a loan with principal \(P\), monthly interest rate \(r\), and tenure \(n\) months, the EMI is calculated using:

$$
EMI = \frac{P r(1+r)^n}{(1+r)^n-1}
$$

For zero interest, EMI is the principal divided by the number of months.

## Fraud Detection

The demo fraud agent uses predefined indicators, such as suspicious flags and unusually large transactions, to calculate a risk score. This is a rule-based demonstration, not a production fraud detection model.

## Limitations and Future Improvements

* Replace sample banking data with secure, authorized integrations.
* Add authentication, authorization, and audit logging.
* Improve validation of natural-language amounts and loan tenures.
* Add more comprehensive unit and integration tests.
* Add structured logging and better API error handling.
* Evaluate false positives and false negatives in fraud detection.
* Separate live LLM tests from offline automated tests.

## Demo Plan

1. Launch the Streamlit application.
2. Ask for an account balance.
3. Display transaction history.
4. Check suspicious transaction `TXN104`.
5. Check demo loan eligibility.
6. Calculate EMI for a sample loan.
7. Explain the Supervisor's routing and the roles of the three specialist agents.
8. Show automated test results.

## Security Notice

This project is for educational demonstration only. It uses simulated customer records and does not authenticate users. Do not enter real banking credentials or sensitive financial information.
