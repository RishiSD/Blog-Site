import os


class Config(object):
    SECRET_KEY = os.environ.get('SECRET_KEY',
                                'Z\xf0\xfb\xf0r\x8c\r\xa4\xc6Qf\xc2\x15\xcb')
    SIMPLEMDE_JS_IIFE = True
    SIMPLEMDE_USE_CDN = True
    SIGNUP_ENABLED = True
    MONGODB_DB = os.environ.get('MONGODB_DB', 'test')
    MONGODB_HOST = os.environ.get('MONGODB_HOST', '127.0.0.1')
    MONGODB_PORT = os.environ.get('MONGODB_PORT', 27017)
