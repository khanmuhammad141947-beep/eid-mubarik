import os

class config:
    SQLALCHEMY_TRACK_MODIFICATIONS = True

    # Session Security
    SESSION_COOKIE_SECURE = True         # HTTPS me hi cookie send hogi
    SESSION_COOKIE_HTTPONLY = True       # JS se access nahi ho sakti
    SESSION_COOKIE_SAMESITE = 'Lax'      # CSRF attacks se protection