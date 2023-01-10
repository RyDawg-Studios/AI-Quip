from data.engine.networking.network import Network
import threading


class NetworkManager():
    def __init__(self, pde):
        self.active = True
        self.pde = pde
        self.network = None

    def activate(self):
        net = threading.Thread(target=self.network_thread, args=())
        net.start()

    def network_thread(self):
        if self.pde.config_manager.config["config"]["network"]["connectToServer"]:
            self.network = Network(server="127.0.0.1")
            self.network.connect()

        while True:
            self.network.update()

        
    def update(self):
        pass