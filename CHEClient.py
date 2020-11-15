import socket
import threading

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


###############################################################################


Cli = Client('localhost', 15000)
Cli.start()
Cli.join()

Sen = Send_Data(Cli.client, Cli.nickname)
Sen.start()
while True:
    msg = input('Writing >>> ')
    Sen.Send(msg)
    if msg == "Q":
        break
