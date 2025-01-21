from flask import Flask, render_template
from markupsafe import escape
app = Flask(__name__)


@app.route("/app")  
def hello():
    return render_template("index.html")

