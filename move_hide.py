"""
# ================ #
# ::		    :: #
# :: PRNTSKR34M :: #
# ::  move_hide	:: #
# ::		    :: #
# ================ #






# ==================================================== #
# -- Utility function to move a file to a directory -- #
# ==================================================== #

"""


# Imports
import os

def hide(file,directory):
    #log.debug('[::] Moving ' + file + ' to ' + directory )
    cmdd = 'move ' + file + ' ' + directory
    os.system(cmdd)
    return
