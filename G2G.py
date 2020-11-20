import socket
import threading


# Server Side
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


# Client Side
class Client(threading.Thread):
    def __init__(self, host, port):
        super().__init__()
        self.host = host
        self.port = port
        self.client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.nickname = ""

    def run(self):
        self.client.connect((self.host, self.port))
        self.nickname = input('Enter your Nickname >>> ')


class Send_Data(threading.Thread):
    def __init__(self, sock, nickname):
        super().__init__()
        self.sock = sock
        self.name = nickname

    def run(self):
        pass

    def Send(self, msg):
        if msg == "Q":
            self.sock.close()
        else:
            data = f"{self.name}: {msg}".encode('ascii')
            self.sock.sendall(data)


