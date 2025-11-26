from flask import Flask, jsonify, request

app = Flask(__name__)

@app.route("/")
def home():
    return jsonify({"message": "Hello from Flask on Vercel 2025!"})

@app.route("/api/hello")
def hello():
    name = request.args.get("name", "bạn")
    return jsonify({"msg": f"Xin chào {name} từ serverless!"})

# Bắt buộc phải có hàm này cho Vercel serverless
def handler(environ, start_response):
    # Vercel sẽ gọi hàm này thay vì chạy Flask trực tiếp
    from flask import Flask
    return app(environ, start_response)

if __name__ == "__main__":
    app.run()
