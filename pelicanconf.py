AUTHOR = 'Arvindh Manian'
SITENAME = 'Arvindh Does Things'
SITEURL = ''

PATH = 'content'

TIMEZONE = 'America/New_York'

DEFAULT_LANG = 'en'

# Feed generation is usually not desired when developing
FEED_ALL_ATOM = None
CATEGORY_FEED_ATOM = None
TRANSLATION_FEED_ATOM = None
AUTHOR_FEED_ATOM = None
AUTHOR_FEED_RSS = None

DEFAULT_PAGINATION = 10
DISPLAY_PAGES_ON_MENU = True
SITESUBTITLE = "A repository of my random thoughts and projects"
BIO = "A repository of my random thoughts and projects"
FOOTER_TEXT = "Made with ♥ by Arvindh using Pelican"

STATIC_PATHS = ['images', 'extra/favicon.ico']

EXTRA_PATH_METADATA = {
    'extra/favicon.ico': {'path': 'favicon.ico'}
}

# Uncomment following line if you want document-relative URLs when developing
# RELATIVE_URLS = True

DEFAULT_DATE_FORMAT = '%B %d, %Y'
REVERSE_ARCHIVE_ORDER = True
TAG_CLOUD_STEPS = 8

PATH = 'content'
THEME = './pelican-hyde'
PROFILE_IMAGE = './profile.png'

MARKUP = 'md'

HTML_LANG = 'en'

SOCIAL = (('github',  'https://www.github.com/arvindh-manian'),
          ('reddit', 'https://www.reddit.com/arvindh_manian'),
          ('linkedin', 'https://www.linkedin.com/in/arvindh-manian/'),
          ('email', 'arvindh.manian@duke.edu'))
