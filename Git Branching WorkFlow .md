# 🧭 Pharma ERP – Git Branching Workflow & Development Lifecycle

This document defines the **branching strategy**, **naming conventions**, and **development workflow** used in the **Pharma ERP (PharmaStore V2)** project.
The goal is to maintain a clean, collaborative, and production-ready workflow from **local development → Docker → Cloud → Kubernetes → CI/CD.**

---

## 🔰 Main Branches

| Branch    | Description                                                       | Deployment Environment |
| :-------- | :---------------------------------------------------------------- | :--------------------- |
| `main`    | Stable production code only. All releases are tagged from here.   | **Production**         |
| `staging` | Pre-production testing and QA branch.                             | **Staging Server**     |
| `dev`     | Active development branch. All feature branches merge here first. | **Local / Dev Server** |

---

## 🧱 Development Phases & Feature Branches

Each feature or milestone will be developed under a **separate branch**, merged into `dev` after review, and then into `staging` → `main`.

| Phase | Branch Name                 | Description                                                                   |
| :---- | :-------------------------- | :---------------------------------------------------------------------------- |
| 01    | `01_project_setup`          | Initialize Django project, settings, environment variables, and dependencies. |
| 02    | `02_models_erd`             | Implement all 21 models as defined in the Enhanced ERD Blueprint.             |
| 03    | `03_serializers_api`        | Add Django REST Framework serializers for all models.                         |
| 04    | `04_views_endpoints`        | Create API views and viewsets for CRUD operations and business logic.         |
| 05    | `05_urls_routing`           | Configure API URLs, routers, and Swagger documentation.                       |
| 06    | `06_tests_unit_integration` | Add unit, integration, and API endpoint tests.                                |

---

## 🐳 Containerization & Local Deployment

| Phase | Branch Name                      | Description                                                        |
| :---- | :------------------------------- | :----------------------------------------------------------------- |
| 07    | `07_docker_local_setup`          | Build Dockerfile and docker-compose for local development.         |
| 08    | `08_database_docker_integration` | Integrate PostgreSQL (or MySQL) in Docker with persistent volumes. |

---

## ☁️ Cloud Setup & Deployment

| Phase | Branch Name              | Description                                                      |
| :---- | :----------------------- | :--------------------------------------------------------------- |
| 09    | `09_cloud_vm_setup`      | Configure VM instance on Google Cloud, DigitalOcean, or AWS EC2. |
| 10    | `10_docker_cloud_deploy` | Deploy Docker containers on the cloud server manually.           |

---

## 🌐 Web Server & Production Layer

| Phase | Branch Name               | Description                                                |
| :---- | :------------------------ | :--------------------------------------------------------- |
| 11    | `11_nginx_gunicorn_setup` | Configure Nginx and Gunicorn for production serving.       |
| 12    | `12_https_ssl_security`   | Enable HTTPS via Let’s Encrypt and apply security headers. |

---

## ☸️ Kubernetes & Scaling

| Phase | Branch Name                   | Description                                                                    |
| :---- | :---------------------------- | :----------------------------------------------------------------------------- |
| 13    | `13_dockerhub_registry`       | Push Docker images to DockerHub or GHCR.                                       |
| 14    | `14_kubernetes_cluster_setup` | Setup Kubernetes cluster (GKE, EKS, or DOKS).                                  |
| 15    | `15_kubernetes_deploy`        | Deploy Pharma ERP stack using YAML manifests (Deployments, Services, Ingress). |

---

## 🔄 CI/CD & Monitoring

| Phase | Branch Name               | Description                                                 |
| :---- | :------------------------ | :---------------------------------------------------------- |
| 16    | `16_jenkins_pipeline`     | Create CI/CD pipelines with Jenkins or GitHub Actions.      |
| 17    | `17_monitoring_logging`   | Integrate centralized logging (ELK / Prometheus / Grafana). |
| 18    | `18_optimization_scaling` | Optimize resources, autoscaling, and caching layers.        |

---

## 🏁 Release & Maintenance

| Branch           | Description                                                              |
| :--------------- | :----------------------------------------------------------------------- |
| `release/v1.0.0` | Official production release tag and branch.                              |
| `hotfix/*`       | Emergency bug fixes applied directly to `main` and merged back to `dev`. |

---

## 🧩 Branch Naming Convention

* Use lowercase, underscores (`_`), and two-digit prefixes for ordering.
* Example:

  * ✅ `02_models_erd`
  * ✅ `04_views_endpoints`
  * ❌ `viewsAPI` (avoid camelCase)
* All branches must be merged into `dev` through a **Pull Request (PR)** for review.

---

## ✅ Summary Workflow

```mermaid
gitGraph
   commit id: "init"
   branch dev
   commit id: "01 setup"
   branch 02_models_erd
   commit id: "models"
   checkout dev
   merge 02_models_erd
   branch 03_serializers_api
   commit id: "serializers"
   checkout dev
   merge 03_serializers_api
   checkout staging
   merge dev
   checkout main
   merge staging
```

---

## 📘 Notes

* Always document your branch purpose in the PR description.
* Keep commits atomic (small and meaningful).
* Never push directly to `main` or `staging`.
* Tag production releases (e.g., `v1.0.0`, `v1.1.0`).

---

**Author:** Pharma ERP DevOps Team
**Version:** 1.0.0
**Last Updated:** October 2025
**License:** Hammad Elaraby 
