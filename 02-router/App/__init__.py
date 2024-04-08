# App/__init__.py
import datetime

from flask import Flask
from App.views.use_view import user_view
from App.views.admin_view import admin_view
from App.views.request_view import request_view
from App.views.cookie_view import cookie_view
from App.views.session_view import session_view

def create_app():
    app = Flask(__name__)
    app.register_blueprint(user_view)
    app.register_blueprint(admin_view)
    app.register_blueprint(request_view)
    app.register_blueprint(cookie_view)
    app.register_blueprint(session_view)
    # 如果使用Session需要配置密钥

    # {'DEBUG': False,
    #  'TESTING': False,
    #  'PROPAGATE_EXCEPTIONS': None,
    #  'SECRET_KEY': None,
    #  'PERMANENT_SESSION_LIFETIME': datetime.timedelta(days=31),
    #  'USE_X_SENDFILE': False,
    #  'SERVER_NAME': None,
    #  'APPLICATION_ROOT': '/',
    #  'SESSION_COOKIE_NAME': 'session',
    #  'SESSION_COOKIE_DOMAIN': None,
    #  'SESSION_COOKIE_PATH': None,
    #  'SESSION_COOKIE_HTTPONLY': True,
    #  'SESSION_COOKIE_SECURE': False,
    #  'SESSION_COOKIE_SAMESITE': None,
    #  'SESSION_REFRESH_EACH_REQUEST': True,
    #  'MAX_CONTENT_LENGTH': None,
    #  'SEND_FILE_MAX_AGE_DEFAULT': None,
    #  'TRAP_BAD_REQUEST_ERRORS': None,
    #  'TRAP_HTTP_EXCEPTIONS': False,
    #  'EXPLAIN_TEMPLATE_LOADING': False,
    #  'PREFERRED_URL_SCHEME': 'http',
    #  'TEMPLATES_AUTO_RELOAD': None,
    #  'MAX_COOKIE_SIZE': 4093}

    print(app.config)
    app.config["SECRET_KEY"] = "www.bugcreator.org.cn"
    # 设置session失效日期
    app.config["PERMANENT_SESSION_LIFETIME"] = datetime.timedelta(seconds=5)
    return app
