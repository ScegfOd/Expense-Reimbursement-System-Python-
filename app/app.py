from flask import Flask
from flask_cors import CORS

app = Flask(__name__)
CORS(app)
cors = CORS(app, resources={r"/static/*": {"origins": "*"}})

import logging
logging.basicConfig(
	filename='log/main.log',
	encoding='utf-8',
	level=logging.DEBUG,
	format='%(asctime)s %(levelname)s : %(message)s')
logging.getLogger().addHandler(logging.StreamHandler())

# a decorator that can take an argument, so we can give function its own log in
# addition to the main app.log file
def func_call_logger(module_name):
	def decorator(func):
		logger = logging.getLogger(f"{module_name}.{func.__name__}")
		logger.addHandler(logging.FileHandler(f'log/{module_name}.log'))
		logger.addHandler(logging.FileHandler(f'log/{module_name}.{func.__name__}.log'))
		def decorated_func(*args, **kwargs):
			logger.debug(f"{module_name}.{func.__name__} called with {args} and {kwargs}")
			return func(*args, **kwargs)
		decorated_func.__name__ = func.__name__
		return decorated_func
	return decorator
