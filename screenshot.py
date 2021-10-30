# -*- coding: utf-8 -*-
"""
# ================ #
# ::		    :: #
# :: PRNTSKR34M :: #
# :: screenshot	:: #
# ::		    :: #
# ================ #



# ================================================ #
# -- Function to take a screenshot of a monitor -- #
# ================================================ #



"""

from mss import mss
from datetime import datetime
import time
import os
from move_hide import hide


def screenshot(storage_dir):
    #log.debug("[::] Taking screenshot")    
    # Screenshot and save with name equal to the time the screenshot was taken
    # Use a move command in a subshell to move the image to the specified directory
    SCREENSHOT_DIR = storage_dir
    
    try:
        os.makedirs(SCREENSHOT_DIR)

    except OSError:
        pass


    with mss() as sct:
        FILENAME = datetime.now().strftime('%Y-%m-%d_%H%M%S') + '.png'
        #log.debug('[::] Saving image {FILENAME}...')
        sct.shot(output=FILENAME)
        hide(FILENAME,SCREENSHOT_DIR)
    return
