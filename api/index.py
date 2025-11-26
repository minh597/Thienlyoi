from flask import Flask, jsonify
from flask import Request  # cho Vercel Serverless Adapter

app = Flask(__name__)

@app.route("/")
def home():
    return jsonify({"message": "Hello from Flask on Vercel!"})

# Vercel sẽ dùng WSGI adapter
from flask import _request_ctx_stack
def handler(request: Request):
    with app.app_context():
        return app.full_dispatch_request()
