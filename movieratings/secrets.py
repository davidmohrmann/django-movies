# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = '#994xy-z61gl0r@$-$yzwm3=f=m8rp-m%j4%^j!u=(8(mi$@#9'

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': 'moviedata',
        'USER': 'davidmohrmann',
        'PASSWORD': '',
        'HOST': '127.0.0.1',
        'PORT': '5432',
    }
}
