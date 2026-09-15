# Flask DevOps Project

A small ready-made Flask application for learning Python, Git/GitHub, Docker, GitHub Actions and AWS EC2.

## Endpoints

- `/` - application information
- `/health` - health check
- `/api/info` - DevOps information

## Run locally

```bash
python -m venv venv
```

Windows:
```powershell
venv\Scripts\activate
```

Linux/EC2:
```bash
source venv/bin/activate
```

Install:
```bash
pip install -r requirements.txt
```

Run:
```bash
python app.py
```

Open:
`http://127.0.0.1:5000`

## Run with Docker

```bash
docker build -t flask-devops-app .
docker run -d --name flask-devops-app -p 5000:5000 flask-devops-app
```

Open:
`http://localhost:5000`

Check:
```bash
docker ps
docker logs flask-devops-app
```

## Run with Docker Compose

```bash
docker compose up -d --build
```

Stop:
```bash
docker compose down
```

## Run tests

```bash
pytest -q
```

## EC2 deployment

Install:
```bash
sudo dnf install python3 python3-pip git -y
```

Clone your GitHub repository:
```bash
git clone YOUR_GITHUB_REPOSITORY_URL
cd flask-devops-project
```

Run:
```bash
python3 -m venv venv
source venv/bin/activate
pip install -r requirements.txt
python app.py
```

The application listens on `0.0.0.0:5000`.

For direct browser testing, allow TCP port 5000 in the EC2 Security Group and open:
`http://YOUR_EC2_PUBLIC_IP:5000`

## Learning path

1. Python and Flask
2. Git/GitHub
3. Docker
4. GitHub Actions CI
5. AWS EC2
6. CloudWatch
7. Production deployment with Nginx
