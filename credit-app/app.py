from flask import Flask
import socket

app = Flask(__name__)

@app.route("/")
def home():
    hostname = socket.gethostname()

    return f"""
    <!DOCTYPE html>
    <html>
    <head>
        <title>SWE40006 Task 4.2</title>
        <style>
            body {{
                font-family: Arial, sans-serif;
                background-color: #f4f6f8;
                padding: 40px;
            }}

            .container {{
                max-width: 700px;
                margin: auto;
                background: white;
                padding: 30px;
                border-radius: 10px;
                box-shadow: 0 4px 12px rgba(0,0,0,0.1);
            }}

            h1 {{
                color: #222;
            }}

            .status {{
                color: green;
                font-weight: bold;
            }}
        </style>
    </head>

    <body>
        <div class="container">
            <h1>SWE40006 Docker Deployment</h1>

            <p><strong>Task:</strong> Task 4.2 - Credit</p>
            <p><strong>Application:</strong> Python Flask Web Application</p>
            <p><strong>Deployment Platform:</strong> Docker</p>
            <p><strong>Status:</strong> <span class="status">Running Successfully</span></p>
            <p><strong>Container Hostname:</strong> {hostname}</p>
        </div>
    </body>
    </html>
    """

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
