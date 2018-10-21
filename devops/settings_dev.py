from .settings import *


LOGGING = {
    'version': 1,
    'disable_existing_loggers': False,
    'loggers': {
        'dashboard': {
            'handlers': ["reboot"],
            'level': 'DEBUG',
        },
        'django': {
            'handlers': ["reboot"],
            'level': 'DEBUG',
        }
    },
    'handlers': {
        'reboot': {
            'level': 'DEBUG',
            'class': 'logging.StreamHandler',
            'formatter': 'simple',
        }
    },
    'formatters': {
        'simple': {
            'format': '[%(levelname)s] %(message)s'
        },
    },
}