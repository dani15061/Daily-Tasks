import logging

logging.debug('It is a debug message')	# it will not be printed
logging.info('It is an info message')	# not printed
logging.warning('OOPs!!! It is a warning')	# it will be print because it is default level
logging.error('Oops !! an error message')	# will be printed 
logging.critical('Oh!!!! it is a critical message')	# will be printed