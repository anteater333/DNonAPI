import datetime

from app.main.model.savedinfo import SavedInfo, Coordinate
from app.main.model.counter import Counter

from pymodm.errors import DoesNotExist, ValidationError
from pymongo.errors import DuplicateKeyError

def save_game_progress(data):
    if data['signed'] == True:  # Saving action for signed user
        
    else:                       # for guest user (who doesn't have our service account)