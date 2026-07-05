# HTTP Status Codes

HTTP status codes are three-digit numbers returned by a web server to indicate the outcome of a client's request. They help clients understand whether the request was successful, redirected, invalid, or failed due to a server issue.

---

# 🟢 2xx – Success

The request was successfully received, understood, and processed.

| Status Code | Description | Common Use Case |
|-------------|-------------|-----------------|
| **200 OK** | The request was successfully processed, and the requested data is returned in the response body. | GET, PUT |
| **201 Created** | The request was successful, and a new resource was created on the server. | POST |
| **204 No Content** | The request was successful, but the server does not return any response body. | DELETE, PUT |

### Example

```http
HTTP/1.1 200 OK
```

```json
{
    "message": "User found"
}
```

---

# 🔵 3xx – Redirection

The client must perform an additional action to complete the request.

| Status Code | Description | Common Use Case |
|-------------|-------------|-----------------|
| **301 Moved Permanently** | The requested resource has permanently moved to a new URL. Browsers update bookmarks and search engines transfer SEO value. | Website migration |
| **302 Found (Temporary Redirect)** | The resource is temporarily available at another URL. Browsers redirect the request, but search engines do not transfer SEO value. | Temporary maintenance |

---

# 🟠 4xx – Client Error

The request contains invalid data or the client is not allowed to access the resource.

| Status Code | Description | Common Use Case |
|-------------|-------------|-----------------|
| **400 Bad Request** | The request is malformed or contains invalid data. | Invalid JSON, missing required parameters |
| **401 Unauthorized** | Authentication is required or the provided credentials are invalid. | Missing or invalid JWT/API Token |
| **403 Forbidden** | The client is authenticated but does not have permission to access the resource. | Insufficient user permissions |
| **404 Not Found** | The requested resource could not be found on the server. | Invalid URL or non-existent resource |

### Example

```http
HTTP/1.1 404 Not Found
```

```json
{
    "detail": "User not found"
}
```

---

# 🔴 5xx – Server Error

The server encountered an unexpected error while processing the request.

| Status Code | Description | Common Use Case |
|-------------|-------------|-----------------|
| **500 Internal Server Error** | A generic server-side error indicating that something unexpected occurred. | Unhandled exception, application bug |
| **503 Service Unavailable** | The server is temporarily unavailable due to maintenance or high traffic. | Scheduled maintenance, server overload |

### Example

```http
HTTP/1.1 500 Internal Server Error
```

```json
{
    "detail": "Internal Server Error"
}
```

---

# Summary Table

| Category | Meaning | Status Codes |
|----------|---------|--------------|
| 🟢 **2xx** | Success | 200, 201, 204 |
| 🔵 **3xx** | Redirection | 301, 302 |
| 🟠 **4xx** | Client Error | 400, 401, 403, 404 |
| 🔴 **5xx** | Server Error | 500, 503 |

---

# Quick Memory Tips

- **200** → Request successful
- **201** → Resource created
- **204** → Success with no response body
- **301** → Permanent redirect
- **302** → Temporary redirect
- **400** → Bad request
- **401** → Authentication required
- **403** → Permission denied
- **404** → Resource not found
- **500** → Server error
- **503** → Server temporarily unavailable

---

# FastAPI Example

```python
from fastapi import FastAPI, HTTPException

app = FastAPI()

@app.get("/users/{user_id}")
def get_user(user_id: int):
    if user_id != 1:
        raise HTTPException(
            status_code=404,
            detail="User not found"
        )

    return {
        "message": "User found"
    }
```

### Response (Success)

```http
200 OK
```

```json
{
    "message": "User found"
}
```

### Response (Failure)

```http
404 Not Found
```

```json
{
    "detail": "User not found"
}
```