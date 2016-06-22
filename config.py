import os
_basedir = os.path.abspath(os.path.dirname(__file__))

DEBUG = True
QUEUING = True

ADMINS = frozenset(['john.mille@ews-network.net'])
SECRET_KEY = 's2ji3s14uF31Mqs63Yy2282GD2j9I2dHP89G216z2Z'

THREADS_PER_PAGE = 8

CSRF_ENABLED = True
CSRF_SESSION_KEY = "8325f63NGe4Qy61sOe421u074ZBTiN8D5AW195D635"
