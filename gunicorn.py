import gevent.monkey

gevent.monkey.patch_all()
debug = True
loglevel = 'debug'
bind = '0.0.0.0:5000'

workers = 1
threads = 2
worker_class = 'gunicorn.workers.ggevent.GeventWorker'
daemon = False

pidfile = './logs/gunicorn.pid'
logfile = './logs/debug.log'
accesslog = './logs/gunicorn_access.log'
errorlog = './logs/gunicorn_error.log'

x_forwarded_for_header = 'X-FORWARDED-FOR'
