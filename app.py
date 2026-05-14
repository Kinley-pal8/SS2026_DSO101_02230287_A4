from flask import Flask, jsonify, request

app = Flask(__name__)

@app.route('/')
def home():
    return jsonify({"message": "Welcome to the CI/CD Pipeline Demo"}), 200

@app.route('/api/status')
def status():
    return jsonify({"status": "Application is running"}), 200

@app.route('/api/add', methods=['GET'])
def add():
    try:
        a = int(request.args.get('a', 0))
        b = int(request.args.get('b', 0))
        return jsonify({"result": a + b}), 200
    except ValueError:
        return jsonify({"error": "Invalid parameters"}), 400

@app.route('/api/add/<int:a>/<int:b>')
def add_path(a, b):
    return jsonify({"result": a + b}), 200

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5000)
