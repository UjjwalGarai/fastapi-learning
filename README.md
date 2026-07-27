# SQLite3 with FastAPI

## What is SQLite3?

**SQLite3** is a lightweight, serverless, file-based relational database that comes built into Python. Unlike databases such as PostgreSQL or MySQL, SQLite does not require a separate database server. All data is stored in a single `.db` file, making it an excellent choice for learning, prototyping, and small applications.

---

## Why Use SQLite3?

- No installation or database server required.
- Built into Python (`sqlite3` module).
- Easy to configure and use.
- Stores data in a single database file.
- Ideal for development, testing, and small projects.

---

## Creating a Database Connection

```python
import sqlite3

conn = sqlite3.connect("test.db", check_same_thread=False)
```

### Explanation

- `test.db` → Creates (or opens) a database file named **test.db**.
- `check_same_thread=False` → Allows the same database connection to be used across multiple threads, which is useful when working with FastAPI.

---

## Creating a Cursor

```python
cursor = conn.cursor()
```

A **cursor** is an object used to execute SQL statements such as `CREATE`, `INSERT`, `SELECT`, `UPDATE`, and `DELETE`.

---

## Creating a Table

```python
cursor.execute("""
    CREATE TABLE IF NOT EXISTS todos(
        id INTEGER PRIMARY KEY,
        TITLE TEXT,
        STATUS TEXT
    )
""")
```

### Explanation

- `CREATE TABLE` → Creates a new table.
- `IF NOT EXISTS` → Prevents an error if the table already exists.
- `id INTEGER PRIMARY KEY` → Unique identifier for each record.
- `TITLE TEXT` → Stores the todo title.
- `STATUS TEXT` → Stores the task status (e.g., Pending or Completed).

---

## Saving Changes

```python
conn.commit()
```

The `commit()` method permanently saves changes made to the database. Without calling `commit()`, changes such as table creation or data insertion may not be stored.

---

## Complete Example

```python
from fastapi import FastAPI
import sqlite3

app = FastAPI(title="SQLite3 Learning")

conn = sqlite3.connect("test.db", check_same_thread=False)
cursor = conn.cursor()

cursor.execute("""
    CREATE TABLE IF NOT EXISTS todos(
        id INTEGER PRIMARY KEY,
        TITLE TEXT,
        STATUS TEXT
    )
""")

conn.commit()
```

---

## Workflow

```text
FastAPI Application
        │
        ▼
Connect to SQLite Database
        │
        ▼
Create Cursor
        │
        ▼
Execute SQL Query
        │
        ▼
Commit Changes
        │
        ▼
Database Ready
```

---

## Advantages

- Simple and beginner-friendly.
- No external database server required.
- Fast for small applications.
- Easy to integrate with FastAPI.
- Perfect for learning SQL and database operations.

---

## Limitations

- Not suitable for high-concurrency applications.
- Limited scalability compared to PostgreSQL or MySQL.
- Best suited for development, testing, and small projects.

---

## Key Points

- SQLite3 is a built-in Python database.
- A database connection is created using `sqlite3.connect()`.
- A cursor executes SQL statements.
- `CREATE TABLE IF NOT EXISTS` creates a table only if it doesn't already exist.
- `commit()` saves all database changes permanently.
- SQLite is an excellent choice for learning FastAPI before moving to production databases like PostgreSQL.