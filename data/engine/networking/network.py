import sys, socket
import pickle

class Network():
    def __init__(self, server="", port=5555):
        self.server = server
        self.port = port
        self.client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.address = (self.server, self.port)

    def connect(self):
        try:
            self.client.connect(self.address)
        except Exception as e:
            print(e)

    def disconnect(self):
        self.client.close()

    def update(self):
        print(self.client.recv(8))