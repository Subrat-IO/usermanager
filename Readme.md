# 📘 User Manager — Flask + MySQL Application

This project is a simple **User Management System** built using **Flask** and **MySQL**.  
It demonstrates backend development concepts such as routing, database connectivity, CRUD operations, use of virtual environments, and Docker-based database setup.

---

## 🚀 Getting Started

Follow these steps to set up and run the application locally.

---

## 🔧 1. Project Setup

### Clone the repository
```bash
git clone https://github.com/Subrat-IO/usermanager.git
cd usermanager
```

### Create and activate a virtual environment
```bash
python3 -m venv venv
source venv/bin/activate
```

### Install dependencies
```bash
pip install -r requirements.txt
```

If you don’t have a `requirements.txt`, install manually:
```bash
pip install flask mysql-connector-python
```

---

## 🐳 2. Setting Up MySQL Using Docker

Start MySQL container:
```bash
docker run -d \
  --name mysql \
  -e MYSQL_ROOT_PASSWORD=Subrat@123 \
  -e MYSQL_DATABASE=users \
  -p 3306:3306 \
  mysql:latest
```

This creates:
- Username: **root**
- Password: **Subrat@123**
- Database: **users**

---

## 🏗️ 3. Database Schema

### Connect to MySQL
```bash
docker exec -it mysql mysql -u root -p
```

Password:
```
Subrat@123
```

### Create the required `users` table
```sql
USE users;

CREATE TABLE users (
    id INT AUTO_INCREMENT PRIMARY KEY,
    name VARCHAR(100),
    email VARCHAR(150),
    role VARCHAR(100)
);
```

### Insert sample data
```sql
INSERT INTO users (name, email, role) VALUES
('John Doe', 'john@example.com', 'Admin'),
('Jane Smith', 'jane@example.com', 'Editor'),
('Mike Ross', 'mike@example.com', 'Viewer');
```

---

## ▶️ 4. Running the Application

Start the Flask app:
```bash
python app.py
```

### Application URLs

| Feature | URL |
|---------|-----|
| View all users | http://localhost:5000/users |
| Add user | http://localhost:5000/new_user |
| User details | http://localhost:5000/users/<id> |

---

## 📦 Dependencies

The main dependencies used are:

- Python 3.10+
- Flask
- mysql-connector-python
- Docker (for running MySQL)

Install missing packages:
```bash
pip install <package-name>
```

---

## 🌿 Git Workflow & Contribution Guide

### Initialize Git
```bash
git init
```

### Create branch named `assignment`
```bash
git checkout -b assignment
```

### Commit your work
```bash
git add .
git commit -m "Implemented Flask API and MySQL setup"
```

### Add remote GitHub repository
```bash
git remote add origin https://github.com/Subrat-Io/usermanager.git
```

### Push the branch
```bash
git push -u origin assignment
```

### Create Pull Request
On GitHub → **Pull Requests → New Pull Request**

- Base branch: **main**
- Compare branch: **assignment**

---

## ✔ Contribution Rules

- Do not commit directly to `main`
- Always create a feature branch
- Keep commits meaningful
- Submit a pull request for review before merging

---

## 📄 License

This project is for educational and assignment purposes.  
Feel free to modify or extend it.

