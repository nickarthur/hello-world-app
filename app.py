from flask import Flask, jsonify, request
from datetime import datetime
import random

app = Flask(__name__)


@app.route("/")
def hello():
    return """<!DOCTYPE html>
<html>
<head><title>Hello</title></head>
<body style="display:flex;justify-content:center;align-items:center;height:100vh;margin:0">
  <h1>Hello, World!</h1>
</body>
</html>"""


@app.route("/api/time")
def get_time():
    """Returns current server time as JSON"""
    return jsonify({
        "timestamp": datetime.now().isoformat(),
        "timezone": "UTC"
    })


@app.route("/greet/<name>")
def greet_user(name):
    """Personalized greeting with URL parameter"""
    return f"""<!DOCTYPE html>
<html>
<head><title>Greeting</title></head>
<body style="display:flex;justify-content:center;align-items:center;height:100vh;margin:0;flex-direction:column">
  <h1>Hello, {name}!</h1>
  <p>Welcome to the app</p>
</body>
</html>"""


@app.route("/api/random")
def random_number():
    """Generate random number with optional min/max parameters"""
    min_val = int(request.args.get('min', 1))
    max_val = int(request.args.get('max', 100))
    return jsonify({
        "number": random.randint(min_val, max_val),
        "min": min_val,
        "max": max_val
    })


@app.route("/calculate/<operation>/<int:a>/<int:b>")
def calculate(operation, a, b):
    """Simple calculator endpoint"""
    operations = {
        "add": a + b,
        "subtract": a - b,
        "multiply": a * b,
        "divide": a / b if b != 0 else "Error: Division by zero"
    }
    result = operations.get(operation, "Invalid operation")
    return jsonify({
        "operation": operation,
        "operands": [a, b],
        "result": result
    })


@app.route("/api/echo", methods=["POST"])
def echo():
    """Echo back the JSON data sent in POST request"""
    data = request.get_json()
    return jsonify({
        "received": data,
        "timestamp": datetime.now().isoformat()
    })


if __name__ == "__main__":
    app.run(debug=True)
