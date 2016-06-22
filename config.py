import os
_basedir = os.path.abspath(os.path.dirname(__file__))

DEBUG = True
QUEUING = True

ADMINS = frozenset(['john.mille@ews-network.net'])
SECRET_KEY = '43e1ecdf2b2eb1ea633ec76d4ff94c29dd112557d442ee0130120df7b4d63a85'

# If you think those KEYS will help you with hacking something, Mr Cracker, unfortunately not.

THREADS_PER_PAGE = 8

CSRF_ENABLED = True
CSRF_SESSION_KEY = "43e1ecdf2b2eb1ea633ec76d4ff94c29dd112557d442ee0130120df7b4d63a85"

SQLALCHEMY_DATABASE_URI = "mysql://devuser:DevPassw0rd@10.30.4.22/dev_db"
