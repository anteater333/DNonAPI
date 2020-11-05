from flask_restx import Api
from flask import Blueprint

from .main.controller.user_controller import api as user_ns
from .main.controller.auth_controller import api as auth_ns
from .main.controller.channel_controller import api as channel_ns
from .main.controller.saved_controller import api as save_ns

blueprint = Blueprint('api', __name__)

api = Api(
    blueprint,
    title='DNon API Server',
    version='0.0.1',
    description='600억 대작 게임 DNon의 API 서버입니다. 보안상의 틈이 존재하지 않습니다.',
    contact='anteater1056@gmail.com'
)

api.add_namespace(user_ns, path='/user')
api.add_namespace(auth_ns, path='/auth')
api.add_namespace(channel_ns, path='/ch')
api.add_namespace(save_ns, path='/saved-info')