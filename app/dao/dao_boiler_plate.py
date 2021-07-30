from app.db.conn import get_db_connection
from app.app import func_call_logger
import logging

# because I'm so tired of this copy-pasta
def logs_and_db_connection(module_name):
	def decorator(func):
		logger = logging.getLogger(module_name)
		@func_call_logger(module_name)
		def decorated_func(*args, **kwargs):
			try:
				cnxn = get_db_connection()
				db = cnxn.cursor()
				logger.info("database connected...")
				result = func(db, *args, **kwargs)
				db.close()
				logger.info("database transaction successful")
				logger.info(f"returning {result}")
			except Exception as e:
				logger.error(e, exc_info=True)
				result = None # in case of exceptions
				logger.warning(f"returning {result}")
			finally:
				cnxn.close()
				return result
		decorated_func.__name__ = func.__name__
		return decorated_func
	return decorator
