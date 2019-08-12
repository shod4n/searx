import certifi
import logging
from os import environ
from os.path import realpath, dirname, join, abspath, isfile
from io import open
from ssl import OPENSSL_VERSION_INFO, OPENSSL_VERSION
try:
    from yaml import safe_load
except:
    from sys import exit, stderr
    stderr.write('[E] install pyyaml\n')
    exit(2)

searx_dir = abspath(dirname(__file__))
engine_dir = dirname(realpath(__file__))


def check_settings_yml(file_name):
    if isfile(file_name):
        return file_name
    else:
        return None

# find location of settings.yml
if 'SEARX_SETTINGS_PATH' in environ:
    # if possible set path to settings using the
    # enviroment variable SEARX_SETTINGS_PATH
    settings_path = check_settings_yml(environ['SEARX_SETTINGS_PATH'])
else:
    # if not, get it from searx code base or last solution from /etc/searx
    settings_path = check_settings_yml(join(searx_dir, 'settings.yml')) or check_settings_yml('/etc/searx/settings.yml')

if not settings_path:
    raise Exception('settings.yml not found')

# load settings
with open(settings_path, 'r', encoding='utf-8') as settings_yaml:
    settings = safe_load(settings_yaml)

searx_debug_env = environ.get('SEARX_DEBUG', '').lower()
if searx_debug_env == 'true' or searx_debug_env == '1':
    searx_debug = True
elif searx_debug_env == 'false' or searx_debug_env == '0':
    searx_debug = False
else:
    searx_debug = settings.get('general', {}).get('debug')

if searx_debug:
    logging.basicConfig(level=logging.DEBUG)
else:
    logging.basicConfig(level=logging.WARNING)

logger = logging.getLogger('searx')
logger.debug('read configuration from %s', settings_path)

if OPENSSL_VERSION_INFO[0:3] < (1, 0, 2):
    if hasattr(certifi, 'old_where'):
        environ['REQUESTS_CA_BUNDLE'] = certifi.old_where()
    logger.warning('You are using an old openssl version({0}), please upgrade above 1.0.2!'.format(OPENSSL_VERSION))

logger.info('Initialisation done')

if 'SEARX_SECRET' in environ:
    settings['server']['secret_key'] = environ['SEARX_SECRET']
if 'SEARX_BIND_ADDRESS' in environ:
    settings['server']['bind_address'] = environ['SEARX_BIND_ADDRESS']
