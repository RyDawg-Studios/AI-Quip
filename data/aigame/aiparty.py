from data.aigame.levels.lobby import LobbyLevel
from data.aigame.levels.revealquestion import RevealQuestionLevel
from data.aigame.levels.revealresponse import RevealResponseLevel
from data.aigame.levels.revealroles import RevealRolesLevel
from data.aigame.levels.wait import WaitLevel
from data.engine.eventdispatcher.eventdispatcher import EventDispatcher
from data.engine.game.game import Game
from data.aigame.levels.mainmenu import MainMenuLevel

class AIParty(Game):
    def __init__(self, pde):
        super().__init__(pde)
        self.player = None
        self.playerinfo = {}
        self.question = ""
        self.response = {"type": "", "text": ""}

    def activate(self):
        super().activate()

        self.currentlevel = self.pde.level_manager.addlevel(level=MainMenuLevel(man=self.pde.level_manager, pde=self.pde), 
                                                                        name="Main", active=True)

        self.pde.network_manager.onjoinednetwork.bind(self.join_game)

        self.pde.event_manager.events['wait_for_question'] = self.wait_for_question
        self.pde.event_manager.events['setup_player'] = self.setup_player
        self.pde.event_manager.events['gather_question'] = self.gather_question
        self.pde.event_manager.events['set_role'] = self.set_role
        self.pde.event_manager.events['set_playersinfo'] = self.set_playersinfo
        self.pde.event_manager.events['game_starting'] = self.game_starting
        self.pde.event_manager.events['reveal_roles'] = self.reveal_roles
        self.pde.event_manager.events['reveal_question'] = self.reveal_question
        self.pde.event_manager.events['reveal_response'] = self.reveal_response




    def set_id(self, id):
        print(f"Set ID to {id}")
        self.player._id = id
        return

    def join_game(self):        
        return

    def wait_for_question(self, args):
        self.pde.level_manager.clearlevel()
        self.currentlevel = self.pde.level_manager.addlevel(level=WaitLevel(man=self.pde.level_manager, pde=self.pde), 
                                                                        name="Main", active=True)

    def reveal_roles(self, args):
        self.pde.network_manager.network.send_event(event={'message_type': 'event', 'message_data': {'event_name': 'retrieve_playerinfo', 'event_args': {'id': self.pde.game.player._id}}})

    def set_playersinfo(self, args):
        info = args["info"]
        print(f"args: {info}")
        self.playerinfo = args["info"]
        
        self.pde.level_manager.clearlevel()
        self.currentlevel = self.pde.level_manager.addlevel(level=RevealRolesLevel(man=self.pde.level_manager, pde=self.pde), 
                                                                        name="Main", active=True)

    def set_role(self, args):
        role = args["role"]
        self.player.role = role
        print(f"Role set to: {role}")

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
        event={'message_type': 'event', 'message_data': {'event_name': 'set_client_nickname', 'event_args': {'name': self.player.name, 'id': self.player._id}}}
        self.pde.network_manager.network.send_event(event)

    def set_host(self, host):
        self.player.ishost = host
        print(f"Set Host to {self.player.ishost}")

    def gather_question(self, args):
        question = str(input("Enter question here: "))
        self.pde.network_manager.network.send_event(event={'message_type': 'event', 'message_data': {'event_name': 'validate_question', 'event_args': {'text': question}}})

    def reveal_question(self, args):
        self.question = args["text"]

        self.pde.level_manager.clearlevel()
        self.currentlevel = self.pde.level_manager.addlevel(level=RevealQuestionLevel(man=self.pde.level_manager, pde=self.pde), 
                                                                        name="Main", active=True)

    def game_starting(self, args):
        return

    def start_game(self):
        if self.player.ishost:
            event = {'message_type': 'event', 'message_data': {'event_name': 'start_game', 'event_args': {'host': self.player.ishost}}}
            self.pde.network_manager.network.send_event(event)

    def send_manual_response(self, response):
        event = {'message_type': 'event', 'message_data': {'event_name': 'get_response', 'event_args': {"type": "manual", "text": str(response)}}}
        self.pde.network_manager.network.send_event(event)

    def send_ai_response(self):
        event = {'message_type': 'event', 'message_data': {'event_name': 'get_response', 'event_args': {"type": "ai", "text": ""}}}
        self.pde.network_manager.network.send_event(event)

    def reveal_response(self, args):
        self.response = args
        self.pde.level_manager.clearlevel()
        self.currentlevel = self.pde.level_manager.addlevel(level=RevealResponseLevel(man=self.pde.level_manager, pde=self.pde), 
                                                                        name="Main", active=True)

