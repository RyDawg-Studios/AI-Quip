from data.aigame.objects.player.player import AIQuip_PlayerObject
from data.engine.level.level import Level
from data.engine.widgets.element.e_button import ButtonElement
from data.engine.widgets.element.e_sprite import SpriteElement
from data.engine.widgets.element.e_textbox import TextBoxElement

class LobbyLevel(Level):
    def __init__(self, man, pde):
        super().__init__(man, pde)

        self.changebackground(bg=r"data\aigame\assets\sprites\ui\bg.png")

        if self.pde.game.player.ishost:
            self.objectManager.add_object(obj=ButtonElement(man=self.objectManager,pde=pde, position=[320, 180], scale=[64,32],useCenterForPosition=True, sprite=r"data\aigame\assets\sprites\ui\start.png", bind=self.pde.game.start_game))
        else:
            self.objectManager.add_object(obj=SpriteElement(man=self.objectManager,pde=pde, position=[320, 240], scale=[64,32],useCenterForPosition=True, sprite=r"data\aigame\assets\sprites\ui\wait.png"))

        self.objectManager.add_object(obj=SpriteElement(man=self.objectManager,pde=pde, position=[320, 140], scale=[64,32],useCenterForPosition=True, sprite=r"data\aigame\assets\sprites\ui\lobby.png"))
        self.objectManager.add_object(obj=SpriteElement(man=self.objectManager,pde=pde, position=[320, 64], scale=[196,64],useCenterForPosition=True, sprite=r"data\aigame\assets\sprites\ui\foolmetwice.png"))

