from flask import request
from flask_restx import Resource

from ..util.decorator import token_required, prove_yourself
from ..util.dto import SavedInfoDto
from ..service.saved_service import save_game_progress
from ..service.auth_helper import Auth

api = SavedInfoDto.api
_saving_info = SavedInfoDto.saving_info
_saved_info = SavedInfoDto.saved_info

@api.route('/')
class SavedInfo(Resource):
    @api.response(201, 'The game data saved successfully.')
    @api.doc('saves ongoing game data.')
    @api.expect(_saved_info, validate=True)
    def post(self):
        """Saves current game and leaves"""
        data = request.json

        if Auth.get_logged_in_user(request)[0].get('status') == 'success':
            data['signed'] = True
        else:
            data['signed'] = False
        
        return save_game_progress(data=data)

# @api.route('/<saveId>')
# @api.param('saveId', 'Unique identifier')
# class SignedSavedInfo(Resource):
#     @prove_yourself
#     def get(self):

# @api.route('/<saveId>/<guestPassword>')
# @api.param('saveId', 'Unique identifier')
# @api.param('guestPassword', 'One-time password that you got when saved the data')
# class GuestSavedInfo(Resource):
#     def get(self):