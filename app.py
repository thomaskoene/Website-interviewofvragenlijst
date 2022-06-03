from flask import Flask, flash, redirect, render_template, request
from flask_talisman import Talisman
from flask_sitemap import Sitemap
# Configure application
app = Flask(__name__)
ext = Sitemap(app=app)

app.config["SECRET_KEY"] = b"\xa1\x13Ll+\x88(\xa4\xcf\xaa\xd7\x97'*j"

@app.route("/")
@app.route("/homescreen")

@app.route("/", methods=["GET"])
def homescreen():
    """Shows homescreen"""
    return render_template("homescreen.html")

@app.route("/explanation/", methods=["GET"])
def explanation():
    """Shows explanation"""
    return render_template("explanation.html")

@app.route("/why/", methods=["GET"])
def why():
    """Shows why"""
    return render_template("why.html")

if __name__ == "__main__":
    app.run(debug=True)
