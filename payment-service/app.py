from fastapi import FastAPI
from pydantic import BaseModel
import random

app = FastAPI()

class PaymentRequest(BaseModel):
    order_id: str
    amount: float

@app.post("/pay")
def process_payment(payment: PaymentRequest):
    # Simulate a random approval
    status = random.choice(["approved", "declined"])
    
    return {
        "order_id": payment.order_id,
        "amount": payment.amount,
        "status": status
    }
