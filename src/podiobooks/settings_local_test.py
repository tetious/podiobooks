# INSTRUCTIONS
# SAVE A COPY OF THIS FILE IN THIS DIRECTORY WITH THE NAME local_settings.py
# MAKE YOUR LOCAL SETTINGS CHANGES IN THAT FILE AND DO NOT CHECK IT IN
# CHANGES TO THIS FILE SHOULD BE TO ADD/REMOVE SETTINGS THAT NEED TO BE
# MADE LOCALLY BY ALL INSTALLATIONS

# local_settings.py, once created, should never be checked into source control

import os

# Set the root path of the project so it's not hard coded
PROJECT_PATH = os.path.abspath(os.path.dirname(__file__))

DEBUG = True
TEMPLATE_DEBUG = DEBUG

# Cache Settings
# CACHE_BACKEND = 'memcached://127.0.0.1:11211/'
CACHE_BACKEND = 'dummy:///'
CACHE_MIDDLEWARE_SECONDS = 30
CACHE_MIDDLEWARE_ANONYMOUS_ONLY = True

ADMINS = (
    # ('Your Name', 'your_email@domain.com'),
)

# Absolute path to the directory that holds media.
# Example: "/home/media/media.lawrence.com/"
MEDIA_ROOT = PROJECT_PATH + '/media/'
MEDIA_COVERS = MEDIA_ROOT + "/covers/"
MEDIA_AWARDS = MEDIA_ROOT + "/awards/"

# URL that handles the media served from MEDIA_ROOT. Make sure to use a
# trailing slash if there is a path component (optional in other cases).
# Examples: "http://media.lawrence.com", "http://example.com/media/"
MEDIA_URL = '/media/'

# URL prefix for admin media -- CSS, JavaScript and images. Make sure to use a
# trailing slash.
# Examples: "http://foo.com/media/", "/media/".
ADMIN_MEDIA_PREFIX = '/adminmedia/'

# Test DB settings. (SQLLite)
DATABASE_ENGINE = 'sqlite3'
DATABASE_NAME = '/tmp/rpgid.db'

# Local time zone for this installation. Choices can be found here:
# http://en.wikipedia.org/wiki/List_of_tz_zones_by_name
# although not all choices may be available on all operating systems.
# If running in a Windows environment this must be set to the same as your
# system time zone.
TIME_ZONE = 'America/Chicago'

# Language code for this installation. All choices can be found here:
# http://www.i18nguy.com/unicode/language-identifiers.html
LANGUAGE_CODE = 'en-us'

SITE_ID = 1

# If you set this to False, Django will make some optimizations so as not
# to load the internationalization machinery.
USE_I18N = False

# Make this unique, and don't share it with anybody.
SECRET_KEY = 'zv$+w7juz@(g!^53o0ai1u082)=jkdfmy_r=3)fglrj5t8l$2#'

# IP Addresses that should be treated as internal/debug users
INTERNAL_IPS = ('127.0.0.1',)

# Email Settings
EMAIL_HOST = 'a real smtp server'
EMAIL_HOST_USER = 'your_mailbox_username'
EMAIL_HOST_PASSWORD = 'your_mailbox_password'
DEFAULT_FROM_EMAIL = 'a real email address'
SERVER_EMAIL = 'a real email address'

# django-registration Settings
ACCOUNT_ACTIVATION_DAYS = 14

# Local add-ons to main variables
LOCAL_MIDDLEWARE_CLASSES = None
LOCAL_TEMPLATE_CONTEXT_PROCESSORS = None

##### PB2 Custom Variables Below Here #######

### Search

SEARCH_PROVIDER = 'DEFAULT'

# Sphinx
# SEARCH_PROVIDER = 'SPHINX'
# SPHINX_SERVER = 'localhost'
# SPHINX_PORT = 3312
# SPHINX_API_VERSION = 0x116