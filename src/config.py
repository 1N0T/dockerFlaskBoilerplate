# Clases para la configuración de la aplicación.

class Config(object):
    pass

class ProConfig(object):
    pass

class DevConfig(object):
    DEBUG = True
    SQLALCHEMY_DATABASE_URI = "sqlite:///database.db"
    SQLALCHEMY_ECHO = True
    