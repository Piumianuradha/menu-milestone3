from flask import render_template
from partymenu import app, db
from partymenu.models import Category, Task


@app.route("/")
def home():
    return render_template("tasks.html")