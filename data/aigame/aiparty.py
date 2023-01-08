from data.engine.game.game import Game
from data.aigame.levels.testlevel import TestLevel

class AIParty(Game):
    def __init__(self, pde):
        super().__init__(pde)

    def activate(self):
        super().activate()
        self.currentlevel = self.pde.level_manager.addlevel(level=TestLevel(man=self.pde.level_manager, pde=self.pde), 
                                                                        name="Main", active=True)

        self.pde.network_manager.network.connect()