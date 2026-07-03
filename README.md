# 📝 FlaskBlog

## 📌 Project Description

The **FlaskBlog** is a modern blogging web application developed using **Flask**, **Flask-SQLAlchemy**, **Flask-Login**, **Bootstrap 5**, and **SQLite**. The application allows users to register, log in securely, create blog posts, edit or delete their own posts, manage their profile, and interact through comments. The project follows a modular Flask architecture using Blueprints and provides a clean, responsive, and user-friendly interface.

---

## 📚 Concepts Used

* Flask Framework
* Flask Blueprints
* Object-Oriented Programming (OOP)
* User Authentication & Authorization
* CRUD Operations
* SQLAlchemy ORM
* SQLite Database
* HTML5, CSS3 & Bootstrap 5
* Jinja2 Templating

---

## 🚀 Features

* ✔ User Registration 
* ✔ User Login & Logout 
* ✔ Secure User Authentication
* ✔ User Profile Management
* ✔ Create Blog Posts
* ✔ Edit and Delete Posts
* ✔ View All Blog Posts
* ✔ View Individual Post Details
* ✔ Add Comments on Posts
* ✔ Responsive User Interface
* ✔ Modern Gradient Design
* ✔ Modular Flask Project Structure
* ✔ Modular Flask Blueprints
* ✔ SQLite Database Integration

---

## 📁 Project Structure

```text
week8-flask-blog/

│── app/
│   │
│   ├── auth/
│   │   ├── __init__.py
│   │   ├── forms.py
│   │   └── routes.py
│   │
│   ├── comments/
│   │   ├── __init__.py
│   │   ├── forms.py
│   │   └── routes.py
│   │
│   ├── main/
│   │   ├── __init__.py
│   │   └── routes.py
│   │
│   ├── posts/
│   │   ├── __init__.py
│   │   ├── forms.py
│   │   └── routes.py
│   │
│   ├── static/
│   │   ├── css/
│   │   │   └── style.css
│   │   │
│   │   ├── images/
│   │   │   └── .gitkeep
│   │   │
│   │   └── js/
│   │       └── main.js
│   │
│   ├── __init__.py
│   └── models.py
│
│── instance/
│   └── blog.db
│
│── migrations/
│   ├── .gitkeep
│   └── README.md
│
│── templates/
│   ├── auth/
│   │   ├── login.html
│   │   └── register.html
│   │
│   ├── main/
│   │   ├── about.html
│   │   ├── home.html
│   │   └── profile.html
│   │
│   ├── posts/
│   │   ├── all_posts.html
│   │   ├── create_post.html
│   │   ├── edit_post.html
│   │   └── post_details.html
│   │
│   └── base.html
│
│── tests/
│   ├── __init__.py
│   └── test_app.py
│
│── .gitignore
│── config.py
│── README.md
│── requirements.txt
└── run.py
```

---

## 🛠 Technologies Used

* Python 3
* Flask
* Flask-SQLAlchemy
* Flask-Login
* Flask-WTF
* Flask-Migrate
* SQLite
* Bootstrap 5
* HTML5
* CSS3
* Jinja2
* VS Code

---

## ▶️ Installation & Execution

### Step 1: Install Required Libraries

```bash
pip install -r requirements.txt
```

### Step 2: Open Flask Shell

```bash
flask shell
```

### Step 3: Create the Database

```python
from app import create_app, db

app = create_app()

with app.app_context():
    db.create_all()
```

### Step 4: Exit Flask Shell

```python
exit()
```

### Step 5: Run the Application

```bash
python run.py
```

### Step 6: Open in Browser

```text
http://127.0.0.1:5000
```

---
---

## Project Objectives

- Learn Flask application development.
- Understand Flask Blueprints.
- Implement user authentication.
- Perform CRUD operations using SQLAlchemy.
- Manage relational databases with SQLite.
- Build a responsive web interface using Bootstrap.
- Organize a Flask project using a modular structure.

---

## 👨‍💻 Author

**Anurag**

B.Tech Computer Science & Engineering

D. Y. Patil International University