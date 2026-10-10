
from agents.llm_agent import LLMAgent

agent = LLMAgent()

questions = [
    "How much money is in my account?",
    "Show my recent payments",
    "Is transaction TXN104 suspicious?",
    "Can I borrow 2 lakh?",
    "Calculate my EMI for 2 lakh",
    "Tell me a joke"
]

for question in questions:
    intent = agent.classify_request(question)
    print(f"Question: {question}")
    print(f"Detected intent: {intent}")
    print("-" * 40)