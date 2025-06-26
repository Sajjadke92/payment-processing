# Payment Processing Microservices

This project consists of **two microservices** built with **FastAPI** that communicate with each other using REST APIs:

1. **Order Service** - Handles order creation and queries
2. **Payment Service** - Simulates payment approval

These services are containerized with Docker and deployed on AWS ECS.

---

## 🛠 Tech Stack

- Python (FastAPI)
- Docker
- AWS ECS (Fargate)
- Cloud9 (Development)
- ECR (Container Registry)

---

## 📦 Microservices Overview

### 🛒 Order Service (`order-service`)
- Accepts order details (product, price)
- Calls Payment Service to simulate payment
- Returns order details with payment status

### 💳 Payment Service (`payment-service`)
- Accepts order ID and amount
- Randomly returns `approved` or `declined`

---

## ▶️ How to Test

### 📍 Live API Endpoint (Order Service)

```bash
POST http://<YOUR_PUBLIC_EC2_OR_LB_IP>:5000/orders
Content-Type: application/json

{
  "product": "Laptop",
  "price": 1200.99
}
