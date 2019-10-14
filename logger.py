
import os
from constants import LOG_DIR



class Logger:
    '''TODO: Implement this class'''
    
    def __init__(self):

        os.remove(LOG_DIR)
        
        # Creating the path if it does not exist
        if not os.path.exists(os.path.dirname(LOG_DIR)):
            try:
                os.makedirs(os.path.dirname(LOG_DIR))
            except OSError as exc: # Guard against race condition
                if exc.errno != errno.EEXIST:
                    raise


    def add(self, string):

        with open(LOG_DIR, 'a') as f:
            f.write(f"L O G   >>>   {str(string)}\n")
        