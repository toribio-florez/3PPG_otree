from os import environ

# if you set a property in SESSION_CONFIG_DEFAULTS, it will be inherited by all configs
# in SESSION_CONFIGS, except those that explicitly override it.
# the session config can be accessed from methods in your apps as self.session.config,
# e.g. self.session.config['participation_fee']

SESSION_CONFIG_DEFAULTS = {
    'real_world_currency_per_point': 1.00,
    'participation_fee': 0.00,
    'doc': "",
}

SESSION_CONFIGS = [
{
       'name': 'JS',
       'display_name': "Justice Sensitivity",
       'num_demo_participants': 1,
       'app_sequence': ['JSLong'],
    },
{
       'name': 'threepersongame',
       'display_name': "Three Person Game",
       'num_demo_participants': 3,
       'app_sequence': ['threepersongame'],
    }
]


# ISO-639 code
# for example: de, fr, ja, ko, zh-hans
LANGUAGE_CODE = 'en'

# e.g. EUR, GBP, CNY, JPY
REAL_WORLD_CURRENCY_CODE = '€'
USE_POINTS = False

ROOMS = []

ADMIN_USERNAME = 'admin'
# for security, best to set admin password in an environment variable
ADMIN_PASSWORD = environ.get('OTREE_ADMIN_PASSWORD')

DEMO_PAGE_INTRO_HTML = """ """

SECRET_KEY = ')+h6)h0syfx%@$u6^4i*x%^78zdzg28ccf1!vx_vi5%@=t2(w6'

# if an app is included in SESSION_CONFIGS, you don't need to list it here
INSTALLED_APPS = ['otree', 'radiogrid', ]
