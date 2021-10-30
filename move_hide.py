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

def hide(FILE,DIR):
    cmd = 'move ' + ' ' + FILE + ' ' + DIR
    os.system(cmd)
    return
