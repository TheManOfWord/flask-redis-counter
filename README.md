# 🐳 Flask + Redis Counter App (Beginner-Friendly Docker Project)

This is a simple project for beginners to learn how to use **Docker** and **Docker Compose**. It includes a basic **Flask** web application that uses **Redis** to store the number of times a page has been visited.

---

## Why This Project?

- **Learn Docker Compose basics:** Run multiple containers (web app + Redis) with a single command.  
- **Understand Flask and Redis integration:** Learn how a Python web app interacts with an in-memory data store.  
- **Practice containerization:** Get hands-on with Dockerfiles, Docker Compose, and managing multi-container apps.

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


## Prerequisites

- Install [Docker](https://docs.docker.com/get-docker/)  
- Install [Docker Compose](https://docs.docker.com/compose/install/)

---

## How to Run

1. Clone this repo:

   ```bash
   git clone https://github.com/TheManOfWord/flask-redis-counter.git
   cd flask-redis-counter

2. Build and start containers:

docker compose up --build

---

## How It Works

The Flask app serves a simple webpage that displays the current count.

The count value is stored in Redis, an in-memory key-value store, which persists between container restarts.

Docker Compose manages two services:

web: Flask app container

redis: Redis server container

The services communicate over a Docker network created automatically.


