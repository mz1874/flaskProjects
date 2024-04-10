from flask import Blueprint,render_template
from App.models.user_model import *

user_view = Blueprint('user', __name__)


@user_view.route('/')
def index():
    data = {
        "name":"IKun",
        "age":22,
        "likes":['ball','sing', 'rap', 'basketball']
    }

    return render_template("index.html", **data)


@user_view.route('/home')
def home():
    data = {
        "name":"IKun",
        "age":22,
        "likes":['ball','sing', 'rap', 'basketball']
    }

    return render_template("home.html", **data)


@user_view.route('/base')
def base():
    return render_template("base.html")

@user_view.route('/child1')
def child1():
    return render_template("child1.html")
