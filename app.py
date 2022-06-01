from flask import Flask, flash, redirect, render_template, request
from flask_talisman import Talisman
from flask_sitemap import Sitemap
# Configure application
app = Flask(__name__)
ext = Sitemap(app=app)
app.config["SITEMAP_INCLUDE_RULES_WITHOUT_PARAMS"] = True
app.config["SITEMAP_URL_SCHEME"] = "https"

csp = {
    'default-src': [
        '\'self\'',
        '\'unsafe-inline\'',
        'stackpath.bootstrapcdn.com',
        'maxcdn.bootstrapcdn.com',
        'opinionstage.com/',
        'code.jquery.com',
        'cdn.jsdelivr.net',
        'w3.org'
    ],
    'frame-src': [
        "https://www.opinionstage.com/api/v1/widgets/1002786/iframe"
    ],
    'img-src': [
        '\'self\'',
        'https:',
        'data:'
    ]
}

Talisman(app, content_security_policy=csp)
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

if __name__ == "__main__":
    app.run(debug=True)
