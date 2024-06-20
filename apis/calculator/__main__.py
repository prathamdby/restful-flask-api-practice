from flask import Flask
from .routes import calculator

app = Flask(__name__)
app.register_blueprint(calculator)

if __name__ == "__main__":
    app.run(debug=True)
