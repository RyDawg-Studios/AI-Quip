from data.aigame.objects.player.player import AIQuip_PlayerObject
from data.engine.level.level import Level
from data.engine.widgets.element.e_button import ButtonElement
from data.engine.widgets.element.e_sprite import SpriteElement

class LobbyLevel(Level):
    def __init__(self, man, pde):
        super().__init__(man, pde)

        self.changebackground(bg=r"data\aigame\assets\sprites\ui\bg.png")

        self.pde.game.player = self.objectManager.add_object(obj=AIQuip_PlayerObject(man=man, pde=pde))

        self.objectManager.add_object(obj=ButtonElement(man=man,pde=pde, position=[320, 240], scale=[64,32],useCenterForPosition=True, sprite=r"data\aigame\assets\sprites\ui\start.png", bind=self.pde.network_manager.activate))
        self.objectManager.add_object(obj=SpriteElement(man=man,pde=pde, position=[320, 64], scale=[196,64],useCenterForPosition=True, sprite=r"data\aigame\assets\sprites\ui\foolmetwice.png"))