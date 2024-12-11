from flask import Flask
from routes import main


app = Flask(__name__)
app.secret_key = 'ochko_xd'
app.register_blueprint(main)


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=80, debug=True)