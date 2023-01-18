from data.aigame.objects.ui.fadeintext import FadeInTextElement
from data.engine.level.level import Level
from data.engine.widgets.element.e_button import ButtonElement
from data.engine.widgets.element.e_sprite import SpriteElement

class RevealResponseLevel(Level):
    def __init__(self, man, pde):
        super().__init__(man, pde)

        self.changebackground(bg=r"data\aigame\assets\sprites\ui\bg.png")

        self.objectManager.add_object(obj=SpriteElement(man=man,pde=pde, position=[320, 64], scale=[196,64],useCenterForPosition=True, sprite=r"data\aigame\assets\sprites\ui\foolmetwice.png"))
        
        for inx, player in enumerate(self.pde.game.playerinfo.keys()):
            if self.pde.game.playerinfo[player]["role"] == "answerer":
                answerer = self.pde.game.playerinfo[player]["name"]

        self.objectManager.add_object(obj=FadeInTextElement(man=man,pde=pde, position=[320, 160], scale=[300,32],useCenterForPosition=True, text=self.pde.game.question))


        response = self.pde.game.response["text"]
        self.objectManager.add_object(obj=FadeInTextElement(man=man,pde=pde, position=[320, 256 + -32], scale=[300,32],useCenterForPosition=True, text=f"{answerer} replies:"))

        for inx, segment in enumerate(list(f'"{response}"'.split('. '))):
            self.objectManager.add_object(obj=FadeInTextElement(man=man,pde=pde, position=[320, 256 + inx*32], scale=[500,32],useCenterForPosition=True, text=segment))
