# 🐳 Flask + Redis Counter App (Beginner-Friendly Docker Project)

This is a simple project for beginners to learn how to use **Docker** and **Docker Compose**. It includes a basic **Flask** web application that uses **Redis** to store the number of times a page has been visited.

---

## 📚 What You’ll Learn

- How to containerize a Python Flask app
- How to use Docker Compose to run multiple services (Flask + Redis)
- How Docker networking works between containers

---

## 🧱 Project Structure

flask-redis-counter/
├── app/
│ ├── app.py
│ ├── Dockerfile
│ └── requirements.txt
├── docker-compose.yml
├── .gitignore
└── README.md


---

## 🚀 How to Run

### Prerequisites:
- Docker installed
- Docker Compose installed

### Steps:

```bash
git clone https://github.com/YOUR_USERNAME/flask-redis-counter.git
cd flask-redis-counter
docker compose up --build

