
# tests/test_customer_agent.py

from agents.customer_agent import CustomerAgent

agent = CustomerAgent()

print("TEST 1: Account information")
print(agent.get_account_information("CUST001")["message"])

print("\nTEST 2: Account balance")
print(agent.check_balance("CUST001")["message"])

print("\nTEST 3: Transaction history")
print(agent.get_transaction_history("CUST001")["message"])

print("\nTEST 4: Invalid customer")
print(agent.check_balance("CUST999")["message"])