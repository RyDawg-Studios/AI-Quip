import sys, socket
import pickle

class Network():
    def __init__(self, server="", port=5050):
        self.server = server
        self.port = port
        self.client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.address = (self.server, self.port)
        self.connected = False

    def connect(self):
        try:
            self.client.connect(self.address)
            self.connected = True
        except Exception as e:
            print(e)

    def disconnect(self):
        self.connected = False
        self.client.close()

    def update(self):
        data = self.client.recv(1024)
        if not data:
            self.disconnect()