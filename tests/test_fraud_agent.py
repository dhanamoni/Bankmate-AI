
# tests/test_fraud_agent.py

from agents.fraud_agent import FraudAgent

agent = FraudAgent()

print("TEST 1: Suspicious transaction")
result = agent.check_transaction("TXN104")
print(result["message"])
print("Reasons:", result["reasons"])

print("\nTEST 2: Normal transaction")
result = agent.check_transaction("TXN101")
print(result["message"])

print("\nTEST 3: Large transaction")
result = agent.check_transaction("TXN102")
print(result["message"])

print("\nTEST 4: Unknown transaction")
result = agent.check_transaction("TXN999")
print(result["message"])