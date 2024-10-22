import os
class Config:
    SQLALCHEMY_DATABASE_URI = os.getenv('DATABASE_URL')
    SQLALCHEMY_TRACK_MODIFICATIONS = False
class DevelopmentConfig(Config):
    FLASK_DEBUG = True

class ProductionConfig(Config):
    FLASK_DEBUG = False