from flask import Flask
from flask_cors import CORS

from config import Config

def create_app(config_class=Config):
    app = Flask(__name__)
    app.config.from_object(config_class)
    # 跨域配置
    CORS(app)
    """
    注册蓝图
    home: 首页
    """
    from app.api import home
    app.register_blueprint(home)
    return app