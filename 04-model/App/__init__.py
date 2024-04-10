# App/__init__.py
from flask import Flask
from App.views.use_view import user_view
from App.views.admin_view import admin_view

def create_app():
    app = Flask(__name__)
    app.register_blueprint(user_view)
    app.register_blueprint(admin_view)
    return app
