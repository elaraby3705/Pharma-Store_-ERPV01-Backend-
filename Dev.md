# Pharma-ERPV2-Backend – Development Branch (`develop`)

## 📌 Branch Purpose

The `develop` branch serves as the **integration branch** for ongoing development.

* All new features are merged here first from `feature/*` branches.
* This branch mirrors the **Staging/Testing environment**.
* Code in `develop` is **not production-ready** until it passes QA and is merged into `main`.

---

## 🛠️ Tech Stack

* **Framework:** Django 4.x + Django REST Framework (DRF)
* **Database:** PostgreSQL (with indexing for optimized search)
* **Cache & Queue:** Redis
* **Containerization:** Docker + Docker Compose
* **Deployment (Staging):** Kubernetes / AWS ECS (12-Factor Compliant)
* **Testing:** Pytest / Unittest + Coverage
* **Documentation:** Swagger / OpenAPI

---

## 📂 Modular Monolith Structure

This branch follows a **4-app modular monolith** architecture:

| App Name      | Responsibility                      | Key Entities (from ERD)                                        |
| ------------- | ----------------------------------- | -------------------------------------------------------------- |
| **users**     | Authentication, Profiles, Addresses | UserProfile, Address                                           |
| **catalog**   | Product Catalog & Lookup Tables     | Product, ProductVariant, Manufacturer, ActiveIngredient        |
| **inventory** | Stock, Branches, AI Data            | Company, Branch, InventoryBatch, Prediction, InventoryMovement |
| **orders**    | Cart, Orders, Fulfillment, Reviews  | Cart, Order, Shipment, OrderItem, Review                       |

---

## ⚙️ Local Setup (for Contributors)

### 1. Prerequisites

* Install **Docker & Docker Compose**
* Install **Python 3.11+** (if running without Docker)
* Install **PostgreSQL** (if running locally without Docker)

### 2. Clone the Repository

```bash
git clone https://github.com/<owner>/Pharma-ERPV2-Backend.git
cd Pharma-ERPV2-Backend
git checkout develop
```

### 3. Environment Variables

Create a `.env` file in the project root with values like:

```
SECRET_KEY=your-secret-key
DEBUG=True
DATABASE_URL=postgres://postgres:postgres@db:5432/pharma_db
REDIS_URL=redis://redis:6379/0
```

### 4. Run Services

```bash
docker-compose up --build
```

### 5. Run Database Migrations

```bash
docker-compose exec app python manage.py migrate
```

### 6. Create Superuser

```bash
docker-compose exec app python manage.py createsuperuser
```

### 7. Run Tests

```bash
docker-compose exec app pytest --disable-warnings
```

---

## 🚀 Workflow Guidelines

1. **Feature Development**

   * Create a branch from `develop`:

     ```bash
     git checkout develop
     git pull origin develop
     git checkout -b feature/<feature-name>
     ```
   * Example: `feature/user-auth`

2. **Pull Requests (PRs)**

   * Always target `develop`.
   * Must pass **CI tests** before merging.
   * Follow commit style:

     ```
     feat(users): add JWT authentication
     fix(orders): correct order item price calculation
     docs: update setup guide for contributors
     ```

3. **Testing Requirement**

   * Unit tests required for all new models, views, and APIs.
   * Coverage target: **≥ 85%**.

4. **CI/CD Pipeline**

   * On PR merge → Deploys automatically to **Staging Environment**.
   * After QA validation → Code is merged into `main` for Production.

---

## 📖 Documentation

* **Swagger/OpenAPI:** Auto-generated API docs available at `/api/docs/` in local/staging.
* **ERD Reference:** See `/docs/ERD.md` for the full database schema.
* **Contribution Guide:** Refer to `CONTRIBUTING.md` for code standards and branching rules.

---

## ✅ Key Principles

* **12-Factor Compliant** (config via `.env`, stateless processes, Dev/Prod parity).
* **Code Modularity** (each app is independent but inside one monorepo).
* **Security First** (JWT auth, least privilege DB access, audit logs).
* **Scalability** (ready for container orchestration + horizontal scaling).

---

## 🔗 Useful Links

* [Production Branch (`main`)](../main/README.md)
* [Feature Branching Guide](./CONTRIBUTING.md)
* [API Documentation](./docs/api.md)
