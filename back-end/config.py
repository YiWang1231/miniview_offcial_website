import os
from dotenv import load_dotenv

base_dir = os.path.abspath(os.path.dirname(__file__))
load_dotenv(os.path.join(base_dir, '.env'))

# 设置数据库域名及端口
DOMAIN_NAME = 'root@localhost'
PORT = '3306'


class Config(object):
    SQLALCHEMY_DATABASE_URI = 'mysql + pymysql://' + DOMAIN_NAME + ':' + PORT + '/offcial_website?charset=utf8'
    SQLALCHEMY_TRACK_MODIFICATIONS = False