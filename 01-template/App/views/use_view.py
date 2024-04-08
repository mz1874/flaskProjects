from flask import Blueprint
from App.models.user_model import *

user_view = Blueprint('user', __name__)


@user_view.route('/')
def index():
    return 'Hello, World!'
