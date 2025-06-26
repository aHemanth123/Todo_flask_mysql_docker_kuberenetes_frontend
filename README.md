# Todo Flask MySQL Docker Kubernetes Frontend

A simple To-Do web application built using Flask (Python) with a MySQL backend. This project containerizes the app using Docker and deploys it on Kubernetes for scalability.

---

## 🚀 Features

- Add, display, and manage tasks.
- Frontend built with HTML & CSS.
- Backend built using Flask.
- Persistent storage using MySQL.
- Containerized using Docker.
- Orchestrated using Kubernetes.

---

## 🛠️ Tech Stack

- **Frontend**: HTML, CSS  
- **Backend**: Python Flask  
- **Database**: MySQL  
- **Containerization**: Docker  
- **Orchestration**: Kubernetes  
- **Platform**: Linux  

---
## 📁 Project Structure

.
├── app/   
│   ├── static/   
│   │   └── style.css   
│   ├── templates/   
│   │   └── index.html  
│   ├── app.py   
│   └── requirements.txt   
├── k8s/   
│   ├── backend-deploy.yaml   
│   ├── backend-service.yaml   
│   ├── db-config.yaml   
│   ├── db-secret.yaml   
│   ├── mysql-deployment.yaml   
│   └── mysql-pv-pvc.yaml   
├── Dockerfile   
├── README.md   
└── Devops assignment3.odt   



 
---

## ⚙️ Setup Instructions (Linux)

### 1. Clone the Repo

```bash
git clone https://github.com/<your-username>/Todo_flask_mysql_docker_kubernetes_frontend.git
cd Todo_flask_mysql_docker_kubernetes_frontend
```

### 2. Build the Docker Image

docker build -t todo-flask-app .


### 3. Run Locally with Docker

docker run -p portno:portno  todo-flask-app

### 4. Kubernetes Deployment

kubectl apply -f k8s/

To check all resources:

kubectl get all

