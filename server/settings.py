#-*- coding:utf-8 -*-

import datetime

DEBUG = True
SQLALCHEMY_DATABASE_URI = 'sqlite:///taski.db'
JSON_AS_ASCII = False
USE_X_SENDFILE = False
SESSION_COOKIE_PATH = None
SESSION_COOKIE_DOMAIN = None
SESSION_COOKIE_NAME = 'session'
LOGGER_NAME = __name__
SECRET_KEY = None
MAX_CONTENT_LENGTH = None
APPLICATION_ROOT = None
SERVER_NAME = None
PREFERRED_URL_SCHEME = 'http'
JSONIFY_PRETTYPRINT_REGULAR = True
TESTING = False
PERMANENT_SESSION_LIFETIME = datetime.timedelta(31)
PROPAGATE_EXCEPTIONS = None
TRAP_BAD_REQUEST_ERRORS = False
JSON_SORT_KEYS = True
SESSION_COOKIE_HTTPONLY = True
SEND_FILE_MAX_AGE_DEFAULT = 43200
PRESERVE_CONTEXT_ON_EXCEPTION = None
SESSION_COOKIE_SECURE = False
TRAP_HTTP_EXCEPTIONS = False