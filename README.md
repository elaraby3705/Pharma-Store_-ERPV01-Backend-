# Pharma ERP V01 - Modular Monolith Backend

## 📌 Overview

Pharma ERP V01 is a **Django-powered ERP system** designed for **pharmacies, suppliers, and healthcare distributors**.
It combines **inventory management, e-commerce workflows, and predictive analytics** into a unified **Modular Monolith** architecture, following **12-Factor App principles** for scalability and maintainability.

The project is structured for **collaborative development** and welcomes external contributions.

---

## 🚀 Key Features

* **User & Role Management**
  Authentication, user profiles, geolocation, and company/branch structures.

* **Catalog & Products**
  Manufacturers, active ingredients, dosage forms, product variants, and detailed drug formulations.

* **Inventory Management**
  Batch-level tracking, expiry monitoring (FEFO/FIFO), supplier relationships, and real-time stock movements.

* **E-commerce & Orders**
  Shopping cart, checkout, order lifecycle, fulfillment, and delivery tracking.

* **AI-Powered Predictions**
  Demand forecasting per branch & product variant.

* **Audit & Security**
  System-wide logging of CRUD operations and sensitive changes.

---

## 🏗️ System Architecture

The system is built as a **Modular Monolith** with 4 core Django applications:

| App           | Responsibility                       | Key Models                                                     |
| ------------- | ------------------------------------ | -------------------------------------------------------------- |
| **users**     | Authentication, profiles, addresses  | UserProfile, Address                                           |
| **catalog**   | Product dictionary, lookups, search  | Product, ProductVariant, Manufacturer, ActiveIngredient        |
| **inventory** | Stock management, pricing, AI data   | Company, Branch, InventoryBatch, Prediction, InventoryMovement |
| **orders**    | Cart, checkout, fulfillment, reviews | Cart, Order, Shipment, OrderItem, Review                       |

---

## 📊 ERD (Enhanced Blueprint)

The database schema is normalized across **21 entities** including:

* **Users & Organizations:** User, Profile, Company, Branch
* **Catalog:** Manufacturer, Product, Variant, Ingredients
* **Inventory:** Batches, Movements, Predictions
* **Transactions:** Orders, OrderItems, Cart, Shipment
* **Audit & Feedback:** AuditLog, Review

---

## 🛠️ Tech Stack

* **Backend:** Django 5.x (Python 3.12+)
* **Database:** PostgreSQL (recommended) / MySQL
* **Containerization:** Docker & Docker Compose
* **Documentation:** Swagger / drf-spectacular
* **Testing:** Pytest & Django Test Framework
* **CI/CD:** GitHub Actions (planned)

---

## ⚙️ Project Setup

### 1. Clone Repository

```bash
git clone https://github.com/<your-username>/pharma-erp-v2.git
cd pharma-erp-v2
```

### 2. Setup Environment

```bash
cp .env.example .env
```

Update DB credentials, secret keys, and debug options.

### 3. Build & Run (Dockerized)

```bash
docker-compose up --build
```

The app will be available at `http://localhost:8000/`.

### 4. Run Migrations & Superuser

```bash
docker-compose exec web python manage.py migrate
docker-compose exec web python manage.py createsuperuser
```

### 5. API Documentation

* Swagger/OpenAPI available at:
  `http://localhost:8000/api/schema/swagger-ui/`

---

## 📂 Codebase Structure

```
pharma-erp-v2/
│── users/         # User profiles, addresses
│── catalog/       # Product catalog, variants, lookups
│── inventory/     # Stock, branches, movements
│── orders/        # Cart, orders, shipping, reviews
│── core/          # Shared settings, utils
│── docs/          # API & ERD documentation
│── docker/        # Docker & deployment configs
│── manage.py
│── requirements.txt
│── docker-compose.yml
│── Dockerfile
```

---

## 🔐 12-Factor Compliance Highlights

* **Codebase:** Modular Monolith, single repo
* **Dependencies:** Managed via `pip` + `requirements.txt`
* **Config:** `.env` environment variables
* **Backing Services:** Database, Redis (future), Storage
* **Build/Release/Run:** Docker Compose workflows
* **Processes:** Stateless Django workers
* **Logs:** Standardized logging to stdout/stderr
* **Concurrency:** Gunicorn/ASGI workers for scaling
* **Disposability:** Quick startup/shutdown via Docker
* **Dev/Prod Parity:** Docker ensures reproducibility

---

## 👥 Contribution Guidelines

We welcome external contributions!

1. **Fork** the repo
2. **Create a branch**:

   ```bash
   git checkout -b feature/your-feature-name
   ```
3. **Commit changes** with clear messages
4. **Push** to your fork
5. **Submit a Pull Request**

### Code Style

* Follow **PEP8** and **Django best practices**
* Ensure tests pass before submitting PR
* Use descriptive commit messages

---

## 🛣️ Roadmap

* [x] Enhanced ERD Blueprint (21 Models)
* [ ] Implement Users & Catalog Apps
* [ ] Inventory Management with FEFO
* [ ] Orders & Fulfillment APIs
* [ ] AI Forecasting Module
* [ ] CI/CD with GitHub Actions
* [ ] Deployment to Cloud (AWS/GCP)

---

## 📜 License

This project is licensed under the ** Dev License** – feel free to use and extend with attribution.

---

## 🙌 Acknowledgments

* Inspired by **real-world pharmacy workflows**
* Designed for **scalability and collaboration**
* Built with 💙 by contributors around the world
