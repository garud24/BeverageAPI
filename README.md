# Beverage API Tutorial

A simple REST API built with Python, Flask, and SQLAlchemy. This project demonstrates how to create a basic CRUD API for managing drinks using an SQLite database.



---

## Project Overview

This API lets you:

- Get all drinks
- Get a single drink by ID
- Add a new drink
- Delete a drink

It uses:

- Python
- Flask
- SQLAlchemy
- SQLite

---

## Project Structure

```bash
BeverageAPI/
├── api/
│   ├── application.py
│   ├── requirements.txt
│   └── instance/
├── create.py
├── README.md
└── .git/
```

### Main files

- `api/application.py` — contains the Flask app, database config, model, and API routes
- `api/requirements.txt` — required dependencies
- `create.py` — an unrelated example script, not part of the beverage API itself

---

## What This API Does

The app defines a `Drink` model with:

- `id`
- `name`
- `description`

Routes included:

- `GET /` — welcome message
- `GET /drinks` — returns all drinks
- `GET /drinks/<id>` — returns one drink by ID
- `POST /drinks` — adds a new drink
- `DELETE /drinks/<id>` — deletes a drink by ID

---

## Step 1: Install Python

Make sure Python 3 is installed on your machine.

Check it with:

```bash
python --version
```

If you use Python 3 by alias:

```bash
python3 --version
```

---

## Step 2: Create a Virtual Environment

Open a terminal inside the project folder and run:

```bash
cd "Documents/Git Hub/BeverageAPI"
python -m venv venv
```

Activate it:

On macOS/Linux:

```bash
source venv/bin/activate
```

On Windows:

```bash
venv\Scripts\activate
```

---

## Step 3: Install Dependencies

Install the packages from the requirements file:

```bash
pip install -r api/requirements.txt
```

This installs:

- Flask
- Flask-SQLAlchemy
- SQLAlchemy
- requests
- other Flask dependencies

---

## Step 4: Understand the Application Code

The main file is `api/application.py`.

### 1) Create the Flask app

```python
app = Flask(__name__)
```

This initializes your API application.

### 2) Configure SQLite database

```python
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///data.db"
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
```

This tells SQLAlchemy to store data in a local SQLite file named `data.db`.

### 3) Create the database object

```python
db = SQLAlchemy(app)
```

This connects Flask with SQLAlchemy so you can define database models.

### 4) Define the model

```python
class Drink(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(80), unique=True, nullable=False)
    description = db.Column(db.String(120))
```

This table will store each drink record.

### 5) Add routes

The app exposes endpoints for reading and writing records.

Example:

```python
@app.route('/drinks', methods=["POST"])
def add_drink():
    drink = Drink(name=request.json['name'], description=request.json['description'])
    db.session.add(drink)
    db.session.commit()
    return {'id': drink.id}
```

This function accepts JSON input, creates a new row, and saves it to the database.

---

## Step 5: Create the Database Tables

Before using the API, create the database tables.

From the project root, run:

```bash
python -c "from api.application import app, db; app.app_context().push(); db.create_all(); print('Database created successfully')"
```

This creates the SQLite database and the `drink` table.

---

## Step 6: Run the API

You can run the Flask app with:

```bash
export FLASK_APP=api/application.py
flask run
```

Or:

```bash
python -m flask --app api/application run --debug
```

The API will usually run at:

```text
http://127.0.0.1:5000
```

---

## Step 7: Test the API with curl

### Get all drinks

```bash
curl http://127.0.0.1:5000/drinks
```

### Get one drink by ID

```bash
curl http://127.0.0.1:5000/drinks/1
```

### Add a new drink

```bash
curl -X POST http://127.0.0.1:5000/drinks \
  -H "Content-Type: application/json" \
  -d '{"name":"Lemonade","description":"Fresh citrus drink"}'
```

### Delete a drink

```bash
curl -X DELETE http://127.0.0.1:5000/drinks/1
```

---

## Example JSON Response

When you call `GET /drinks`, the response looks like:

```json
{
  "drinks": [
    {
      "name": "Lemonade",
      "description": "Fresh citrus drink"
    }
  ]
}
```

When you add a drink, you may get:

```json
{
  "id": 1
}
```

---

## How This API Works

The basic flow of a Flask API is:

1. Create app
2. Connect to a database
3. Create a model
4. Define endpoints
5. Accept JSON requests
6. Save or read data from the database
7. Return JSON responses

This is a classic pattern for building small web APIs.

---

## Common Beginner Concepts Used Here

### Flask

Flask is a lightweight Python web framework used to build APIs and web apps.

### SQLAlchemy

SQLAlchemy helps you work with databases using Python objects and queries instead of writing raw SQL manually.

### SQLite

SQLite is a lightweight database that stores data in a file, which makes it perfect for learning and simple projects.

### REST API

REST APIs expose resources through URLs, and clients communicate using HTTP methods such as:

- `GET`
- `POST`
- `DELETE`

---

## Best Practices for Building This Kind of API

- Use environment variables for sensitive data
- Validate request data before saving it
- Add proper error handling
- Use database migrations for production projects
- Add authentication for real-world APIs
- Use a proper production database like PostgreSQL or MySQL
- Add tests for each endpoint

---

## Why This Project Is Useful

This project is a great starting point for learning:

- Python backend development
- REST API design
- database modeling
- database interaction with SQLAlchemy
- basic CRUD operations

---

## Next Steps

Once you understand this project, you can extend it by adding:

- a `PUT` method to update a drink
- user login/authentication
- categories or ingredients
- search filters
- pagination
- tests with pytest
- deployment to Render, Heroku, Azure, or Railway

---

## Summary

This Beverage API shows the basic building blocks of a minimal CRUD API in Python. It is intentionally simple, making it ideal for learning how Flask and SQLAlchemy work together.


---

## Quick Start

```bash
cd "Documents/Git Hub/BeverageAPI"
python -m venv venv
source venv/bin/activate
pip install -r api/requirements.txt
python -c "from api.application import app, db; app.app_context().push(); db.create_all()"
export FLASK_APP=api/application.py
flask run
```

Then open:

```text
http://127.0.0.1:5000/drinks
```

---
