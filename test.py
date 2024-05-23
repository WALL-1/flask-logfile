
from flask import Flask
from flask_logfile import LogFile

app = Flask(__name__)
LogFile().init_app(app)

app.logger.debug('debug')
app.logger.info('info')
app.logger.warning('warning')
app.logger.error('error')