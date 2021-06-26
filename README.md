# Product Management Django API

https://www.guru99.com/er-diagram-tutorial-dbms.html

Implement the Above ERD

The features supported provided by this service are listed below

1. CRUD Operations.
2. User Register and Login
3. User Authentication and Authorization.

# EndPoints

 - localhost:8000/ - To Access API Documentation/Swagger
 - /user/signup
 - /user/login   -- To Access Token
 - /product
 - /category
 - /apperalsize
 - /color


# Pre-requisites

Make sure to have installed the following pre-requisites for a development setup

1. Python 3.8.5 or greater
2. Install Postgresql database server.
3. Create a user by the name `admin` and password `admin` and grant all privileges to the user admin
4. Create a database by the name `product_db` if it does not exist using sql command

```bash
CREATE DATABASE IF NOT EXISTS vfq_assets encoding='utf8';
```

```bash
CREATE SCHEMA users AUTHORIZATION admin;
```

# Developer set-up instructions

1. Clone the repository.

```bash
pip install -r requirements.txt
```

2. Use the following command to run the migrations, which will create the required tables.

```bash
python manage.py migrate
```

3. Finally use the following command to start the development server.

```bash
python manage.py runserver
```