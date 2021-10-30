

import socket as sck
import threading


class Server_tcp:
    
    def __init__(self,bind_ip,bind_port):
        self.BIND_IP = bind_ip 
        self.BIND_PORT = bind_port 

        self.SERVER = sck.socket(sck.AF_INET,sck.SOCK_STREAM)
        self.SERVER.bind((BIND_IP,BIND_PORT))
        
        self.SERVER.listen(5)
        print("Listening on",BIND_IP,BIND_PORT)
        
        while True:
            CLIENT,ADDR = self.SERVER.accept()
            print('Accepted connection from ',ADDR[0],ADDR[1])
            client_handler = threading.Thread(target=self.handle_client,args=(CLIENT,))
            client_handler.start()

    def handle_client(self,client_socket):
        RECV = client_socket.recv(4098).decode()
        FILE = os.path.basename(RECV)
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




















    
