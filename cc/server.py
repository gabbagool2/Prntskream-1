import socket






def main():

    SERVER_LOCAL = ''
    PORT_LOCAL = 0

    BUFFER_SIZE = 4096
    SEPARATOR = ";"

    server = socket.socket(SOCKET.AF_NET,SOCKET.SOCK_STREAM)

    server.bind((SERVER_LOCAL,PORT_LOCAL))
    server.listen(5)




    
