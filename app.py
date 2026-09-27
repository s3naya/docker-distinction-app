from flask import Flask
import os

app = Flask(__name__)

APP_NAME = os.getenv("APP_NAME", "Docker Deployment Dashboard")
APP_ENV = os.getenv("APP_ENV", "development")

@app.route("/")
def home():
    return f"""
    <!DOCTYPE html>
    <html>
    <head>
        <title>{APP_NAME}</title>
        <style>
            body {{
                font-family: Arial, sans-serif;
                background: #f4f6f8;
                margin: 0;
                padding: 50px;
                text-align: center;
            }}
            .container {{
                max-width: 700px;
                margin: auto;
                background: white;
                padding: 40px;
                border-radius: 12px;
                box-shadow: 0 4px 15px rgba(0,0,0,0.1);
            }}
            h1 {{
                margin-bottom: 10px;
            }}
            .status {{
                display: inline-block;
                padding: 10px 20px;
                border-radius: 20px;
                background: #e8f5e9;
                color: #2e7d32;
                font-weight: bold;
            }}
            .info {{
                margin-top: 30px;
                text-align: left;
                line-height: 1.8;
            }}
        </style>
    </head>
    <body>
        <div class="container">
            <h1>{APP_NAME}</h1>
            <div class="status">Container Running Successfully</div>

            <div class="info">
                <p><strong>Application:</strong> {APP_NAME}</p>
                <p><strong>Environment:</strong> {APP_ENV}</p>
                <p><strong>Deployment:</strong> Docker Container</p>
                <p><strong>Status:</strong> Operational</p>
            </div>
        </div>
    </body>
    </html>
    """

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)