
import streamlit as st
from agents.supervisor_agent import SupervisorAgent

st.set_page_config(
    page_title="BankMate AI",
    page_icon="🏦",
    layout="wide"
)

# Create the Supervisor Agent
if "supervisor" not in st.session_state:
    st.session_state.supervisor = SupervisorAgent()

if "chat_history" not in st.session_state:
    st.session_state.chat_history = []

st.title("🏦 BankMate AI")
st.caption("Simulated Banking Assistant | Multi-Agent Automation")

st.write(
    "Ask questions about account balances, transactions, "
    "fraud checks, loan eligibility, and EMI calculations."
)

# Sidebar settings
st.sidebar.header("Banking Dashboard")

customer_id = st.sidebar.selectbox(
    "Select sample customer",
    ["CUST001", "CUST002"]
)

st.sidebar.caption("Demo data only — no real bank accounts.")

st.sidebar.markdown("### Available agents")
st.sidebar.write("👤 Customer Agent")
st.sidebar.write("🛡️ Fraud Detection Agent")
st.sidebar.write("🏦 Credit & Loan Agent")
st.sidebar.write("🧭 Supervisor Agent")

if st.sidebar.button("Clear Chat"):
    st.session_state.chat_history = []
    st.rerun()

# Example questions
st.subheader("Try a sample question")

examples = [
    "What is my account balance?",
    "Show my transaction history",
    "Check whether TXN104 is suspicious",
    "Am I eligible for a loan of 2 lakh?",
    "Calculate EMI for 2 lakh at 10% interest for 36 months"
]

selected_example = st.selectbox(
    "Choose an example",
    ["Choose a question..."] + examples
)

# Display previous conversation
st.subheader("Banking Assistant Chat")

for item in st.session_state.chat_history:
    with st.chat_message(item["role"]):
        st.markdown(item["content"])

        if item.get("agent"):
            st.caption(f"Handled by: {item['agent']}")

# Accept a new question
question = st.chat_input("Type your banking question...")

if question:
    st.session_state.chat_history.append({
        "role": "user",
        "content": question
    })

    result = st.session_state.supervisor.process_request(
        question,
        customer_id
    )

    st.session_state.chat_history.append({
        "role": "assistant",
        "content": result["message"],
        "agent": result.get("agent", "Supervisor")
    })

    st.rerun()

# Submit the selected example
if st.button("Ask Example Question", use_container_width=True):
    if selected_example == "Choose a question...":
        st.warning("Please select an example question.")
    else:
        st.session_state.chat_history.append({
            "role": "user",
            "content": selected_example
        })

        result = st.session_state.supervisor.process_request(
            selected_example,
            customer_id
        )

        st.session_state.chat_history.append({
            "role": "assistant",
            "content": result["message"],
            "agent": result.get("agent", "Supervisor")
        })

        st.rerun()