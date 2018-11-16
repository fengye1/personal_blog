# coding=utf8

from flask import Blueprint, jsonify, request
from personal_blog.dao.account import dao_register_account
from personal_blog.utils.response_util import ajax_response

account_bp = Blueprint('account', __name__)


@account_bp.route('/login/', methods=['POST'])
def login():
    email = request.values.get("email")
    password = request.values.get("password")


@account_bp.route('/register/', methods=["POST"])
def register():
    name = request.values.get("name")
    email = request.values.get('email')
    password = request.values.get('password')
    res = ajax_response()
    user = dao_register_account(email, password, name)
    if not user:
        res.update({
            'status': 'fail',
            'msg': '邮箱已经被注册'
        })
    return jsonify(res)

