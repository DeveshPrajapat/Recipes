📌 Project Overview

This is a Django-based Recipe Management System that allows users to create, view, and manage recipes. The project is built using Django 5.1.7 and follows standard Django project structure and best practices. It is suitable for learning, practice, and portfolio use.

🚀 Features

Add new recipes

View recipe list

Recipe detail pages

Django Admin Panel

Secure and scalable backend

Clean and modular project structure

🛠️ Tech Stack

Backend: Python, Django

Database: SQLite (default Django database)

Frontend: HTML, CSS (Django Templates)

Environment: Python Virtual Environment

📦 Python Packages Used

The project uses the following dependencies:

asgiref==3.8.1
Django==5.1.7
sqlparse==0.5.3
tzdata==2025.2

📂 Project Structure
📁 recipe-project
│── manage.py
│── recipe/
│   ├── settings.py
│   ├── urls.py
│   ├── wsgi.py
│   ├── asgi.py
│── templates/
│── static/
│── db.sqlite3
│── README.md

⚙️ Virtual Environment Setup
1️⃣ Create Virtual Environment
python -m venv venv

2️⃣ Activate Virtual Environment
# Windows
venv\Scripts\activate

# Linux / Mac
source venv/bin/activate

3️⃣ Install Dependencies
pip install Django==5.1.7 asgiref==3.8.1 sqlparse==0.5.3 tzdata==2025.2


(Optional: you can also use requirements.txt)

🗄️ Database Migration
python manage.py migrate

👤 Create Superuser (Optional)
python manage.py createsuperuser

▶️ Run the Project
python manage.py runserver


Open in browser:

http://127.0.0.1:8000/

🧪 Testing

Add recipes through the admin panel

View and manage recipes through the UI

Verify database operations using Django ORM

🔮 Future Enhancements

User authentication

Recipe categories & tags

Image upload for recipes

REST API using Django REST Framework

Responsive UI

👨‍💻 Author

Devesh Prajapat

GitHub: DeveshPrajapat

📄 License

This project is developed for educational and learning purposes.
