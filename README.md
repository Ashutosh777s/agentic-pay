# AgenticPay: Autonomous AI Agent for Contextual Payments

> Submission for Razorpay Buildathon | Track: AI Growth & Agentic Commerce

AgenticPay is an AI-driven agent prototype designed to streamline conversational commerce. By parsing user intent directly within a chat interface, it dynamically interacts with Razorpay APIs to generate instant, friction-free payment links.

## System Architecture

1. **Intent Processing:** Extracts numerical values and contextual purchasing parameters from user prompt.
2. **Dynamic Order Creation:** Constructs API payload and communicates with Razorpay Payment Links API.
3. **Checkout Execution:** Serves an inline payment action without requiring multi-step checkout forms.

## Tech Stack

- Python 3.10+
- Streamlit Framework
- Razorpay Python SDK

## Setup & Running Locally

1. Clone the repository:
   ```bash
   git clone [https://github.com/YOUR_USERNAME/agentic-pay.git](https://github.com/YOUR_USERNAME/agentic-pay.git)
   cd agentic-pay
   
