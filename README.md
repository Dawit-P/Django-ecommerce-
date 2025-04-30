# Django E-Commerce Management System

This is a Django-based e-commerce management system developed for a coding challenge.  
It models Products, Purchase Orders, and Customer Invoices, with Django Admin customization, advanced ORM usage, and XLSX export functionality.

## Features

- Product management (name, SKU, unit price).
- Purchase Orders with line items linking products and quantities.
- Customer Invoices with line items.
- Inline editing of line items in Django Admin.
- Custom calculated totals in list view.
- Admin action to mark invoices as paid.
- Highlighting overdue invoices.
- Export invoices to XLSX format.
- Advanced ORM queries using annotations and conditional filters.

## Installation

1. Clone the repository:
    ```bash
    git clone https://github.com/Dawit-P/Django-ecommerce-.git
    cd django-ecommerce
    ```

2. Create and activate a virtual environment:
    ```bash
    python -m venv env
    source env/bin/activate  # On Windows: env\Scripts\activate
    ```

3. Install dependencies:
    ```bash
    pip install -r requirements.txt
    ```

4. Apply migrations:
    ```bash
    python manage.py migrate
    ```

5. Create a superuser:
    ```bash
    python manage.py createsuperuser
    ```

6. Run the server:
    ```bash
    python manage.py runserver
    ```

## Usage

- Login to the Django Admin panel.
- Manage Products, Purchase Orders, and Invoices.
- Edit line items directly in the parent object page.
- Use the custom admin actions to mark invoices as paid.
- Export selected invoices to XLSX.
- Overdue invoices are highlighted in red.
