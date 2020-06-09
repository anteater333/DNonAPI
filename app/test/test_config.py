import os
import unittest

from flask import current_app   # 현재 실행 중인 app인듯
from flask_testing import TestCase

from manage import app
from app.main.config import basedir

class TestDevelopmentConfig(TestCase):
    def create_app(self):   # Flask_testing 공식 document에 따르면 create_app 메소드를 꼭 구현해야함.
        app.config.from_object('app.main.config.DevelopmentConfig')
        return app

    def test_app_is_development(self):
        # 센세가 가르쳐준 assert
        self.assertFalse(app.config['SECRET_KEY'] is 'FlaskAPI')     # 조건이 false인지 확인
        self.assertTrue(app.config['DEBUG'] is True)                   # 조건이 true인지 확인
        self.assertFalse(current_app is None)
        self.assertTrue(
            app.config['MONGO_URI'] == 'mongodb://127.0.0.1:27017/dnonDevDB'
        )   # 여러 줄에 나눠서

class TestTestingConfig(TestCase):
    def create_app(self):
        app.config.from_object('app.main.config.TestingConfig')
        return app

    def test_app_is_testing(self):
        self.assertFalse(app.config['SECRET_KEY'] is 'FlaskAPI')
        self.assertTrue(app.config['DEBUG'])
        self.assertTrue(
            app.config['MONGO_URI'] == 'mongodb://127.0.0.1:27017/flaskAPITest'
        )

class TestProductionConfig(TestCase):
    def create_app(self):
        app.config.from_object('app.main.config.ProductionConfig')
        return app

    def test_app_is_production(self):
        self.assertTrue(app.config['DEBUG'] is False)


if __name__ == '__main__':
    unittest.main()