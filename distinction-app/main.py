import os
import socket

from fastapi import FastAPI
from fastapi.responses import HTMLResponse

APP_NAME = os.getenv("APP_NAME", "SWE40006 Task 4 Distinction")
APP_ENV = os.getenv("APP_ENV", "Development")
APP_VERSION = os.getenv("APP_VERSION", "1.0.0")

app = FastAPI(title=APP_NAME)

@app.get("/", response_class=HTMLResponse)
def home():
    hostname = socket.gethostname()

    return f"""
    <!DOCTYPE html>
    <html>
    <head>
        <title>{APP_NAME}</title>
        <style>
            body {{
                font-family: Arial, sans-serif;
                background-color: #f4f6f8;
                margin: 0;
                padding: 40px;
            }}
            .container {{
                max-width: 800px;
                margin: auto;
                background: white;
                padding: 35px;
                border-radius: 12px;
                box-shadow: 0 4px 14px rgba(0,0,0,0.10);
            }}
            h1 {{
                margin-top: 0;
                color: #222;
            }}
            .item {{
                margin: 14px 0;
                font-size: 17px;
            }}
            .status {{
                color: green;
                font-weight: bold;
            }}
            .badge {{
                display: inline-block;
                background: #eeeeee;
                padding: 5px 10px;
                border-radius: 6px;
            }}
        </style>
    </head>
    <body>
        <div class="container">
            <h1>Docker Deployment Dashboard</h1>
            <div class="item"><strong>Unit:</strong> SWE40006 Software Deployment and Evolution</div>
            <div class="item"><strong>Task:</strong> Task 4.3 - Distinction</div>
            <div class="item"><strong>Application:</strong> {APP_NAME}</div>
            <div class="item"><strong>Environment:</strong> <span class="badge">{APP_ENV}</span></div>
            <div class="item"><strong>Version:</strong> {APP_VERSION}</div>
            <div class="item"><strong>Container Hostname:</strong> {hostname}</div>
            <div class="item"><strong>Status:</strong> <span class="status">Running Successfully</span></div>
        </div>
    </body>
    </html>
    """

@app.get("/health")
def health():
    return {
        "status": "healthy",
        "application": APP_NAME,
        "environment": APP_ENV,
        "version": APP_VERSION
    }

@app.get("/about")
def about():
    return {
        "unit": "SWE40006 Software Deployment and Evolution",
        "task": "Task 4.3 Distinction",
        "platform": "Docker",
        "hostname": socket.gethostname()
    }
