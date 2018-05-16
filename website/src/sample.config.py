import os

class Configuration:
    """
    Application configuration
    """

    DEBUG = True

    BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

    TIME_ZONE = 'UTC'

    ALLOWED_HOSTS = [
        'localhost',
        '127.0.0.1'
    ]

    TEMPLATE_DIRS = [

    ]

    DATABASES = {
        'default': {
            'ENGINE': 'django.db.backends.mysql',
            'NAME': 'd_is_silent',
            'USER': 'root',
            'PASSWORD': '111111',
            'HOST': 'localhost',
            'PORT': '3306'
        }
    }

Config = Configuration()
