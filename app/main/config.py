import os, json

basedir = os.path.abspath(os.path.dirname(__file__))

with open('./secrets.json', 'r') as f:
    conn_info = json.load(f)

class Config:
    SECRET_KEY = conn_info['SECRET_KEY']    # KEY, jwt에 사용
    DEBUG = False


class DevelopmentConfig(Config):            # 개발버전 설정
    DEBUG = True
    ## DB 정보들 ##
    MONGO_URI = conn_info['DB_URL']

class TestingConfig(Config):                # 테스팅 설정
    DEBUG = True
    TESTING = True
    PRESERVE_CONTEXT_ON_EXCEPTION = False   # 예외 발생 시 컨텍스트 보존 여부
    ## DB 정보들 ##
    MONGO_URI = conn_info['DB_TEST_URL']

class ProductionConfig(Config):             # 배포판 설정
    DEBUG = False
    ## DB 정보들 ##
    MONGO_URI = conn_info['DB_URL']


config_by_name = dict(
    dev=DevelopmentConfig,
    test=TestingConfig,
    prod=ProductionConfig
)

key = Config.SECRET_KEY