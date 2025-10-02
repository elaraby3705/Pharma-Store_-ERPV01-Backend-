# Pharma-Store_-ERPV01-Backend-
 - Production Environment

## Overview
This repository contains the Backend API for the digital pharmacy platform (Pharma ERD v2), built using **Django** and **Django REST Framework**. This branch (`main`) holds the stable code ready for deployment to **Production**.

## Key Features
- Secure Authentication System (JWT).
- Detailed Product Catalog Management.
- Batch-Level Inventory Tracking (Expiry Dates).
- AI Prediction Pipeline integration readiness.

## Setup and Deployment (12-Factor Compliant)
**12-Factor App Implementation:** Deployment uses **Docker** and **Kubernetes/AWS ECS** to ensure scalability and stateless operations (Factor VIII, VI).

1.  **Environment Variables (Config):** All sensitive configurations (e.g., `DATABASE_URL`, `SECRET_KEY`) must be supplied via `.env` files or directly into the deployment environment (Factor III).
2.  **Build:** Build the Docker image from the provided `Dockerfile`.
    ```bash
    docker build -t pharma-backend:latest .
    ```
3.  **Run:** Start the image, linked to all Backing Services (PostgreSQL, Redis).
    ```bash
    # Example run command in a production-like environment
    docker run -d --env-file .env pharma-backend
    ```
## Documentation
- **API Docs:** [Link to Swagger/OpenAPI documentation here]
- **ERD:** [Link to ERD Diagram here]
