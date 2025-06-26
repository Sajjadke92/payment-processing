from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
import requests


app = FastAPI()

orders = {}
order_counter = 1

# Use container/service name in Docker, replace with real URL in deployment
PAYMENT_SERVICE_URL = "http://54.81.163.88:5001/pay"

class Order(BaseModel):
    product: str
    price: float

@app.post("/orders")
def create_order(order: Order):
    global order_counter 
    order_id = str(order_counter)
    order_counter += 1
    try:
        res = requests.post(PAYMENT_SERVICE_URL, json={
            "order_id": order_id,
            "amount": order.price
        })
        if res.status_code != 200:
            raise HTTPException(status_code=500, detail="Payment failed")
        payment = res.json()
    except:
        raise HTTPException(status_code=500, detail="Payment service error 2")

    orders[order_id] = {
        "order_id": order_id,
        "product": order.product,
        "price": order.price,
        "payment_status": payment["status"]
    }

    return orders[order_id]

@app.get("/orders/{order_id}")
def get_order(order_id: str):
    if order_id not in orders:
        raise HTTPException(status_code=404, detail="Order not found")
    return orders[order_id]