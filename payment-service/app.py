from fastapi import FastAPI
from pydantic import BaseModel
import random

app = FastAPI()

class Payment(BaseModel):
    order_id: str
    amount: float

@app.post("/pay")
def pay(payment: Payment):
    status = random.choice(["approved", "declined"])
    return {
        "order_id": payment.order_id,
        "amount": payment.amount,
        "status": status
    }
