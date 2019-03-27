#! coding=utf8

"""
主页视图模块

Created on 2010-01-29 by Varwey
"""

from flask import Blueprint

frontend_bp = Blueprint('frontend', __name__, static_folder='static', template_folder='templates')


@frontend_bp.route("/")
def index():

    return "index"

