# Dependency Injection (DI) in FastAPI

## What is Dependency Injection?

Dependency Injection (DI) is a design pattern where one function or class receives the resources it needs from an external source instead of creating them itself.

In FastAPI, dependencies are injected using the `Depends()` function.

A dependency can be:

- Authentication
- Database connection
- API key validation
- JWT token verification
- Configuration settings
- Common business logic
- Logging

---

# Why Use Dependency Injection?

Without Dependency Injection, you would repeat the same code in every API.

### Without Dependency Injection

```python
from fastapi import FastAPI

app = FastAPI()

@app.get("/users")
def get_users():
    token = "abc123"
    # Validate token
    return {"message": "Users"}

@app.get("/products")
def get_products():
    token = "abc123"
    # Validate token
    return {"message": "Products"}
```

Here, the token validation logic is duplicated.

---

### With Dependency Injection

```python
from fastapi import FastAPI, Depends

app = FastAPI()

def validate_token():
    return {"user": "Ujjwal"}

@app.get("/users")
def get_users(user=Depends(validate_token)):
    return user

@app.get("/products")
def get_products(user=Depends(validate_token)):
    return user
```

The validation logic is written only once and reused across multiple endpoints.

---

# Syntax

```python
Depends(dependency_function)
```

General structure:

```python
@app.get("/example")
def example(data=Depends(dependency_function)):
    return data
```

---

# How Dependency Injection Works

Suppose you have:

```python
from fastapi import FastAPI, Depends

app = FastAPI()

def get_user():
    return {
        "name": "Ujjwal"
    }

@app.get("/profile")
def profile(user=Depends(get_user)):
    return user
```

### Request

```
GET /profile
```

### Internal Workflow

```
Client Request
      │
      ▼
FastAPI receives request
      │
      ▼
Depends(get_user)
      │
      ▼
Execute get_user()
      │
      ▼
Return {"name":"Ujjwal"}
      │
      ▼
Pass result to profile()
      │
      ▼
Return response
```

FastAPI automatically calls the dependency before executing the endpoint.

---

# Dependency with Query Parameters

```python
from fastapi import FastAPI, Depends

app = FastAPI()

def get_user(name: str):
    return {
        "User": name
    }

@app.get("/home")
def home(data=Depends(get_user)):
    return {
        "Validation": "Pass",
        "User": data
    }
```

### Request

```
GET /home?name=Ujjwal
```

### Response

```json
{
    "Validation": "Pass",
    "User": {
        "User": "Ujjwal"
    }
}
```

---

# Dependency Execution Order

FastAPI always executes dependencies before the endpoint.

```
Request
   │
   ▼
Dependency 1
   │
   ▼
Dependency 2
   │
   ▼
Endpoint Function
   │
   ▼
Response
```

If a dependency raises an exception, the endpoint is never executed.

---

# Dependency Returning a Value

```python
from fastapi import Depends, FastAPI

app = FastAPI()

def add():
    return 10 + 20

@app.get("/")
def home(result=Depends(add)):
    return {
        "Answer": result
    }
```

Response

```json
{
    "Answer": 30
}
```

---

# Authentication Example

```python
from fastapi import Depends, HTTPException

def verify_token(token: str):
    if token != "abc123":
        raise HTTPException(
            status_code=401,
            detail="Invalid Token"
        )

    return {
        "username": "Ujjwal"
    }

@app.get("/dashboard")
def dashboard(user=Depends(verify_token)):
    return {
        "message": "Welcome",
        "user": user
    }
```

FastAPI executes `verify_token()` first.

If the token is invalid:

- The request stops immediately.
- The endpoint is never executed.
- A `401 Unauthorized` response is returned.

---

# Common Use Cases

Dependency Injection is commonly used for:

- User Authentication
- Authorization
- Database Sessions
- API Key Validation
- JWT Token Validation
- Logging
- Configuration Management
- Email Services
- Caching
- Shared Business Logic

---

# Advantages

- Eliminates duplicate code
- Improves code readability
- Encourages modular design
- Makes testing easier
- Simplifies maintenance
- Promotes code reuse
- Follows Clean Architecture principles

---

# Best Practices

- Keep dependencies focused on a single responsibility.
- Avoid placing business logic inside dependencies unless it is shared.
- Give dependency functions descriptive names.
- Reuse dependencies whenever possible.
- Use dependencies for cross-cutting concerns like authentication, logging, and database access.

---

# Summary

| Component | Purpose |
|-----------|---------|
| `Depends()` | Declares a dependency |
| Dependency Function | Executes before the endpoint |
| Return Value | Passed as an argument to the endpoint |
| Exception in Dependency | Stops request execution and returns an error response |
| Main Benefit | Code reuse and separation of concerns |

---

# Key Points

- Dependency Injection allows FastAPI to automatically provide required resources to an endpoint.
- `Depends()` tells FastAPI which function should run first.
- The dependency's return value is injected into the endpoint function.
- Dependencies help avoid duplicate code and improve maintainability.
- Authentication, database sessions, configuration, and logging are the most common real-world applications of Dependency Injection.