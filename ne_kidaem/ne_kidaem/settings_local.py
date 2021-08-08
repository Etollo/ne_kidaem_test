ALLOWED_HOSTS = ['127.0.0.1']
DEBUG = True
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': 'ne_kidaem',
        'HOST': '127.0.0.1',
        'PORT': '5432',
    },
}