import os
import razorpay

class RazorpayService:
    """
    Production-grade Wrapper for Razorpay Payment Links API.
    Handles dynamic order creation and payment link generation for Agentic Commerce.
    """
    def __init__(self, key_id: str = None, key_secret: str = None):
        self.key_id = key_id or os.getenv("RAZORPAY_KEY_ID", "rzp_test_demo")
        self.key_secret = key_secret or os.getenv("RAZORPAY_KEY_SECRET", "demo_secret")
        self.client = razorpay.Client(auth=(self.key_id, self.key_secret))

    def create_payment_link(self, amount_in_inr: float, description: str, customer_name: str = "Valued Customer") -> dict:
        try:
            payload = {
                "amount": int(amount_in_inr * 100),  # Convert to paise
                "currency": "INR",
                "accept_partial": False,
                "description": description,
                "customer": {
                    "name": customer_name,
                    "email": "customer@agenticpay.io",
                    "contact": "+919999999999"
                },
                "notify": {"sms": False, "email": False},
                "reminder_enable": True,
                "notes": {"source": "AgenticPay Automated Checkout"}
            }
            response = self.client.payment_link.create(payload)
            return {
                "status": "success",
                "payment_url": response.get("short_url"),
                "id": response.get("id")
            }
        except Exception as err:
            return {"status": "error", "message": str(err)}
          
