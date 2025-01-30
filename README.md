# Django REST Framework Authentication API

This project provides user authentication using Django REST Framework (DRF) with token-based authentication. It includes user registration, login, and authentication check endpoints.

## Features
- User registration with token generation
- User login with token retrieval
- Authentication check endpoint
- Uses Django's built-in `User` model
- Token-based authentication using `rest_framework.authtoken`

## Installation
### 1. Clone the Repository
```sh
git clone <repository-url>
cd <repository-folder>
```

### 2. Create and Activate Virtual Environment
```sh
python -m venv venv
source venv/bin/activate  # On Windows use `venv\Scripts\activate`
```

### 3. Install Dependencies
```sh
pip install -r requirements.txt
```

### 4. Apply Migrations
```sh
python manage.py migrate
```

### 5. Create a Superuser (Optional, for admin access)
```sh
python manage.py createsuperuser
```

### 6. Run the Server
```sh
python manage.py runserver
```

## API Endpoints
### 1. **Register a User**
#### Endpoint: `/register/`
#### Method: `POST`
#### Request Body:
```json
{
    "username": "exampleuser",
    "email": "user@example.com",
    "password": "securepassword"
}
```
#### Response:
```json
{
    "token": "generated-auth-token",
    "user": {
        "id": 1,
        "username": "exampleuser",
        "email": "user@example.com"
    }
}
```

### 2. **User Login**
#### Endpoint: `/login/`
#### Method: `POST`
#### Request Body:
```json
{
    "username": "exampleuser",
    "password": "securepassword"
}
```
#### Response:
```json
{
    "token": "user-auth-token",
    "user": {
        "id": 1,
        "username": "exampleuser",
        "email": "user@example.com"
    }
}
```

### 3. **Check Authentication**
#### Endpoint: `/auth/`
#### Method: `GET`
#### Headers:
```sh
Authorization: Token user-auth-token
```
#### Response:
```json
"this user is Authenticated"
```

## Dependencies
- Django
- Django REST Framework
- Django REST Framework Token Authentication

## Notes
- Ensure you have `rest_framework` and `rest_framework.authtoken` added to `INSTALLED_APPS` in `settings.py`.
- Run `python manage.py migrate` to apply token authentication models.
- Tokens are generated when users register and remain valid until deleted manually.

## License
This project is open-source and free to use under the MIT License.

