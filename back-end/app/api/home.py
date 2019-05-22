from flask import jsonify
from flask import Blueprint


# 创建蓝图
home = Blueprint('home', __name__)


@home.route('/', methods=['GET'])
def index():
    return jsonify("Welcome to miniview offcial website")