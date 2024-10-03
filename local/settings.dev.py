print("local settings")
DEBUG = True

SECRET_KEY = 'django-insecure-*7#51@jl^f1kw4z)@8tvu7i&oe^qeu@x8e2*14^$ojihc*+bu!(devsecretkey)'

LOGGING['formatters']['colored'] = {
    '()': 'colorlog.ColoredFormatter',
    'format': '%(log_color)s%(asctime)s %(levelname)s %(name)s %(bold_white)s%(message)s',
}
LOGGING['loggers']['src']['level'] = 'DEBUG'
LOGGING['handlers']['console']['level'] = 'DEBUG'
LOGGING['handlers']['console']['formatter'] = 'colored'
