import logging

from flask import Flask
from flask_logfile import LogFile


app = Flask(__name__)

app.config['LOG_LEVEL'] = logging.INFO
app.config['LOG_FILE'] = '`logs/main.log`'

LogFile().init_app(app)

app.logger.debug('debug')
app.logger.info('info')
app.logger.warning('warning')
app.logger.error('error')