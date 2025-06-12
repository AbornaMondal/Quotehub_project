# Quotehub_project
# 🚀 QuoteHub

QuoteHub is a fun full-stack Docker application showcasing the use of **Dockerfiles**, **Docker Compose**, **Docker Swarm**, and **GitHub Actions CI/CD**.

## 🧰 Tech Stack
- **Backend**: Python Flask API providing random quotes
- **Frontend**: Static HTML page using JavaScript
- **Docker**: Containerization for both services
- **Docker Swarm**: Container orchestration
- **GitHub Actions**: CI/CD pipeline to build, push, and deploy

---

## 📁 Project Structure
quotehub/
├── backend/ # Flask API
│ ├── app.py
│ ├── requirements.txt
│ └── Dockerfile
├── frontend/ # Static frontend
│ ├── index.html
│ └── Dockerfile
├── docker-compose.yml # For local development
├── swarm-deploy.yml # Swarm deployment config
├── .github/
│ └── workflows/
│ └── ci-cd.yml # GitHub Actions CI/CD pipeline


---

## 🏗️ Setup Instructions

### 🔧 Local Development with Docker Compose

```bash
git clone https://github.com/yourusername/quotehub.git
cd quotehub
docker-compose up --build
Frontend: http://localhost:8080

Backend API: http://localhost:5000/quote

⚙️ Deploy with Docker Swarm
bash
Copy
Edit
# Initialize swarm if not already done
docker swarm init

# Deploy stack
docker stack deploy -c swarm-deploy.yml quotehub
🔄 GitHub Actions CI/CD
On every push to the main branch:

Builds and pushes Docker images for both backend and frontend

Deploys the latest stack to a Docker Swarm server over SSH

🔐 Required GitHub Secrets
DOCKER_USERNAME

DOCKER_PASSWORD

SWARM_HOST

SSH_USER

SSH_KEY

🧪 Optional Enhancements
Add tests for backend API
Use NGINX reverse proxy for /api/quote
Add Prometheus + Grafana monitoring
Extend API with categories or authors

