Coding Assessment Portal

A web-based application built to manage and conduct coding tests for students or job applicants. The platform supports multiple-choice questions and code-based problems, complete with login authentication, test-timing features, and result tracking.
---
![Python](https://img.shields.io/badge/Python-3.11-blue) 
![Django](https://img.shields.io/badge/Django-4.2-green)
![License](https://img.shields.io/badge/License-MIT-yellow.svg)

---

## 🚀 Features

- 👤 User registration and authentication
- 📝 Admin can create and manage tests
- 📄 Multiple-choice and coding questions support
- ⏱️ Timed assessments
- 📊 Score evaluation and result viewing
- 💡 Simple and clean user interface

---

## 🛠️ Tech Stack

- **Backend:** Python, Django
- **Frontend:** HTML, CSS, Bootstrap, JavaScript
- **Database:** SQLite
- **Authentication:** Django's built-in auth system

---

## 🔧 How to Run Locally

```bash
# Clone the repository
git clone https://github.com/KShivasai1/coding-assessment-portal.git
cd coding-assessment-portal

# Create a virtual environment (optional but recommended)
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate

# Install dependencies
pip install -r requirements.txt

# Apply migrations
python manage.py migrate

# Create superuser (for admin access)
python manage.py createsuperuser

# Start the development server
python manage.py runserver

📌 Default Admin Route

http://127.0.0.1:8000/admin/

📂 Folder Structure

├── portal/                 # Main Django app
│   ├── templates/          # HTML templates
│   ├── static/             # CSS, JS files
│   └── views.py            # View functions
├── manage.py
└── requirements.txt

📈 Future Enhancements

Add real-time code compiler integration
Support for PDF/CSV export of results
Email notifications for test invites
Timer auto-submit feature

👨‍💻 Developed By
Shivasai


