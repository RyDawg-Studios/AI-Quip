from data.engine.networking.network import Network


class NetworkManager():
    def __init__(self, pde):
        self.active = True
        self.pde = pde
        self.network = None

    def activate(self):
        if self.pde.config_manager.config["config"]["network"]["connectToServer"]:
            self.network = Network(server="127.0.0.1")

        
    def update(self):
        while self.active:
            if self.network is not None:
                self.network.update()