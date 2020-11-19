from flask import Flask
from pymodm import connect
from flask_bcrypt import Bcrypt     # 암호화 관련 모듈
from flask_cors import CORS, cross_origin

from .config import config_by_name

flask_bcrypt = Bcrypt()

def create_app(config_name):
    app = Flask(__name__)
    app.config.from_object(config_by_name[config_name])

    # logger = logging.getLogger('werkzeug')
    # handler = logging.handlers.RotatingFileHandler(
    #     filename='./.svr/log_' + time.strftime('%Y-%m-%d-%H', time.localtime(time.time())) + '.log',
    #     mode='a', maxBytes=1024 * 1024)
    # logger.addHandler(handler)

    connect(app.config['MONGO_URI'])    # pymodm 사용 전에 반드시 호출

    flask_bcrypt.init_app(app)

    CORS(app)               # CORS 헤더 허용

    return app