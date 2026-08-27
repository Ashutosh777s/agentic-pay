import streamlit as st
import re
from razorpay_client import RazorpayService

st.set_page_config(page_title="AgenticPay", layout="centered")

st.title("AgenticPay")
st.caption("Contextual Payments Engine - Razorpay Buildathon 2026")

# Initialize SDK wrapper
rzp_service = RazorpayService()

def parse_amount(user_text):
    # Regex to grab numerical pricing from prompt
    match = re.search(r'\b\d+(?:,\d+)*(?:\.\d+)?\b', user_text)
    if match:
        clean_num = match.group().replace(',', '')
        return float(clean_num)
    return 500.0  # Fallback default value

# State management for chat
if "chat_history" not in st.session_state:
    st.session_state.chat_history = [
        {
            "role": "assistant",
            "content": "Hello! Enter your purchase details below to generate a direct checkout link."
        }
    ]

# Render current chat sequence
for message in st.session_state.chat_history:
    with st.chat_message(message["role"]):
        st.write(message["content"])

# User prompt execution
user_input = st.chat_input("E.g., Order wireless earbuds for 1800...")

if user_input:
    st.session_state.chat_history.append({"role": "user", "content": user_input})
    with st.chat_message("user"):
        st.write(user_input)

    with st.chat_message("assistant"):
        with st.spinner("Processing purchase intent..."):
            extracted_price = parse_amount(user_input)
            item_summary = f"Agentic Checkout: {user_input[:30]}"

            res = rzp_service.create_payment_link(
                amount=extracted_price,
                description=item_summary
            )

            if res.get("success"):
                checkout_url = res.get("url")
                response_text = f"Payment link generated for INR {extracted_price:.2f}."
                st.write(response_text)
                st.link_button("Complete Payment via Razorpay", checkout_url)
            else:
                response_text = f"Could not create live link for INR {extracted_price:.2f}. Check API key configuration."
                st.write(response_text)

            st.session_state.chat_history.append({
                "role": "assistant",
                "content": response_text
            })
