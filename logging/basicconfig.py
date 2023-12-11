'''
import logging

logging.basicConfig(level=logging.INFO)
logging.info('This is an info message.This will get logged.')
'''
#process ID
'''
import logging

logging.basicConfig(format='%(process)d-%(levelname)s-%(message)s')
logging.warning('This message is a warning')
'''
#timestamp
'''
import logging

logging.basicConfig(format='%(asctime)s - %(message)s', level=logging.INFO)
logging.info('This message is to indicate that Admin has just logged in')
'''
