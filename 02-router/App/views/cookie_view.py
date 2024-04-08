import datetime

from flask import Blueprint, request, render_template, jsonify, make_response, redirect, url_for

cookie_view = Blueprint('user_cookie', __name__)


@cookie_view.route("/login", methods=["POST", 'GET'])
def login():
    if request.method == 'GET':
        return render_template("cookie/login.html")
    elif request.method == 'POST':
        username = request.form.get("user_name")
        password = request.form.get("pass_word")
        if username == "admin" and password == "admin":
            resp = redirect("/home")
            # 浏览器关闭 cookie自动失效
            resp.set_cookie("user", username, max_age=3600)
            # 设置固定时间
            # resp.set_cookie("user", username, expires=datetime.datetime(2024,12,12))
            return resp
        else:
            return "登录失败"
    return "Un Support method"


@cookie_view.route("/home", methods=["POST", 'GET'])
def home():
    # 获取user cookie
    cookie = request.cookies.get("user")
    return render_template("cookie/home.html", user_name=cookie)


@cookie_view.route("/logout", methods=["POST", 'GET'])
def logout():
    cookie = request.cookies.get('user')
    resp = redirect("/home")
    resp.delete_cookie('user')
    return resp

