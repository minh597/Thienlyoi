from flask import Flask, jsonify, request

app = Flask(__name__)

@app.route("/")
def home():
    return jsonify({
        "message": "API Thienlyoi đang chạy ngon trên Vercel!",
        "status": "success",
        "author": "minh597"
    })

@app.route("/api/test")
def test():
    name = request.args.get("name", "bạn")
    return jsonify({"msg": f"Chào {name} từ Thienlyoi API!"})

# Quan trọng: Vercel yêu cầu có hàm này
def handler(environ, start_response):
    return app(environ, start_response)

if __name__ == "__main__":
    app.run()
