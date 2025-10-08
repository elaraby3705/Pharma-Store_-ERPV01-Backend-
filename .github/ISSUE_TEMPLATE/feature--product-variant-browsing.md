---
name: 'Feature: Product Variant Browsing'
about: 'Public template for the Project '
title: ''
labels: ''
assignees: ''

---

As a Customer,
I want to browse a paginated list of all product variants,
So that I can quickly find the exact dosage and form I need.

@Catalog @ReadAPI @MVP

Background: 
    Given the Catalog Service is running.
    And several Product Variants (e.g., 'Panadol 500mg Tablet', 'Amoxicillin 250mg Syrup') exist in the database.

Scenario: Successful Paginated Product Listing
    When a GET request is sent to the '/api/v1/catalog/variants/' endpoint.
    Then the system returns a status code of 200 (OK).
    And the response body should be a paginated list containing 10 Product Variants.
    And each item should display its 'product_name', 'dosage_form_name', and 'pack_size'.

Scenario: Retrieving a Single Variant Detail
    Given the Product Variant with ID 42 exists.
    When a GET request is sent to the '/api/v1/catalog/variants/42/' endpoint.
    Then the system returns a status code of 200 (OK).
    And the response displays the unique 'barcode_gtin' for Variant 42.

### Technical Requirements (for Pull Request)
* **Target App:** `catalog`
* **New Files:** `catalog/views.py`, `catalog/urls.py`
* **Middleware:** Must be accessible by Anonymous User (no authentication required).

Sources and related content
