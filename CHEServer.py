import socket
import threading

class Server(threading.Thread):
    def __init__(self, host, port):
        super().__init__()
        self.server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.host = host
        self.port = port
    
    def run(self):
        self.server.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
        #server.setblocking(False)
        self.server.bind((self.host, self.port))
        self.server.listen(5)
        print('Listening to {}'.format(self.server.getsockname()))


class Accept(threading.Thread):
    def __init__(self, server):
        super().__init__()
        self.server = server
        self.signals = 0
        self.conn = None
        self.addr = None
        self.clients = {}
    
    def run(self):
        while True:
            self.conn, self.addr = self.server.accept()
            print(f'Accepted connect from {self.addr}...')
            self.clients[str(self.addr)] = [self.conn, self.addr]
            self.signals += 1


class Recieve_Data(threading.Thread):
    def __init__(self):
        super().__init__()
    
    def run(self):
        pass
    
    def Recieve(self, connect, buff_size):
        buff_size = int(buff_size)
        data      = connect.recv(buff_size).decode('ascii')
        return data
        
        
###############################################################################


Serv = Server('localhost', 15000)
Serv.start()
Serv.join()

Acpt = Accept(Serv.server)
Acpt.start()

Rcve = Recieve_Data()
Rcve.start()

while True:
    clients = list(Acpt.clients.keys())
    if clients:
        for client in clients:
            try:
                connect = Acpt.clients[client][0]
                data    = Rcve.Recieve(connect, 1024)
                if data:
                    if data == 'Q':
                        Serv.server.close()
                        
                        break
                    print(f'{data}')
            except Exception as err:
                print(err)
                continue
