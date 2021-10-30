"""
# ================ #
# ::		    :: #
# :: PRNTSKR34M :: #
# ::   export	:: #
# ::		    :: #
# ================ #




# ============================================ #
# -- Export data to a desired remote device -- #
# ============================================ #

"""


# Connect to a host and transfer data

# Imports
import socket
import os
import shutil

SERVER_REMOTE = ''
PORT_REMOTE = 0
INPUT_DIR = ''
ARCHIVE_OUT= ''
DIR_SIZE = os.path.getsize(directory)


def export():
    
    # Compress directory before sending
    shutil.make_archive(ARCHIVE_OUT,zip,INPUT_DIR)
    
    # Store compressed file location
    # Create client socket
    tx_client = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
    tx_client.connect((SERVER_REMOTE,PORT_REMOTE))
    tx_client.send(f"{ARCHIVE_OUT}")


    # Open the archive in read mode and get the binary data, read 4kB at a time
    # Send data and close the connection
    with open(ARCHIVE_OUT,"rb") as f:
        while True:
            bytes_read = f.read(4096)
	    if not bytes_read:
	        break

	    tx_client.sendall(bytes_read)
    tx_client.close()
    return



