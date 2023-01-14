import socket
import json

class Network():
    def __init__(self, owner, server="", port=5050):
        self.owner = owner
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
        return

    def disconnect(self):
        self.connected = False
        self.client.close()
        return

    def send_event(self, event={'message_type': 'ping', 'message_data': {'data': "Default Message!"}}):
        print(f"Sending Event: {event}")
        self.client.sendall(bytes(json.dumps(event), 'utf-8'))

    def update(self):
        try:
            data = json.loads(self.client.recv(1024).decode('utf-8'))
            print(f"Receiving event: {data}")
            if data["message_type"] == 'ping':
                print(data['message_data']['data'])
            elif data['message_type'] == 'event':
                self.owner.pde.event_manager.handle_netevent(data)
            if not data:
                self.disconnect()
        except:
            return
