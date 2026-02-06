from flask import Flask

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


if __name__ == "__main__":
    app.run(debug=True)
