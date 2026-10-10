
from agents.supervisor_agent import SupervisorAgent

supervisor = SupervisorAgent()

questions = [
    "What is my account balance?",
    "Show my transaction history",
    "Check whether TXN104 is suspicious",
    "Am I eligible for a loan of 2 lakh?",
    "Calculate EMI for 2 lakh at 10% interest for 36 months",
    "Tell me a joke"
]

for question in questions:
    print("\nQuestion:", question)

    result = supervisor.process_request(question)

    print("Selected agent:", result["agent"])
    print("Response:", result["message"])