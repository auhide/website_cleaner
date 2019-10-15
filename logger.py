
import os
import logging
from constants import LOG_DIR




class Logger:
    '''
    Custom Logger
    '''

    def __init__(self, dir=LOG_DIR, name='cleaner_logger'):
        '''
        Setuping the Logging object
        '''

        
        # Try to create the path to the Log file
        try:
            # Going back a folder
            log_folder = os.path.abspath(os.path.join(LOG_DIR, ".."))
                        
            os.makedirs(log_folder)

        # If the path exists
        except FileExistsError:
            pass



        # Delete the previous Log file
        try:
            os.remove(LOG_DIR)
        
        # If it does not exist, create it
        except FileNotFoundError:
            open(LOG_DIR, 'w')



        self.logger = logging.getLogger(name)
        self.logger.setLevel(logging.DEBUG)

        # F I L E   H A N D L I N G
        #####################################################################################
        # The path to the current file
        curr_dir_path = os.path.dirname(os.path.abspath(__file__))

        # Creating the File Handler for the Logging
        f_handler = logging.FileHandler(os.path.join(curr_dir_path, dir))
        #####################################################################################


        # F O R M A T T I N G   H A N D L I N G
        #####################################################################################
        formatter = logging.Formatter('%(asctime)s - %(levelname)s - %(message)s')
        f_handler.setFormatter(formatter)
        #####################################################################################

        # Adding the Formatted File Handler to the Logging object
        self.logger.addHandler(f_handler)

    def add(self, string):
        self.logger.debug(str(string))

