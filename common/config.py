from os.path import abspath, dirname, join
import web

import sys
reload(sys)
sys.setdefaultencoding('utf-8')

curdir = abspath(dirname(__file__))

# debug option
debug = True

# database settings
db_engine = 'mysql'
db_name = 'pycms'
db_user = 'www'
db_password = 'www'
db_host = 'localhost'

# template directory
template_dir = join(curdir, '../templates/')

# root directory
root_dir = join(curdir, '../')

# session settings
session_tablename = 'session'

# default new user's password
default_password = 'pycms'

#publish html directory
publish_dir = join(curdir, '../static/html/')

#static url
static_url = lambda: web.ctx.homedomain + '/static'

#default pagination record number
default_page_size = 20

try:
    from local_config import *
except ImportError:
    pass
