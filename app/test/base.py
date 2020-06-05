from flask_testing import TestCase
from manage import app
from pymodm import connect, connection

class BaseTestCase(TestCase):
    """ Base Tests """

    def create_app(self):
        app.config.from_object('app.main.config.TestingConfig')
        connect(app.config['MONGO_URI'])
        return app

    def tearDown(self):
        collections = connection._get_db().collection_names()
        for collection in collections:
            connection._get_db()[collection].delete_many({})