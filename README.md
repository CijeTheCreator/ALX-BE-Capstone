Here's a detailed and well-documented README file for your Django E-commerce API, covering all the key components including user accounts, products, wishlists, reviews, and discounts. This README is designed to provide a comprehensive guide to understanding the API and how to interact with it.

---

# E-commerce API

This API is built using Django and Django REST Framework to power an e-commerce platform. It provides core functionalities including user authentication, product management, reviews, wishlists, and discounts.

## Table of Contents

1. [Project Overview](#project-overview)
2. [Setup and Installation](#setup-and-installation)
3. [Authentication](#authentication)
4. [Endpoints](#endpoints)
   - [Users (Accounts)](#users-accounts)
   - [Products](#products)
   - [Wishlists](#wishlists)
   - [Reviews](#reviews)
   - [Discounts](#discounts)
5. [Testing the API](#testing-the-api)
6. [Contribution Guidelines](#contribution-guidelines)
7. [License](#license)

---

## Project Overview

This API enables users to:

- Register, log in, and manage their accounts.
- Create, update, and delete products.
- Submit reviews and ratings for products.
- Create and manage wishlists.
- Create and manage discounts on products.

---

## Setup and Installation

### Prerequisites

- Python 3.8+
- Django 4.2+
- Django REST Framework
- PostgreSQL (or SQLite for development)

### Installation Steps

1. Clone the repository:

   ```bash
   git clone https://github.com/your-repo/e_commerce_api.git
   ```

2. Navigate to the project directory:

   ```bash
   cd e_commerce_api
   ```

3. Create a virtual environment:

   ```bash
   python -m venv env
   source env/bin/activate   # On Windows: env\Scripts\activate
   ```

4. Install the required packages:

   ```bash
   pip install django
   ```

5. Configure your database in `settings.py` (SQLite is default, but PostgreSQL can be used in production).

6. Apply migrations:

   ```bash
   python manage.py makemigrations
   python manage.py migrate
   ```

7. Run the development server:

   ```bash
   python manage.py runserver
   ```

8. Access the API at `http://127.0.0.1:8000/`

---

## Authentication

This API uses token-based authentication. Users must authenticate via token to interact with most endpoints.

### Obtain Authentication Token

- **URL**: `/api/auth/token/login/`
- **Method**: `POST`
- **Request Body**:
  ```json
  {
    "username": "your_username",
    "password": "your_password"
  }
  ```
- **Response**:
  ```json
  {
    "auth_token": "your_token"
  }
  ```

Include the token in the Authorization header for authenticated requests:

```bash
Authorization: Token your_token
```

---

## Endpoints

### 1. **Users (Accounts)**

#### Register a New User

- **URL**: `/api/auth/users/`
- **Method**: `POST`
- **Request Body**:
  ```json
  {
    "username": "newuser",
    "password": "newpassword",
    "email": "newuser@example.com"
  }
  ```
- **Response**:
  ```json
  {
    "id": 1,
    "username": "newuser",
    "email": "newuser@example.com"
  }
  ```

#### User Login

- **URL**: `/api/auth/token/login/`
- **Method**: `POST`
- See [Authentication](#authentication) for request details.

#### Get User Profile

- **URL**: `/api/auth/users/me/`
- **Method**: `GET`
- **Authentication Required**: Yes

---

### 2. **Products**

#### List All Products

- **URL**: `/api/products/`
- **Method**: `GET`
- **Response**:
  ```json
  [
    {
      "id": 1,
      "name": "Product 1",
      "description": "A detailed description",
      "price": 99.99,
      "category": "Electronics",
      "stock_quantity": 50,
      "image_url": "http://localhost:8000/media/images/product1.jpg",
      "created_date": "2024-10-01"
    }
  ]
  ```

#### Create a New Product

- **URL**: `/api/products/`
- **Method**: `POST`
- **Authentication Required**: Yes
- **Request Body**:
  ```json
  {
    "name": "Product Name",
    "description": "Product description",
    "price": 59.99,
    "category": "Category Name",
    "stock_quantity": 100,
    "image_url": "http://localhost:8000/media/images/product_image.jpg"
  }
  ```

#### Retrieve a Product by ID

- **URL**: `/api/products/{id}/`
- **Method**: `GET`

#### Update a Product by ID

- **URL**: `/api/products/{id}/`
- **Method**: `PUT` or `PATCH`

#### Delete a Product by ID

- **URL**: `/api/products/{id}/`
- **Method**: `DELETE`

---

### 3. **Wishlists**

#### List User's Wishlist

- **URL**: `/api/wishlists/`
- **Method**: `GET`

#### Add a Product to Wishlist

- **URL**: `/api/wishlists/`
- **Method**: `POST`
- **Request Body**:
  ```json
  {
    "product_id": 1
  }
  ```

#### Remove a Product from Wishlist

- **URL**: `/api/wishlists/{id}/`
- **Method**: `DELETE`

---

### 4. **Reviews**

#### List All Reviews for a Product

- **URL**: `/api/reviews/product/{product_id}/`
- **Method**: `GET`

#### Submit a Review

- **URL**: `/api/reviews/`
- **Method**: `POST`
- **Request Body**:
  ```json
  {
    "rating": 5,
    "review_text": "Great product!",
    "product_id": 1
  }
  ```

#### Update a Review

- **URL**: `/api/reviews/{id}/`
- **Method**: `PUT` or `PATCH`

#### Delete a Review

- **URL**: `/api/reviews/{id}/`
- **Method**: `DELETE`

---

### 5. **Discounts**

#### List All Discounts

- **URL**: `/api/discounts/`
- **Method**: `GET`

#### Create a New Discount

- **URL**: `/api/discounts/`
- **Method**: `POST`
- **Request Body**:
  ```json
  {
    "percentage": 10,
    "start_date": "2024-10-01",
    "end_date": "2024-10-31",
    "product_id": 1
  }
  ```

#### Update a Discount

- **URL**: `/api/discounts/{id}/`
- **Method**: `PUT` or `PATCH`

#### Delete a Discount

- **URL**: `/api/discounts/{id}/`
- **Method**: `DELETE`

---
