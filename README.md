# Bakery Management System

##  Overview

Bakery Management System is a Django-based web application developed to simplify bakery operations. The system helps manage customers, products, and orders from a single dashboard. It also provides real-time statistics and highlights the most popular product based on customer orders.

---

##  Features

* Dashboard with live statistics
* Customer Management (Add, Edit, Delete)
* Product Management (Add, Edit, Delete)
* Order Management (Add, Edit, Delete)
* Search Orders by Customer or Product
* Pending & Completed Order Tracking
* Most Popular Product
* Recent Orders

---

##  Technologies Used

* Python
* Django
* SQLite
* HTML
* CSS
* Bootstrap 5

---

##  Project Structure

```text
bakery_management/
│── accounts/
│── bakery_management/
│── customers/
│── orders/
│── products/
│── static/
│── templates/
│── manage.py
│── requirements.txt
│── db.sqlite3
```

---

##  Installation

Clone the repository

```bash
git clone https://github.com/pritibha-vishwakarma/bakery-management-system.git
```

Go to the project folder

```bash
cd bakery-management-system
```

Create a virtual environment

```bash
python -m venv venv
```

Activate the virtual environment

Windows

```bash
venv\Scripts\activate
```

Install dependencies

```bash
pip install -r requirements.txt
```

Apply migrations

```bash
python manage.py migrate
```

Run the development server

```bash
python manage.py runserver
```

Open your browser and visit:

```text
http://127.0.0.1:8000/
```

---

##  Modules

### Dashboard

* Total Orders
* Pending Orders
* Completed Orders
* Total Products
* Total Customers
* Recent Orders
* Most Popular Product

### Customers

* Add Customer
* Update Customer
* Delete Customer

### Products

* Add Product
* Update Product
* Delete Product

### Orders

* Create Order
* Update Order Status
* Delete Order
* Search Orders

---

##  Future Enhancements

* Customer Login
* Online Order Booking
* Payment Gateway Integration
* Invoice Generation
* Sales Reports
* Email Notifications

---

##  Developer

**Pritibha Vishwakarma**

GitHub: https://github.com/pritibha-vishwakarma
