import datetime

from flask import Blueprint, request, render_template, jsonify, make_response, redirect, url_for, session


session_view = Blueprint('session_view', __name__)

@session_view.route("/session/login", methods=["POST", 'GET'])
def login():
    if request.method == 'GET':
        return render_template("session/login.html")
    elif request.method == 'POST':
        print("进入")
        username = request.form.get("user_name")
        password = request.form.get("pass_word")
        if username == "admin" and password == "admin":
            resp = redirect("/session/home")
            # 这里登录成功后使用用户id作为session key
            session['user'] = username
            # 不要设置session为永久性的
            session.permanent = False

            return resp
        else:
            return "登录失败"
    return "Un Support method"


@session_view.route("/session/home", methods=["POST", 'GET'])
def home():
    username=session.get("user")
    return render_template("session/home.html", user_name=username)


@session_view.route("/session/logout", methods=["POST", 'GET'])
def logout():
    session.pop('user')
    resp = redirect("/session/home")
    return resp