from flask import request
from flask_restx import Resource

from ..util.decorator import token_required, prove_yourself
from ..util.dto import SavedInfoDto
from ..service.saved_service import save_game_progress, load_guest_game_progress, load_user_game_progress
from ..service.auth_helper import Auth

api = SavedInfoDto.api
_saving_info = SavedInfoDto.saving_info
_saved_info = SavedInfoDto.saved_info

@api.route('/')
class SavedInfo(Resource):
    @api.response(201, 'The game data saved successfully.')
    @api.response(200, 'The data replaced to the latest.')
    @api.doc('saves ongoing game data.')
    @api.expect(_saving_info, validate=True)
    def post(self):
        """Saves current game and leaves"""
        data = request.json

        signed = Auth.get_logged_in_user(request)
        if signed[0].get('status') == 'success':
            data['guest'] = True
            data['userId'] = signed[0].get('data').get('userId')
        else:
            data['guest'] = False
        
        return save_game_progress(data=data)

@api.route('/<savedId>/<guestPassword>')
@api.param('savedId', 'Unique identifier')
@api.param('guestPassword', 'One-time password that you got when saved the data')
class GuestSavedInfo(Resource):
    @api.doc('get and delete the guest\'s saved game progress.')
    @api.marshal_with(_saved_info)
    def delete(self, savedId, guestPassword):
        saved_data = load_guest_game_progress(savedId, guestPassword)
        if not saved_data:
            api.abort(404, 'data not found')
        return saved_data