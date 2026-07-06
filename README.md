# Middleware in FastAPI

## What is Middleware?

Middleware is a function that executes **before** a request reaches an API endpoint and **after** the endpoint returns a response. It acts as an intermediate layer between the client and the FastAPI application.

Middleware is commonly used for tasks that should apply to every request, such as logging, authentication, performance monitoring, CORS handling, and adding custom headers.

---

## Request Flow

```text
Client Request
      │
      ▼
Middleware (Before Request)
      │
      ▼
API Endpoint
      │
      ▼
Middleware (After Response)
      │
      ▼
Client Response
```

---

## Syntax

```python
from fastapi import FastAPI, Request

app = FastAPI()

@app.middleware("http")
async def custom_middleware(request: Request, call_next):
    print("Before Request")

    response = await call_next(request)

    print("After Response")

    return response
```

### How it Works

1. A client sends a request.
2. The middleware executes before the API endpoint.
3. `call_next(request)` forwards the request to the appropriate endpoint.
4. The endpoint processes the request and returns a response.
5. The middleware receives the response, performs any additional processing, and returns it to the client.

---

## Common Use Cases

- Request and response logging
- Authentication and authorization
- Measuring API execution time
- Adding custom response headers
- CORS handling
- Request validation
- Rate limiting

---

## Advantages

- Executes for every request automatically.
- Keeps common logic separate from endpoint functions.
- Reduces duplicate code.
- Improves application maintainability and readability.

---

## Key Points

- Middleware runs **before and after** every request.
- `call_next(request)` passes the request to the next component in the request pipeline.
- Multiple middleware functions execute in the order they are added.
- Use middleware for application-wide functionality, not endpoint-specific business logic.