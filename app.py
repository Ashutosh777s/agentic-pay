import streamlit as st
import re
from razorpay_client import RazorpayService

st.set_page_config(
    page_title="AgenticPay | Autonomous AI Commerce",
    page_icon="⚡",
    layout="centered"
)

st.title("⚡ AgenticPay")
st.subheader("Autonomous AI Agent for Contextual Payments & Checkout")
st.caption("Built for Razorpay Buildathon | Track: AI Growth & Agentic Commerce")

# Initialize Razorpay Service
rzp = RazorpayService()

if "messages" not in st.session_state:
    st.session_state.messages = [
        {"role": "assistant", "content": "Namaste! Main AgenticPay Agent hoon. Main aapki conversational checkout me help kar sakta hoon. Aapko kya purchase karna hai?"}
    ]

# Render Chat History
for msg in st.session_state.messages:
    with st.chat_message(msg["role"]):
        st.write(msg["content"])

# User Input
if prompt := st.chat_input("Ex: Mujhe ₹8000 ka SSD purchase karna hai..."):
    st.session_state.messages.append({"role": "user", "content": prompt})
    with st.chat_message("user"):
        st.write(prompt)

    with st.chat_message("assistant"):
        with st.spinner("Processing intent and generating secure Razorpay checkout link..."):
            numbers = re.findall(r'\b\d+(?:,\d+)*(?:\.\d+)?\b', prompt)
            amount = float(numbers[0].replace(',', '')) if numbers else 500.0
            
            res = rzp.create_payment_link(
                amount_in_inr=amount,
                description=f"Agentic Order Intent: {prompt[:30]}..."
            )
            
            if res["status"] == "success":
                reply = f"Aapka request process ho gaya hai. Total amount: **₹{amount}**. Niche button par click karke instant payment complete karein:"
                st.write(reply)
                st.link_button("👉 Complete Payment via Razorpay", res["payment_url"])
            else:
                reply = f"Order ready hai (₹{amount}). Demo Razorpay Checkout Link active."
                st.write(reply)

            st.session_state.messages.append({"role": "assistant", "content": reply})
          
