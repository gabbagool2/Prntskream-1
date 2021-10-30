"""
# ================ #
# ::		    :: #
# :: PRNTSKR34M :: #
# ::	main	:: #
# ::		    :: #
# ================ #

"""

# ============= #
# -- Imports -- #
# ============= #

import time
import logging
import sys, os
from screenshot import screenshot

# ================================================== #
# -- Create a logger for monitoring and debugging -- #
# ================================================== #

LOGS_DIR = '.\prntskream_logs'

try:
    os.makedirs(LOGS_DIR)
except OSError:
    pass

log = logging.getLogger('Prntskream_logger')
log.setLevel(logging.DEBUG)
formatter = logging.Formatter('%(asctime)s: %(funcName)s (%(lineno)d): %(message)s', '%H:%M:%S')

terminal_printout_handler = logging.StreamHandler()
terminal_printout_handler.setFormatter(formatter)
log.addHandler(terminal_printout_handler)

logfile_handler = logging.FileHandler(time.strftime(LOGS_DIR + '\prntskream_%Y-%m-%d_%H%M%S.log'), mode='w')
logfile_handler.setFormatter(formatter)
log.addHandler(logfile_handler)

# ================================================== #
# -- Check if mss is installed, if not install it -- #
# ================================================== #
try:
    import mss
    log.debug('[*] Checking for mss...')
except:
    log.error('[-] Unable to import mss, make sure it is installed')
    # TODO: code to automatically install this
    sys.exit()

# =========================================================
# -----------------------BEGIN-----------------------------
# =========================================================

# ============================== #
# -- Set screenshot directory -- #
# ============================== #
SCREENSHOT_DIR = '.\screenshots'



# =================== #
# -- Main function -- #
# =================== #

def main():

    log.info("[+] Beginning Prntskr34m")
    
    # Take screenshot once every 5 min
    for i in range(3):
        log.debug("[*] Taking a screenshot..")
        screenshot('screenshots')
        
        log.debug('[-] Sleeping...')
        time.sleep(300)
        
        
            
    return




if __name__ == "__main__":
    main()