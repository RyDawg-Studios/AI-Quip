from data.aigame.objects.ui.fadeintext import FadeInTextElement
from data.engine.level.level import Level
from data.engine.widgets.element.e_button import ButtonElement
from data.engine.widgets.element.e_sprite import SpriteElement

class RevealVotesLevel(Level):
    def __init__(self, man, pde):
        super().__init__(man, pde)

        self.changebackground(bg=r"data\aigame\assets\sprites\ui\bg.png")

        self.objectManager.add_object(obj=SpriteElement(man=self.objectManager,pde=pde, position=[320, 64], scale=[196,64],useCenterForPosition=True, sprite=r"data\aigame\assets\sprites\ui\foolmetwice.png"))
        response = self.pde.game.response["type"]
        print(f"response: {response}")
        
        if self.pde.game.response["type"] == "manual":
            self.objectManager.add_object(obj=SpriteElement(man=self.objectManager,pde=pde, position=[320, 240], scale=[216,82],useCenterForPosition=True, sprite=r"data\aigame\assets\sprites\ui\messagewasreal.png"))
            self.objectManager.add_object(obj=SpriteElement(man=self.objectManager,pde=pde, position=[320, 320], scale=[96,96],useCenterForPosition=True, sprite=r"data\aigame\assets\sprites\ui\person.png"))
        elif self.pde.game.response["type"] == "ai":
            self.objectManager.add_object(obj=SpriteElement(man=self.objectManager,pde=pde, position=[320, 240], scale=[216,82],useCenterForPosition=True, sprite=r"data\aigame\assets\sprites\ui\messagewasfake.png"))
            self.objectManager.add_object(obj=SpriteElement(man=self.objectManager,pde=pde, position=[320, 320], scale=[96,96],useCenterForPosition=True, sprite=r"data\aigame\assets\sprites\ui\robot.png"))

        if self.pde.game.player.ishost:
            self.objectManager.add_object(obj=ButtonElement(man=self.objectManager,pde=pde, position=[320, 416], scale=[64,32],useCenterForPosition=True, sprite=r"data\aigame\assets\sprites\ui\start.png", bind=self.pde.game.start_game))