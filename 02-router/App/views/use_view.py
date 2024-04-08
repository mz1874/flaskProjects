from flask import Blueprint
from App.models.user_model import *
import uuid

user_view = Blueprint('user', __name__)

@user_view.route('/')
def index():
    return 'Hello, World!'

@user_view.route("/user/<name>")
def print_name(name):
    print("调用")
    return name

@user_view.route("/user/<float:price>")
def print_float(price):
    return str(price)

"""
生成UUID
"""
@user_view.route("/uuid/get")
def get_uuid():
    return str(uuid.uuid1())

"""
获取之后的uuid需要和之前的匹配
"""
@user_view.route("/uuid/test/<uuid:uuid>")
def get_current_uuid(uuid):
    return str(uuid)


@user_view.route("/any/<any(apple,orange,banana):fruit>")
def get_any(fruit):
    return str(fruit)


#请求方式
@user_view.route("/testpost/", methods=['POST'])
def test_post():
    return "This IS POST FUNCTION"