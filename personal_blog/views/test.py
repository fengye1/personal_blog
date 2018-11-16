# coding=utf8

from flask import Blueprint

test_bp = Blueprint('/text', __name__)


@test_bp.route('/')
def index():
    return "测试成功"
