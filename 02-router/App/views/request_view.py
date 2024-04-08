from flask import Blueprint, request, render_template, jsonify, make_response, redirect, url_for

request_view = Blueprint('request', __name__)

"""
This controller is used for test request
    url 完整的
    去掉GET参数的base_url
    只有主机和端口号的host_url
    path 路由中的路径
    method 请求方法
    remote addr 请求的客户端地址
    GET请求参数args
    form PoST请求参数
    文件上传files
    请求头headers
    请求中的cookie
"""


@request_view.route('/request', methods=['GET', 'POST'])
def index():
    # 获取请求方式
    print(request.method)

    # ImmutableMultiDict([('SSS', 'SS')]), 可以出现重复的key
    # request.args.get('')
    print(request.args)
    # 如果传递的是多个参数的话，那么会优先获取第一个
    print(request.args.get("SSS"))
    print(request.args.getlist("SSS"))

    # 使用与GET相同的方式， From 用来解析 表单数据
    print(request.form)
    # 如果使用的是JSON的话则需要使用request.json
    print(request.json)

    # key1=value1; key2=value2 Cookie
    print(request.cookies)
    print("request.path:", request.path)
    print("request.remote_addr:", request.remote_addr)
    print("request.url:", request.url)
    print("request.base_url:", request.base_url)
    print("request.file:", request.files)
    print("request.headers:", request.headers)

    return "success"


@request_view.route("/response")
def response():
    # 返回字符串
    return "Hello world"


@request_view.route("/response/template")
def response_template():
    # 返回字符串
    return render_template("index.html")


@request_view.route("/response/json")
def response_json():
    # 返回字符串
    data = {'name': "张三"}
    return jsonify(data)


@request_view.route("/response/personalized")
def personalized_response():
    # 模板解析在这一步已经完成了
    html = render_template("index.html", name="张三");
    resp = make_response(html, 200)
    return resp


########################################################### 重定向开始#################################################################################

# 有意思的是， 不要使用redirect作为关键字再调用 redirect function
@request_view.route("/redirect")
def redirect_test():
    return redirect("https://www.baidu.com");


# 跳转到当前程序中存在的路由参数上
@request_view.route("/redirect2")
def redirect_test2():
    # 并不是直接跳转，而是重新进入视图函数
    return redirect("/response/personalized");


@request_view.route("/main/<name>")
def main_test(name):
    return render_template("index.html", name=name)


@request_view.route("/redirect3")
def redirect_test3():
    # 注释掉的为基础使用的URL-FOR,

    # ret = url_for('request.redirect_test')
    # print(ret)

    # url for 可以被用来传递参数
    ret = url_for('request.main_test', name = "wo")
    return redirect(ret)
