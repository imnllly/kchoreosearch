from flask import *

app = Flask(__name__)

@app.route('/')

def index():


    return render_template("kchoreosearch.html")


app.run(debug=True)