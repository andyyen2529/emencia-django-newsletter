"""Settings for the emencia18 of emencia.django.newsletter"""
"""Settings for the emencia18 of emencia.django.newsletter"""
import os

gettext = lambda s: s

DATABASES = {'default':
             {'ENGINE': 'django.db.backends.sqlite3',
              'NAME': os.path.join(os.path.dirname(__file__), 'emencia18.db')}
}

MEDIA_URL = 'http://localhost:8000/'

SECRET_KEY = 'jkjf7878fsdok-|767sjdvjsm_qcskhvs$:?shf67dd66%&sfj'

USE_I18N = True
USE_L10N = True

SITE_ID = 1

LANGUAGE_CODE = 'zh-TW'

LANGUAGES = (('en', gettext('English')),
             ('fr', gettext('French')),
             ('de', gettext('German')),
             ('es', gettext('Spanish')),
             ('it', gettext('Italian')),
             ('pt', gettext('Portuguese')),
             ('nl', gettext('Dutch')),
             ('fo', gettext('Faroese')),
             ('ja', gettext('Japanese')),
             ('zh_CN', gettext('Simplified Chinese')),)

MIDDLEWARE_CLASSES = (
    'django.middleware.common.CommonMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.middleware.locale.LocaleMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.admindocs.middleware.XViewMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    )

ROOT_URLCONF = 'demo.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'OPTIONS': {
            'context_processors': [
                # Insert your TEMPLATE_CONTEXT_PROCESSORS here or use this
                # list if you haven't customized them:
                'django.contrib.auth.context_processors.auth',
                'django.template.context_processors.debug',
                'django.template.context_processors.i18n',
                'django.core.context_processors.request',
                'django.template.context_processors.media',
                'django.template.context_processors.static',
                'django.template.context_processors.tz',
                'django.contrib.messages.context_processors.messages',
                'emencia.django.newsletter.context_processors.media',
            ],
            'loaders': [
                'django.template.loaders.filesystem.Loader',
                'django.template.loaders.app_directories.Loader',
                'django.template.loaders.eggs.Loader',
            ]
        },
    },
]

INSTALLED_APPS = (
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.sites',
    'django.contrib.admin',
    'django.contrib.staticfiles',
    'tagging',
    'emencia.django.newsletter',
    )

DEBUG = True

STATIC_URL = '/static/'

NEWSLETTER_DEFAULT_HEADER_SENDER = 'My NewsLetter <mq.nuwainfo.com>'
