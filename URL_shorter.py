from flask import Flask, render_template, request, redirect, url_for
from flask_sqlalchemy import SQLAlchemy
import string
import random

app = Flask(__name__)

# Database configuration
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///urls.db"
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False

db = SQLAlchemy(app)


# Database Model
class URL(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    original_url = db.Column(db.String(500), nullable=False)
    short_code = db.Column(db.String(10), unique=True, nullable=False)


# Generate random short code
def generate_short_code(length=6):
    characters = string.ascii_letters + string.digits

    while True:
        code = ''.join(random.choices(characters, k=length))

        existing_url = URL.query.filter_by(short_code=code).first()

        if not existing_url:
            return code


# Home page
@app.route("/", methods=["GET", "POST"])
def index():

    if request.method == "POST":

        original_url = request.form.get("url")

        if not original_url:
            return render_template(
                "index.html",
                error="Please enter a URL."
            )

        # Check if URL already exists
        existing_url = URL.query.filter_by(
            original_url=original_url
        ).first()

        if existing_url:
            short_url = url_for(
                "redirect_to_url",
                short_code=existing_url.short_code,
                _external=True
            )

            return render_template(
                "result.html",
                short_url=short_url,
                original_url=original_url
            )

        # Generate short code
        short_code = generate_short_code()

        new_url = URL(
            original_url=original_url,
            short_code=short_code
        )

        db.session.add(new_url)
        db.session.commit()

        short_url = url_for(
            "redirect_to_url",
            short_code=short_code,
            _external=True
        )

        return render_template(
            "result.html",
            short_url=short_url,
            original_url=original_url
        )

    return render_template("index.html")


# Redirect using short code
@app.route("/<short_code>")
def redirect_to_url(short_code):

    url = URL.query.filter_by(
        short_code=short_code
    ).first_or_404()
    return redirect(url.original_url)


# Create database
with app.app_context():
    db.create_all()


if __name__ == "__main__":
    app.run(debug=True)