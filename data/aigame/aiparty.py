from data.engine.game.game import Game
from data.aigame.levels.testlevel import TestLevel

class AIParty(Game):
    def __init__(self, pde):
        super().__init__(pde)
        self.player = None

    def activate(self):
        super().activate()

        self.currentlevel = self.pde.level_manager.addlevel(level=TestLevel(man=self.pde.level_manager, pde=self.pde), 
                                                                        name="Main", active=True)

        self.pde.network_manager.onjoinednetwork.bind(self.joingame)

        self.pde.event_manager.events['set_host'] = self.set_host
        self.pde.event_manager.events['set_id'] = self.set_id

    def set_id(self, args):
        self.player._id = args["id"]
        return

    def joingame(self):
        self.setname()
        print("Joined Lobby")

    def setname(self):
        self.player.name = "RyDawgE"
        print(f"Name set as {self.player.name}")
        self.pde.network_manager.network.send_event(event={'message_type': 'event', 'message_data': {'event_name': 'set_client_nickname', 'event_args': {'name': self.player.name}}})


    def set_host(self, args):
        print("Client set to host")
        self.player.ishost = args["host"]

    def startgame(self):
        print(self.player.ishost)
        if self.player.ishost:
            event = {'message_type': 'event', 'message_data': {'event_name': 'start_game', 'event_args': {'host': self.player.ishost}}}
            self.pde.network_manager.network.send_event(event=event)

        

