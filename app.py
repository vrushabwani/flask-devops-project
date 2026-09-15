from flask import Flask, jsonify
import os
import socket
from datetime import datetime, timezone

app = Flask(__name__)

@app.get("/")
def home():
    return jsonify({
        "application": "Flask DevOps Application",
        "message": "Application is running",
        "hostname": socket.gethostname(),
        "environment": os.getenv("APP_ENV", "development"),
        "timestamp": datetime.now(timezone.utc).isoformat()
    })

@app.get("/health")
def health():
    return jsonify({"status": "healthy"})

@app.get("/api/info")
def info():
    return jsonify({
        "python": "Flask",
        "container_ready": True,
        "devops_ready": True
    })

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=int(os.getenv("PORT", "5000")))
