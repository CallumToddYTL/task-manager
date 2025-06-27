# Task Manager Web Application

A Flask-based task management web app designed for individuals and small teams to manage tasks efficiently. It features secure login, role-based access, and full CRUD operations for Admin users.

## Features

- 🔒 Secure registration with password strength enforcement
- 🔐 Login and authentication
- 👥 Role-based access control (Admin/User)
- 📝 Task CRUD operations:
  - Admin: Create, Read, Update, Delete
  - User: Create, Read, Update
- 📊 Dashboard UI with Bootstrap
- 💡 Real-time feedback using Flask flash messages

## Live Demo

The application is deployed on AWS EC2 and accessible at:  
[http://13.51.150.160:5000](http://13.51.150.160:5000)

## Tech Stack

- Backend: Python, Flask, SQLAlchemy
- Frontend: HTML, CSS, Bootstrap, Jinja2
- Authentication: Flask-Login, Flask-WTF
- Database: SQLite
- Deployment: AWS EC2 (Ubuntu 20.04)

## Local Setup

```bash
git clone https://github.com/CallumToddYTL/task-manager.git
cd task-manager

# Create virtual environment
python -m venv venv

# Activate (Mac/Linux)
source venv/bin/activate

# Activate (Windows)
venv\Scripts\activate

# Install dependencies
pip install -r requirements.txt

# Run the app
flask run
```

## Development Approach (Agile)

This project followed an Agile development methodology using short sprints and user stories. Progress and task tracking were managed in ClickUp. Example user stories included:

- "As a user, I want to log in securely so that I can view my tasks"
- "As an admin, I want to delete any user's task to maintain task hygiene"

Regular iterations and peer feedback were used to refine the UI and logic.

## Known Issues

- No email verification yet
- No pagination for large task lists

## Future Improvements

- Add due dates and priority levels
- Implement search/filter functionality
