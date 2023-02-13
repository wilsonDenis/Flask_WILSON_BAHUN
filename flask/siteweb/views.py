from flask import Blueprint, render_template, request, flash, jsonify
from flask_login import login_required
from .models import User

views = Blueprint('views', __name__)


@views.route('/', methods=['GET', 'POST'])
def home():
    user= User()
    if request.method == 'POST':
        email = request.form.get("email")
        firstName = request.form.get("firstName")
        password = request.form.get("password")
        password2 = request.form.get("password2")
        if len(email) < 6:
           flash("email doit contenir au moins 5 caractère", category="error")
        elif len(firstName) < 4:
            flash("le nom doit contenir au moins 3 caractère", category="error")
        elif len(password) < 7:
            flash("le mot de passe doit dépasser 7 caractère", category="error")
        elif password != password2:
            flash("le mot de passe ne correspond pas")
        else:
            user = User(email = email, username = firstName, password = password, password2 = password2)
            db.session.add(user)
            db.session.commit()
            flash("compte créé avec succès", category="success")
    return render_template("home.html", user = user)


