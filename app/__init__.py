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
    version='0.2.5',
    description='Dnon Official API Document.',
    contact='anteater1056@gmail.com'
)

api.add_namespace(user_ns, path='/user')
api.add_namespace(auth_ns, path='/auth')
api.add_namespace(channel_ns, path='/ch')
api.add_namespace(save_ns, path='/saved-info')