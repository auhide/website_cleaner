'''
Cleaner configuration settings
'''
import os

HOME_PATH = os.path.dirname(os.path.abspath(__file__))



PARSER = 'lxml'
KEEP_TAG = 1

# Creating the Absolute Paths
CSV_PATH =  'data\\tags_percent.csv'
CSV_PATH = os.path.join(HOME_PATH, CSV_PATH)

LOG_DIR = 'output\log.log'
LOG_DIR = os.path.join(HOME_PATH, LOG_DIR)