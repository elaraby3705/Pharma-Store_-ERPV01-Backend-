# 🧩 Pharma Store Project Documentation

## Branch: `03-serializers`

### 🧱 Issues and Gherkin Templates

#### Issue 1: Create Product Serializer
**Description:**
Create a serializer for the Product model to define the fields shown in API responses.

```gherkin
Feature: Product Serializer
  As a developer
  I want to serialize product data
  So that I can expose clean and consistent API data

  Scenario: Serialize a valid product instance
    Given a Product model with fields name, price, and stock
    When I serialize the product instance
    Then I should see a JSON response with "name", "price", and "stock" fields
```

---

#### Issue 2: Validate Product Data
**Description:**
Add validation rules to the serializer to ensure data integrity (e.g., disallow negative prices).

```gherkin
Feature: Product Validation
  As a developer
  I want to validate product input data
  So that invalid data doesn't enter the database

  Scenario: Reject negative price values
    Given a Product serializer
    When I submit a product with a negative price
    Then I should receive a validation error with "Invalid price value"
```

---

#### Issue 3: Link Serializer to Views
**Description:**
Connect the serializer to API views so that real database data is properly serialized in API responses.

```gherkin
Feature: Integrate Product Serializer with Views
  As an API developer
  I want to connect the Product serializer to my API views
  So that my endpoints return properly serialized data

  Scenario: Return product data via API
    Given a GET request to /api/products/
    When the view uses ProductSerializer
    Then the response should include serialized product data in JSON format
```

---

## 🧾 Pull Request Template

```markdown
## 🚀 Pull Request Summary

**Branch:** `feature/03-serializers` → `develop`

### 📋 Description
Briefly describe what changes have been made in this PR:
- Added ProductSerializer
- Added validation for negative prices
- Connected serializer with views

### 🧪 Testing
Steps to test this feature:
1. Run the server
2. Access `/api/products/`
3. Verify serialized data

### 🧩 Related Issues
Closes #3, #4, #5

### ✅ Checklist
- [ ] Code runs without errors
- [ ] Unit tests added/updated
- [ ] Documentation updated
- [ ] Code reviewed by another developer

### 🧠 Notes
Any additional context or potential improvements.
```

---

## 🧭 Documentation Icons

| Icon | Meaning |
|:--|:--|
| 🧱 | Development Task |
| 🧪 | Testing / QA |
| 🚀 | Deployment |
| 🧠 | Documentation |
| 🧩 | Feature Integration |
| 🔧 | Fix / Refactor |
| 📦 | Milestone |

---

## 🗓️ Milestones Overview

| Milestone | Description | Branch | Status |
|:--|:--|:--|:--|
| 🧩 01 - Models Setup | Create and link all project models | `01-models` | ✅ Done |
| 🧩 02 - Views and URLs | Setup API views and routes | `02-views-urls` | ✅ Done |
| 🧩 03 - Serializers | Build and validate serializers | `03-serializers` | 🔄 In Progress |
| 🧩 04 - Authentication | Add user auth + permissions | `04-auth` | ⏳ Next |
| 🧩 05 - Frontend Integration | Connect API with frontend | `05-frontend` | ⏳ Planned |
| 🚀 Final - Production Release | Deploy and document | `main` | ⏳ Planned |
