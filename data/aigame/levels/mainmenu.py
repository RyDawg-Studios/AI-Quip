from data.aigame.objects.player.player import AIQuip_PlayerObject
from data.engine.level.level import Level
from data.engine.widgets.element.e_button import ButtonElement
from data.engine.widgets.element.e_sprite import SpriteElement
from data.engine.widgets.element.e_textbox import TextBoxElement

class MainMenuLevel(Level):
    def __init__(self, man, pde):
        super().__init__(man, pde)

        self.changebackground(bg=r"data\aigame\assets\sprites\ui\bg.png")

        self.pde.game.player = self.objectManager.add_object(obj=AIQuip_PlayerObject(man=self.objectManager, pde=pde))

        self.objectManager.add_object(obj=ButtonElement(man=self.objectManager,pde=pde, position=[320, 240], scale=[64,32],useCenterForPosition=True, sprite=r"data\aigame\assets\sprites\ui\start.png", bind=self.pde.network_manager.activate))
        self.objectManager.add_object(obj=SpriteElement(man=self.objectManager,pde=pde, position=[320, 64], scale=[196,64],useCenterForPosition=True, sprite=r"data\aigame\assets\sprites\ui\foolmetwice.png"))

        tb = self.objectManager.add_object(obj=TextBoxElement(man=self.objectManager,pde=pde, position=[320, 140], scale=[240,64],useCenterForPosition=True))
        tb.confirm_event.bind(self.confirm_name)

    def confirm_name(self, text):
        self.pde.game.set_name(text)