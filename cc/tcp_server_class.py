

import socket as sck
import threading


class Server_tcp:
    
    def __init__(self,bind_ip,bind_port):
        self.bind_ip = bind_ip 
        self.bind_port = bind_port 

        self.server = sck.socket(sck.AF_INET,sck.SOCK_STREAM)
        self.server.bind((bind_ip,bind_port))
        
        self.server.listen(5)
        print("Listening on",bind_ip,bind_port)
        
        while True:
            client,addr = self.server.accept()
            print('Accepted connection from ',addr[0],addr[1])
            client_handler = threading.Thread(target=self.handle_client,args=(client,))
            client_handler.start()

    def handle_client(self,client_socket):
        SEPARATOR = ';'
        FILE, FILE_SIZE = req.split(SEPARATOR)
        FILE = os.path.basename(FILE)
        FILE_SIZE = int(FILE_SIZE)
        with open(FILE,"wb") as f:
            while True:
                bytes_read = client_socket.recv(4098)
		if not bytes_read:
		    break
	  	f.write(bytes_read)

	client_socket.close()





def main():
    # server = Server_tcp("127.0.0.1",6969)
    return




if __name__ == '__main__':
    main()




















    
