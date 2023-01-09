import socket
import threading

class Client:
    def __init__(self, conn, addr):
        self.connection = conn
        self.address = addr

    def start(self):
        while True:
            self.update()

    def update(self):
        return

class GameServer:
    def __init__(self):
        self.host = socket.gethostbyname(socket.gethostname())
        self.port = 5555

        self.address = (self.host, self.port)

        self.server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

        self.connections = []

    def manage_client(self, conn, addr):
        cli = Client(conn, addr)
        self.connections.append(cli)
        cli.start()

    def start(self):
        self.server.bind(self.address)
        self.server.listen()
        print("Game Server Started")
        while True:
            conn, addr = self.server.accept()
            cli_thread = threading.Thread(target=self.manage_client, args=(conn, addr))
            cli_thread.start()
            print("Accepted New Client")

game = GameServer()
game.start()


