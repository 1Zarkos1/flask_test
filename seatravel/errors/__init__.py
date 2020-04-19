from flask import Blueprint

bp = Blueprint('errors', __name__)

from seatravel.errors import handlers