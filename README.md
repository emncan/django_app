# Django app with Docker, PostgreSQL, Gunicorn, and Nginx

Sample product management django api using JWT token authentication.

## Usage

Uses gunicorn + nginx.

1. Build the images and run the containers:

    ```sh
    $ docker-compose up -d --build
    ```
  To apply changes, the image must be re-built.
  
## API Functionality

### 1. Create New User and Login Get JWT Token
#### 1.1. Register for new user.

  ```sh
  http://127.0.0.1:8000/api/register/

  {   
    "email":"test@testuser.com",
    "username":"test_user",
    "password":"admin_123456"
  }
  ```

#### 1.2. Login and get jwt token for auth.

  ```sh
  http://127.0.0.1:8000/api/login/

  {   
    "username":"test_user",
    "password":"admin_123456"
  }
  ```

  ![login](https://user-images.githubusercontent.com/30287266/141646938-30c25879-3f29-4cc4-816d-e5ac697a0560.png)

#### 1.3. Refresh JWT Token.

  ```sh
  http://127.0.0.1:8000/api/login/refresh/

  {
      "refresh":"refresh token"
  }
  ```

  ![refresh](https://user-images.githubusercontent.com/30287266/141647095-0c6362db-6129-46c1-91fe-f92216335892.png)
      
### 2. Add Product

  ```sh
  http://127.0.0.1:8000/api/products/

  {
    "product_name":"test_product_1",
    "cat_id":"1230123",
    "stock":"2",
    "barcod":"1234567",
    "manufacturer":"test_prod_manufacturer"
  }
  ```
  
  ![add](https://user-images.githubusercontent.com/30287266/141647299-e0057662-a717-4fd1-86fa-809b22127e68.png)
  
### 3. Get List of Product

  ```sh
  http://127.0.0.1:8000/api/products/
  ```
  
  ![list](https://user-images.githubusercontent.com/30287266/141648053-a9906b38-b397-4309-9836-534b9e2c24d8.png)

### 4. Update Product

   ```sh
  http://127.0.0.1:8000/api/products/<id>
  ```
  
  ![update](https://user-images.githubusercontent.com/30287266/141648159-437f8a13-c9a4-4344-9497-fcb62b3ac83e.png)

### 5. Delete Product

  ```sh
  http://127.0.0.1:8000/api/products/<id>
  ```
  
  ![delete](https://user-images.githubusercontent.com/30287266/141648185-c0ed9a78-4682-431a-a558-8cf8552b284d.png)

### 6. Filtering Object 

#### 6.1 Equality-Based Filtering.

Listing the set of fields you wish to filter against.

  ```sh
    http://127.0.0.1:8000/api/products_filter?manufacturer=test_prod_manufacturer
  ```
  
  ![filter](https://user-images.githubusercontent.com/30287266/141648671-be20ec46-c9d1-4c2d-8851-b018491ab27b.png)

#### 6.2 Search Filtering.
 
This will allow the client to filter the items in the list by making queries such as: (searches by product name and manufacturer)

   ```sh
    http://127.0.0.1:8000/api/products_search?search=test
  ```
#### 6.3 Ordering Filter.

Simple query parameter controlled ordering of results.

For example, to order products by product name:

  ```sh
    http://127.0.0.1:8000/api/products_order?ordering=product_name
  ```
  
  ![order2](https://user-images.githubusercontent.com/30287266/141649061-8796d141-46d9-4e5b-a97e-68c0bb9d07a8.png)

The client may also specify reverse orderings by prefixing the field name with '-', like so:

  ```sh
    http://127.0.0.1:8000/api/products_order?ordering=-product_name
  ```
  
Multiple orderings may also be specified:
 
  ```sh
  http://127.0.0.1:8000/api/products_order?ordering=product_name,stock
  ```
 
