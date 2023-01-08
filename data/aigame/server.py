import socket


class GameServer():
    def __init__(self):
        self.host = "127.0.0.1"
        self.port = 5555

    def start(self):
        print("Online")
        try:
            with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
                s.bind((self.host, self.port))
                s.listen()
                conn, addr = s.accept()
                with conn:
                    print(f"Connected by {addr}")
                    while True:
                        conn.sendall(bytes("Hello!", "utf-8"))
                        data = conn.recv(1024)
                        if not data:
                            break
                        conn.sendall(data)
        except:
            print("Error")


game = GameServer()
game.start()


