"""
This file contains all the routes for the website
"""
from flask import Blueprint, render_template
from flask_login import login_required, current_user

# Setsup the blueprint for the app
views = Blueprint("views", __name__)

@views.route("/")
@login_required
def home():
    return render_template("home.html", user = current_user)

