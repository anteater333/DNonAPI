import os

basedir = os.path.abspath(os.path.dirname(__file__))


class Config:
    SECRET_KEY = os.getenv('SECRET_KEY', 'dnon_api')    # KEY, jwt에 사용
    DEBUG = False


class DevelopmentConfig(Config):            # 개발버전 설정
    DEBUG = True
    ## DB 정보들 ##
    MONGO_URI = 'mongodb://127.0.0.1:27017/dnonDevDB'

class TestingConfig(Config):                # 테스팅 설정
    DEBUG = True
    TESTING = True
    PRESERVE_CONTEXT_ON_EXCEPTION = False   # 예외 발생 시 컨텍스트 보존 여부
    ## DB 정보들 ##
    MONGO_URI = 'mongodb://127.0.0.1:27017/flaskAPITest'

class ProductionConfig(Config):             # 배포판 설정
    DEBUG = False


config_by_name = dict(
    dev=DevelopmentConfig,
    test=TestingConfig,
    prod=ProductionConfig
)

key = Config.SECRET_KEY