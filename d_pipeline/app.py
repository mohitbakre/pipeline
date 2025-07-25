# app.py
from flask import Flask, jsonify
import os

app = Flask(__name__)

# Get environment variable for a customizable message, default to "World"
GREETING_TARGET = os.environ.get("GREETING_TARGET", "World")


@app.route('/')
def hello_world():
    """
    Returns a simple 'Hello, [GREETING_TARGET]!' message.
    """
    return f"Hello, {GREETING_TARGET}!"


@app.route('/healthz')
def health_check():
    """
    Health check endpoint for monitoring.
    """
    return jsonify({"status": "healthy"}), 200


@app.route('/metrics')
def metrics():
    """
    Simple metrics endpoint (placeholder for Prometheus).
    In a real app, you'd use a library like Prometheus client.
    """
    # Example of a simple metric
    return "app_requests_total 1\n", 200, {'Content-Type': 'text/plain'}


if __name__ == '__main__':
    # When running locally without Gunicorn/WSGI server
    # In production (Docker/Cloud Run), a WSGI server like Gunicorn will be used.
    app.run(host='0.0.0.0', port=int(os.environ.get('PORT', 8080)))
