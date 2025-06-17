from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
import requests
import uuid

app = FastAPI()

orders = {}

# IMPORTANT: We'll change this URL when we run both services together
PAYMENT_SERVICE_URL = "http://payment-service:5001/pay"

class OrderRequest(BaseModel):
    product: str
    price: float

@app.post("/orders")
def create_order(order: OrderRequest):
    order_id = str(uuid.uuid4())
    
    try:
        response = requests.post(PAYMENT_SERVICE_URL, json={
            "order_id": order_id,
            "amount": order.price
        })
        payment_data = response.json()
    except Exception:
        raise HTTPException(status_code=500, detail="Payment service not reachable")

    orders[order_id] = {
        "order_id": order_id,
        "product": order.product,
        "price": order.price,
        "payment_status": payment_data.get("status")
    }

    return orders[order_id]

@app.get("/orders/{order_id}")
def get_order(order_id: str):
    if order_id not in orders:
        raise HTTPException(status_code=404, detail="Order not found")
    return orders[order_id]
