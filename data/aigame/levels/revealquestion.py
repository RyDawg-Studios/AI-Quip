from data.aigame.objects.ui.fadeintext import FadeInTextElement
from data.engine.level.level import Level
from data.engine.widgets.element.e_button import ButtonElement
from data.engine.widgets.element.e_sprite import SpriteElement

class RevealQuestionLevel(Level):
    def __init__(self, man, pde):
        super().__init__(man, pde)

        self.changebackground(bg=r"data\aigame\assets\sprites\ui\bg.png")

        self.objectManager.add_object(obj=SpriteElement(man=man,pde=pde, position=[320, 64], scale=[196,64],useCenterForPosition=True, sprite=r"data\aigame\assets\sprites\ui\foolmetwice.png"))
        
        for inx, player in enumerate(self.pde.game.playerinfo.keys()):
            if self.pde.game.playerinfo[player]["role"] == "questioneer":
                asker = self.pde.game.playerinfo[player]["name"]

        text = f"{asker} asks... {self.pde.game.question}"
        self.objectManager.add_object(obj=FadeInTextElement(man=man,pde=pde, position=[320, 240], scale=[400,32],useCenterForPosition=True, text=text))


