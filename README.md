# Internet Banking Application

This is an Internet Banking Application developed using Django Rest Framework. The application provides RESTful APIs for managing bank accounts, transactions, and user authentication.

## Features

- User Registration and Authentication
- View and manage Bank Accounts
- Perform Transactions (e.g., transfers, withdrawals, deposits)
- Transaction History
- Security Measures (e.g., two-factor authentication)


## Table of Contents

- [Getting Started](#getting-started)
  - [Technology Stack](#Technology Stack)
  - [Installation](#Installation)
- [Project Structure](#project-structure)
- [Configuration](#configuration)
- [API Documentation](#api-documentation)
- [Testing](#testing)
- [Contributing](#contributing)
- [License](#license)

## Getting Started

### Technology Stack
This project is built using the following technologies:

- Python: The core programming language used for development.
- Django: A powerful Python web framework.
- Django Rest Framework: A toolkit for building Web APIs in Django.
- PostgreSQL: A robust open-source relational database system.
- Docker: A containerization platform for easy deployment.
## Installation

### Clone the repository:

   ```bash
   git clone https://github.com/TatoSoselia/bank-rest-api
   ```

### Install Dependencies
Build the project's dependencies using Docker Compose:

```bash
docker-compose build
```

### Run the API
Start the API server with Docker Compose:

```bash
docker-compose up
```

### Register as Superuser
To access the admin panel and perform administrative tasks, you need to register as a superuser. Run the following command via Docker Compose:

```bash
docker-compose run --rm app sh -c "python manage.py createsuperuser"
```

Now, you can access the admin panel at:

```bash
http://127.0.0.1:8000/admin/
```
