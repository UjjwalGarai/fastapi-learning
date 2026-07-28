````markdown
# Asynchronous Programming (`asyncio`) in FastAPI

## Overview

FastAPI is built on **ASGI (Asynchronous Server Gateway Interface)**, which allows it to handle multiple requests concurrently using Python's `asyncio` library.

Asynchronous programming enables a program to perform other tasks while waiting for time-consuming operations (such as database queries, API calls, or file operations) to complete. This improves the performance and scalability of web applications.

---

# Synchronous vs Asynchronous Programming

## Synchronous Execution

In synchronous programming, tasks execute **one after another**. The next task cannot start until the previous one finishes.

```python
import time

def sync_task(task_id: int):
    print(f"Sync Task {task_id} Start")
    time.sleep(2)
    print(f"Sync Task {task_id} Completed")

sync_task(1)
sync_task(2)
```

### Workflow

```text
Task 1 Start
     │
     ▼
Wait 2 Seconds
     │
     ▼
Task 1 Complete
     │
     ▼
Task 2 Start
     │
     ▼
Wait 2 Seconds
     │
     ▼
Task 2 Complete
```

### Execution Time

```
Task 1 → 2 Seconds
Task 2 → 2 Seconds

Total ≈ 4 Seconds
```

---

# Asynchronous Execution

In asynchronous programming, multiple tasks can run concurrently. While one task is waiting, another task can continue executing.

```python
import asyncio

async def async_task(task_id: int):
    print(f"Async Task {task_id} Start")
    await asyncio.sleep(2)
    print(f"Async Task {task_id} Completed")

async def main():
    await asyncio.gather(
        async_task(1),
        async_task(2)
    )

asyncio.run(main())
```

### Workflow

```text
Task 1 Start
      │
      ├─────────────┐
      ▼             ▼
Waiting         Task 2 Start
      │             │
      └──────┬──────┘
             ▼
Both Complete Together
```

### Execution Time

```
Task 1 → 2 Seconds
Task 2 → 2 Seconds

Total ≈ 2 Seconds
```

---

# Understanding the Keywords

## `async`

Declares an asynchronous function (coroutine).

```python
async def async_task():
    ...
```

An `async` function must be executed inside an event loop.

---

## `await`

Pauses the current coroutine until another asynchronous operation finishes.

```python
await asyncio.sleep(2)
```

Unlike `time.sleep()`, `await` does **not** block the entire program. It allows other asynchronous tasks to run.

---

## `asyncio.sleep()`

```python
await asyncio.sleep(2)
```

- Non-blocking delay.
- Used only inside `async` functions.
- Allows the event loop to continue executing other tasks.

---

## `asyncio.gather()`

```python
await asyncio.gather(
    async_task(1),
    async_task(2)
)
```

Runs multiple asynchronous tasks concurrently and waits until all of them complete.

---

## `asyncio.run()`

```python
asyncio.run(main())
```

Starts the event loop and executes the main coroutine.

---

# Why `time.sleep()` Blocks the Program

```python
time.sleep(2)
```

During this delay:

- The current thread is blocked.
- No other code executes in that thread.
- The program waits until the sleep finishes.

---

# Why `await asyncio.sleep()` Doesn't Block

```python
await asyncio.sleep(2)
```

During this delay:

- The coroutine pauses.
- The event loop switches to another available task.
- Overall application performance improves.

---

# Using Async in FastAPI

FastAPI supports both synchronous and asynchronous endpoints.

### Synchronous Endpoint

```python
@app.get("/sync")
def sync_api():
    time.sleep(2)
    return {"message": "Completed"}
```

### Asynchronous Endpoint

```python
@app.get("/async")
async def async_api():
    await asyncio.sleep(2)
    return {"message": "Completed"}
```

The asynchronous endpoint can serve other requests while waiting, making it more efficient for I/O-bound operations.

---

# Common Use Cases

Use asynchronous programming for:

- Database queries
- External API requests
- File uploads and downloads
- Email sending
- Background processing
- Cloud storage operations
- Network communication

---

# Advantages

- Better performance for I/O-bound tasks.
- Handles many client requests efficiently.
- Improves application scalability.
- Reduces idle waiting time.
- Makes better use of system resources.

---

# Limitations

- Not beneficial for CPU-intensive tasks.
- Code can be more complex to understand.
- Requires asynchronous libraries to gain full benefits.

---

# Summary

| Concept | Description |
|---------|-------------|
| `async` | Declares an asynchronous function. |
| `await` | Waits for an asynchronous operation without blocking other tasks. |
| `asyncio.sleep()` | Non-blocking delay. |
| `time.sleep()` | Blocking delay. |
| `asyncio.gather()` | Runs multiple asynchronous tasks concurrently. |
| `asyncio.run()` | Starts the event loop and executes the main coroutine. |

---

# Key Points

- FastAPI is built on ASGI and has first-class support for asynchronous programming.
- Synchronous code executes one task at a time.
- Asynchronous code allows multiple I/O-bound tasks to progress concurrently.
- `await` pauses only the current coroutine, not the entire application.
- Use `async` endpoints when working with asynchronous libraries such as async database drivers or HTTP clients.
- Use synchronous functions when the task is simple or relies on blocking libraries that do not support asynchronous execution.
````
