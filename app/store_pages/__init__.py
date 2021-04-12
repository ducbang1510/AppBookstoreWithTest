from flask import Blueprint
store_pages_blueprint = Blueprint('store_pages', __name__, template_folder='templates')

from . import routes