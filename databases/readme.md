# **Introduction to Databases**
A **database** is an organized collection of data that can be accessed, managed, and updated efficiently. It allows storing data in a structured manner, making it easy to retrieve and manipulate.

### **Types of Databases**
1. **Relational Databases (SQL)**
    - Uses structured schema (tables with rows and columns).
    - Data is stored in a tabular format.
    - Ensures ACID (Atomicity, Consistency, Isolation, Durability) properties.
    - Examples: MySQL, PostgreSQL, SQLite, SQL Server.

2. **Non-Relational Databases (NoSQL)**
    - Schema-less or dynamic schema.
    - Can store data in different formats like documents, key-value pairs, graphs, or wide-columns.
    - Provides high scalability and flexibility.
    - Examples: MongoDB, Cassandra, Redis, Firebase.

---

### **SQL vs NoSQL**
| Feature       | SQL (Relational)  | NoSQL (Non-Relational)  |
|--------------|------------------|------------------------|
| Structure    | Tables (rows & columns) | Documents, Key-Value, Graphs |
| Schema       | Fixed schema     | Dynamic schema |
| Scalability  | Vertical Scaling | Horizontal Scaling |
| Transactions | ACID Compliance  | BASE (Basically Available, Soft state, Eventual consistency) |
| Query Language | SQL | Query languages like MongoDB Query Language (MQL) |
| Use Case     | Structured Data, Banking, ERP | Big Data, Real-time apps, JSON-based |

---

# **MongoDB and PyMongo CRUD Operations**
MongoDB is a **NoSQL document-based database**, and **PyMongo** is a Python library to interact with MongoDB.

#### **1. Install PyMongo**
```sh
pip install pymongo
```

#### **2. Connect to MongoDB**
```python
from pymongo import MongoClient

client = MongoClient("mongodb://localhost:27017/")
db = client["students_db"]
collection = db["students"]
```

---

### **CRUD Operations in PyMongo**

#### **Create (Insert Data)**
```python
# Insert One
student = {"name": "Ali", "age": 22, "course": "Database"}
collection.insert_one(student)

# Insert Multiple
students = [
    {"name": "Sara", "age": 21, "course": "AI"},
    {"name": "Ahmed", "age": 23, "course": "Web Dev"}
]
collection.insert_many(students)
```

---

#### **Read (Retrieve Data)**
```python
# Find One
student = collection.find_one({"name": "Ali"})
print(student)

# Find All
for student in collection.find():
    print(student)

# Find with Condition
for student in collection.find({"course": "AI"}):
    print(student)
```

---

#### **Update (Modify Data)**
```python
# Update One
collection.update_one({"name": "Ali"}, {"$set": {"age": 23}})

# Update Many
collection.update_many({"course": "AI"}, {"$set": {"course": "Machine Learning"}})
```

---

#### **Delete (Remove Data)**
```python
# Delete One
collection.delete_one({"name": "Ali"})

# Delete Many
collection.delete_many({"course": "Machine Learning"})
```

---

### **Bonus: Advanced MongoDB Queries**
- **Sorting**: `collection.find().sort("age", -1)` (Descending)
- **Limiting Results**: `collection.find().limit(5)`
- **Projection (Selecting Fields)**: `collection.find({}, {"_id": 0, "name": 1})`

---

# **Setting Up Alembic with PostgreSQL in a FastAPI Project**

### **Installation**
To set up the project with Alembic and PostgreSQL, install the required dependencies using Poetry:
```sh
poetry add alembic psycopg2-binary
```

### **New Project Setup**
Follow these steps to initialize Alembic and configure it for database migrations:

#### **1. Initialize Alembic**
```sh
poetry run alembic init alembic
```

#### **2. Set the Database URL**
Locate the `alembic.ini` file and modify the `sqlalchemy.url` entry to point to your PostgreSQL database, e.g.:
```ini
sqlalchemy.url = postgresql+psycopg2://user:password@localhost/dbname
```

#### **3. Create SQLAlchemy Model**
Define a SQLAlchemy model for your table, for example:
```python
from sqlalchemy import Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()

class Todo(Base):
    __tablename__ = 'todos'
    id = Column(Integer, primary_key=True, index=True)
    title = Column(String, nullable=False)
    description = Column(String, nullable=True)
```

#### **4. Set Target Metadata in Alembic**
Open `alembic/env.py` and update the target metadata:
```python
from models import Base  # Import the model base
target_metadata = Base.metadata
```

### **Running Migrations**
Whenever you make changes to your models, run the following commands:

#### **Generate Migration Script**
```sh
poetry run alembic revision --autogenerate -m "create todos table"
```

#### **Apply Migrations**
```sh
poetry run alembic upgrade head
```
This will create and apply the necessary database schema changes based on your models.

---

### **CRUD Operations in SQL Databases**

#### **Create (Insert Data)**
```python
from sqlalchemy.orm import Session
from models import Todo

def create_todo(db: Session, title: str, description: str = None):
    db_todo = Todo(title=title, description=description)
    db.add(db_todo)
    db.commit()
    db.refresh(db_todo)
    return db_todo
```

#### **Read (Retrieve Data)**
```python
def get_todo_by_id(db: Session, todo_id: int):
    return db.query(Todo).filter(Todo.id == todo_id).first()

def get_all_todos(db: Session):
    return db.query(Todo).all()
```

#### **Update (Modify Data)**
```python
def update_todo(db: Session, todo_id: int, title: str = None, description: str = None):
    db_todo = db.query(Todo).filter(Todo.id == todo_id).first()
    if db_todo:
        if title:
            db_todo.title = title
        if description:
            db_todo.description = description
        db.commit()
        db.refresh(db_todo)
    return db_todo
```

#### **Delete (Remove Data)**
```python
def delete_todo(db: Session, todo_id: int):
    db_todo = db.query(Todo).filter(Todo.id == todo_id).first()
    if db_todo:
        db.delete(db_todo)
        db.commit()
    return db_todo
```

---

### **Setting Up Alembic with PostgreSQL in a FastAPI Project**

#### **1. Install Dependencies**
To set up the project with Alembic and PostgreSQL, install the required dependencies using Poetry:
```sh
poetry add alembic psycopg2-binary
```

#### **2. Initialize Alembic**
Initialize Alembic in your project directory:
```sh
poetry run alembic init alembic
```

#### **3. Configure Database URL**
Locate the `alembic.ini` file and modify the `sqlalchemy.url` entry to point to your PostgreSQL database, e.g.:
```ini
sqlalchemy.url = postgresql+psycopg2://user:password@localhost/dbname
```

#### **4. Create SQLAlchemy Model**
Define a SQLAlchemy model for your table, for example:
```python
from sqlalchemy import Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()

class Todo(Base):
    __tablename__ = 'todos'
    id = Column(Integer, primary_key=True, index=True)
    title = Column(String, nullable=False)
    description = Column(String, nullable=True)
```

#### **5. Set Target Metadata in Alembic**
Open `alembic/env.py` and update the target metadata:
```python
from models import Base  # Import the model base
target_metadata = Base.metadata
```

#### **6. Generate Migration Script**
Whenever you make changes to your models, generate a migration script:
```sh
poetry run alembic revision --autogenerate -m "create todos table"
```

#### **7. Apply Migrations**
Apply the generated migrations to create the database schema:
```sh
poetry run alembic upgrade head
```

This will create and apply the necessary database schema changes based on your models.

---

### **Creating Database Schema**
To create the database schema, run the following command:
```sh
poetry run alembic upgrade head
```
This will apply all migrations and create the necessary tables in your PostgreSQL database.

---
