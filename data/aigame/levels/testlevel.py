from data.aigame.objects.player.player import AIQuip_PlayerObject
from data.engine.level.level import Level

class TestLevel(Level):
    def __init__(self, man, pde):
        super().__init__(man, pde)

        self.pde.game.player = self.objectManager.add_object(obj=AIQuip_PlayerObject(man=man, pde=pde))