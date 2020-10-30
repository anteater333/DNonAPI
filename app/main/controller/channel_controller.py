from flask import request
from flask_restx import Resource

from ..util.decorator import token_required
from ..util.dto import ChannelDto
# from ..service.user_service import save_new_user, get_all_users, get_a_user, delete_a_user
from ..service.channel_service import get_all_channels, save_new_channel

api = ChannelDto.api
_channel = ChannelDto.channel

@api.route('/')
class ChannelList(Resource):
    @api.doc('list_of_all_channels')
    @api.marshal_list_with(_channel, envelope='data')
    def get(self):
        """List all channels in server"""
        return get_all_channels()
    
    @api.response(201, 'A new channel has successfully been added.')
    @api.doc('create a new channel (Admin)')
    @api.expect(_channel, validate=True)
    def post(self):
        """Creates a new channel"""
        data = request.json
        return save_new_channel(data=data)