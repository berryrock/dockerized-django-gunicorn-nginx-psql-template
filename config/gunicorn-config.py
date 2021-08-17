command = './venv/bin/gunicorn'
pythonpath = './config'
bind = '127.0.0.1:8000'
workers = 3
user = 'www'
limit_request_fields = 32000
lomit_request_filed_size = 0
raw_env = 'DJANGO_SETTINGS_MODULE=config.settings'
