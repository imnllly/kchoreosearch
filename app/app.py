from flask import Flask
from routes import main
from config import SECRET_KEY

app = Flask(__name__)
app.secret_key = SECRET_KEY
app.register_blueprint(main)


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=80, debug=True)