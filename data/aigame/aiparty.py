from data.aigame.levels.lobby import LobbyLevel
from data.engine.eventdispatcher.eventdispatcher import EventDispatcher
from data.engine.game.game import Game
from data.aigame.levels.mainmenu import MainMenuLevel

class AIParty(Game):
    def __init__(self, pde):
        super().__init__(pde)
        self.player = None

    def activate(self):
        super().activate()

        self.currentlevel = self.pde.level_manager.addlevel(level=MainMenuLevel(man=self.pde.level_manager, pde=self.pde), 
                                                                        name="Main", active=True)

        self.pde.network_manager.onjoinednetwork.bind(self.join_game)

        self.pde.event_manager.events['wait_for_question'] = self.wait_for_question
        self.pde.event_manager.events['setup_player'] = self.setup_player
        self.pde.event_manager.events['gather_question'] = self.gather_question

    def set_id(self, id):
        print(f"Set ID to {id}")
        self.player._id = id
        return

    def join_game(self):        
        return

    def wait_for_question(self, args):
        print("Waiting For Question!")

    def set_role(self, args):
        self.player.role = args["role"]

    def setup_player(self, args):
        self.set_id(args["id"])
        self.set_host(args["host"])
        self.set_name()

        self.pde.level_manager.clearlevel()
        self.currentlevel = self.pde.level_manager.addlevel(level=LobbyLevel(man=self.pde.level_manager, pde=self.pde), 
                                                                        name="Main", active=True)
    def set_name(self):
        self.player.name = "RyDawgE"
        print(f"Name set as {self.player.name}")
        # Send Name
        event={'message_type': 'event', 'message_data': {'event_name': 'set_client_nickname', 'event_args': {'name': self.player.name, 'id': self.player._id}}}
        #event={'message_type': 'ping', 'message_data': {'data': 'SetName'}}
        self.pde.network_manager.network.send_event(event)

    def set_host(self, host):
        self.player.ishost = host
        print(f"Set Host to {self.player.ishost}")

    def gather_question(self, args):
        question = str(input("Enter question here: "))
        self.pde.network_manager.network.send_event(event={'message_type': 'event', 'message_data': {'event_name': 'validate_question', 'event_args': {'text': question}}})

    def start_game(self):
        if self.player.ishost:
            # Send Start Game
            event = {'message_type': 'event', 'message_data': {'event_name': 'start_game', 'event_args': {'host': self.player.ishost}}}
            #event={'message_type': 'ping', 'message_data': {'data': 'Start Game'}}
            self.pde.network_manager.network.send_event(event)
            

        

