# Pharma-Store_-ERPV01-Backend-
 - Production Environment


  # Pharma-ERPV2-Backend - Development Environment

## Purpose
This branch serves as the primary integration hub for all new features before they are validated and promoted to the `main` (Production) branch. The code here reflects the latest complete and tested features.

## Key Project Documentation
For comprehensive understanding of the project structure and vision, refer to these foundational documents:

1.  **Full ERD Blueprint:** Defines all 21 core tables and their relationships, ensuring data integrity across the Catalog, Inventory, and Orders domains.
2.  **Dual Data Flow Pipeline:** Outlines the core system architecture, separating the **Transactional Flow** (focusing on speed and order processing) from the **Analytical/AI Flow** (focusing on strategic insights and forecasting).

## Local Setup (For Developers)

The following steps enforce **Dev/Prod Parity (Factor X)** and **Configuration Isolation (Factor III)**:

1.  **Prerequisites:** Install Docker and Docker Compose.
2.  **Configuration (Factor III):** Create a local `.env` file at the project root. This file must hold all secret settings and backing service URLs (e.g., `POSTGRES_DB`, `SECRET_KEY`), ensuring no sensitive data is committed to Git.
3.  **Clone:** Clone the repository and source the local `.env` file.
4.  **Run Services:** Start all required services (Application, PostgreSQL database, and Redis cache).
    ```bash
    docker-compose up --build
    ```
5.  **Run Migrations:**
    ```bash
    docker-compose exec app python manage.py migrate
    ```
6.  **Create Superuser:**
    ```bash
    docker-compose exec app python manage.py createsuperuser
    ```

## Architectural Roadmap: Monolith to Microservices (Explained)

### Rationale for the Modular Monolith:
We start with a Modular Monolith **not as the final form**, but as a strategic initial step to achieve **faster Time-to-Market (MVP)** and reduce the initial operational complexity associated with managing distributed services. **Crucially, the app separation (Catalog, Inventory, Orders) establishes the clean domain boundaries required for Factor I (Codebase) and future decoupling.**

### Transition Plan:
Each isolated Django App serves as the definitive **Blueprint** for a future independent Microservice, adhering to the Strangler Fig Pattern:

1.  **Phase 1 (Current): Modular Monolith:** All services run in one Django project, sharing a single database.
2.  **Phase 2 (Scaling): Microservices Decoupling:** When required by scale, services will be isolated incrementally:
    * The code for a service (e.g., **Inventory**) is moved to its own repository and deployment environment.
    * It is assigned its **own dedicated database** (enforcing Factor IV).
    * Communication switches from internal Python function calls to external **API calls and Asynchronous Message Broker events**.

**Goal:** To build a robust foundation today that scales horizontally tomorrow without a complete rewrite.

## Workflow
- All Pull Requests (PRs) must target the `develop` branch.
- Every PR must be accompanied by successful unit tests.
