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

        self.pde.network_manager.onjoinednetwork.bind(self.join_game)

        self.pde.event_manager.events['set_host'] = self.set_host
        self.pde.event_manager.events['set_id'] = self.set_id

    def set_id(self, args):
        id = args["id"]
        print(f"Name ID as {id}")
        self.player._id = id
        return

    def join_game(self):
        print("Joined Lobby")
        self.set_name()

    def set_name(self):
        self.player.name = "RyDawgE"
        print(f"Name set as {self.player.name}")
        # Send Name
        event={'message_type': 'event', 'message_data': {'event_name': 'set_client_nickname', 'event_args': {'name': self.player.name, 'id': self.player._id}}}
        #event={'message_type': 'ping', 'message_data': {'data': 'SetName'}}
        self.pde.network_manager.network.send_event(event)

    def set_host(self, args):
        ishost = args["host"]
        print(f"Name Host to {ishost}")
        self.player.ishost = ishost

    def start_game(self):
        if self.player.ishost:
            # Send Start Game
            event = {'message_type': 'event', 'message_data': {'event_name': 'start_game', 'event_args': {'host': self.player.ishost}}}
            #event={'message_type': 'ping', 'message_data': {'data': 'Start Game'}}
            self.pde.network_manager.network.send_event(event)

        

