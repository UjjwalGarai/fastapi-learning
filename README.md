# SQLAlchemy CRUD Operations with FastAPI

## Overview

**SQLAlchemy** is one of the most popular Object Relational Mappers (ORM) in Python. It allows developers to interact with databases using Python classes and objects instead of writing raw SQL queries.

In this project, SQLAlchemy is integrated with **FastAPI** to perform basic **CRUD (Create, Read, Update, Delete)** operations on a SQLite database.

---

# Technologies Used

- FastAPI
- SQLAlchemy ORM
- SQLite3
- Uvicorn

---

# Project Workflow

```text
Client Request
      │
      ▼
FastAPI Endpoint
      │
      ▼
Dependency Injection (Database Session)
      │
      ▼
SQLAlchemy ORM
      │
      ▼
SQLite Database
      │
      ▼
Response to Client
```

---

# Step 1: Create Database Engine

```python
DATABASE_URL = "sqlite:///./test.db"

engine = create_engine(
    DATABASE_URL,
    connect_args={"check_same_thread": False}
)
```

### Explanation

- `DATABASE_URL` specifies the SQLite database file.
- `create_engine()` establishes the connection between the application and the database.
- `check_same_thread=False` allows SQLite to be used with FastAPI's multi-threaded request handling.

---

# Step 2: Create the Base Class

```python
class Base(DeclarativeBase):
    pass
```

### Explanation

The `Base` class is the parent class for all database models. Every SQLAlchemy model should inherit from this class.

---

# Step 3: Create the Database Model

```python
class Todos(Base):
    __tablename__ = "todos"

    id = Column(Integer, primary_key=True, index=True)
    title = Column(String)
    status = Column(String)
```

### Explanation

- `__tablename__` defines the database table name.
- `id` is the primary key.
- `title` stores the todo title.
- `status` stores the completion status.

---

# Step 4: Create the Table

```python
Base.metadata.create_all(bind=engine)
```

### Explanation

This creates all tables defined by your models if they do not already exist.

---

# Step 5: Create a Session Factory

```python
sessionLocal = sessionmaker(bind=engine)
```

### Explanation

`sessionmaker()` creates a factory for generating database sessions. Each request gets its own session.

---

# Step 6: Database Dependency

```python
def get_db():
    db = sessionLocal()
    try:
        yield db
    finally:
        db.close()
```

### Explanation

This dependency:

- Opens a database session.
- Makes it available to the endpoint.
- Automatically closes the session after the request completes.

This prevents database connection leaks.

---

# CRUD Operations

## 1. Create (POST)

```python
@app.post("/todo")
def createTodo(title: str, db: Session = Depends(get_db)):
    todo = Todos(title=title, status="False")

    db.add(todo)
    db.commit()
    db.refresh(todo)

    return todo
```

### Workflow

1. Create a new `Todos` object.
2. Add it to the session.
3. Commit the transaction.
4. Refresh the object to retrieve generated values (such as `id`).
5. Return the saved record.

---

## 2. Read All (GET)

```python
@app.get("/todos")
def get_all_todos(db: Session = Depends(get_db)):
    todos = db.query(Todos).all()
    return todos
```

### Explanation

- `db.query(Todos)` selects all records from the `todos` table.
- `.all()` returns every record as a list.

---

## 3. Read Single Record (GET)

```python
@app.get("/todos/{todo_id}")
def get_todo(todo_id: int, db: Session = Depends(get_db)):
    todo = db.query(Todos).filter(
        Todos.id == todo_id
    ).first()

    if not todo:
        raise HTTPException(404, "Todo not found")

    return todo
```

### Explanation

- Filters records using the provided `todo_id`.
- Returns the first matching record.
- Returns a **404 Not Found** error if the record does not exist.

---

## 4. Update (PUT)

```python
@app.put("/todo/{id}")
def modify_todo(
    id: int,
    title: str,
    status: str,
    db: Session = Depends(get_db)
):
    todo = db.query(Todos).filter(
        Todos.id == id
    ).first()

    if not todo:
        raise HTTPException(404, "Todo not found")

    todo.title = title
    todo.status = status

    db.commit()

    return {
        "message": "Todo updated"
    }
```

### Explanation

- Find the existing record.
- Update the required fields.
- Commit the transaction.
- Return a success message.

---

## 5. Delete (DELETE)

```python
@app.delete("/todo/{id}")
def delete_todo(
    id: int,
    db: Session = Depends(get_db)
):
    todo = db.query(Todos).filter(
        Todos.id == id
    ).first()

    if not todo:
        raise HTTPException(404, "Todo not found")

    db.delete(todo)
    db.commit()

    return {
        "message": "Todo deleted"
    }
```

### Explanation

- Find the record.
- Delete it from the session.
- Commit the transaction.
- Return a confirmation message.

---

# SQLAlchemy Session Methods

| Method | Purpose |
|---------|---------|
| `db.add()` | Adds a new object to the session. |
| `db.commit()` | Saves all pending changes to the database. |
| `db.refresh()` | Reloads the object from the database after committing. |
| `db.query()` | Retrieves data from a table. |
| `filter()` | Filters records based on a condition. |
| `first()` | Returns the first matching record or `None`. |
| `all()` | Returns all matching records as a list. |
| `db.delete()` | Marks a record for deletion. |
| `db.close()` | Closes the database session. |

---

# CRUD Flow Diagram

```text
CREATE
Client
   │
   ▼
Create Model Object
   │
   ▼
db.add()
   │
   ▼
db.commit()
   │
   ▼
db.refresh()
   │
   ▼
Response

--------------------------------

READ
Client
   │
   ▼
db.query()
   │
   ▼
filter()/all()
   │
   ▼
Response

--------------------------------

UPDATE
Client
   │
   ▼
Find Record
   │
   ▼
Modify Fields
   │
   ▼
db.commit()
   │
   ▼
Response

--------------------------------

DELETE
Client
   │
   ▼
Find Record
   │
   ▼
db.delete()
   │
   ▼
db.commit()
   │
   ▼
Response
```

---

# Advantages of SQLAlchemy ORM

- Reduces the need to write raw SQL queries.
- Improves code readability and maintainability.
- Supports multiple database systems (SQLite, PostgreSQL, MySQL, etc.).
- Provides built-in protection against SQL injection through parameterized queries.
- Integrates seamlessly with FastAPI.

---

# Best Practices

- Use a separate database session for each request.
- Always close the session using dependency injection.
- Raise appropriate HTTP exceptions when resources are not found.
- Keep database models and API schemas separate in larger projects.
- Use Pydantic models for request and response validation instead of accepting raw query parameters for create and update operations.

---

# Summary

- `create_engine()` creates the database connection.
- `DeclarativeBase` is the parent class for all ORM models.
- `sessionmaker()` creates database sessions.
- `Depends(get_db)` injects a database session into each endpoint.
- `db.add()`, `db.commit()`, and `db.refresh()` are used to create records.
- `db.query()` retrieves records.
- `db.delete()` removes records.
- SQLAlchemy ORM allows developers to work with Python objects instead of writing raw SQL, resulting in cleaner, more maintainable, and database-independent code.