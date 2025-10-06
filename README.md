🛒 Order Management System (Django REST API)

A simple yet powerful Order Management System built using Django REST Framework (DRF).
This project demonstrates how to manage Products, Order Items, and Orders through RESTful APIs with clean serialization, validation, and relationship handling between models.

🚀 Features
* Product Management
    * Create, update, delete, and list products
    * Fields include: name, description, price, and stock
    * Search and filter support
* Order Item Management
    * Represents individual items within an order
    * Linked to both Product and Order models
    * Automatic price calculation based on product
* Order Management
    * Create and track orders containing multiple items
    * Calculate total order amount dynamically
    * Manage order status (e.g., Pending, Shipped, Delivered)
