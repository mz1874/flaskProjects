from flask import Blueprint

admin_view = Blueprint('admin', __name__)

@admin_view.route('/admin')
def index():
    return 'I am Admin';
