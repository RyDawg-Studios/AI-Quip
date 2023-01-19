from data.aigame.objects.ui.fadeintext import FadeInTextElement
from data.engine.level.level import Level
from data.engine.widgets.element.e_button import ButtonElement
from data.engine.widgets.element.e_sprite import SpriteElement

class RevealRolesLevel(Level):
    def __init__(self, man, pde):
        super().__init__(man, pde)

        self.changebackground(bg=r"data\aigame\assets\sprites\ui\bg.png")

        self.objectManager.add_object(obj=SpriteElement(man=self.objectManager,pde=pde, position=[320, 64], scale=[196,64],useCenterForPosition=True, sprite=r"data\aigame\assets\sprites\ui\foolmetwice.png"))
        

        print(f"role: {self.pde.game.player.role}")
        role = self.pde.game.player.role

        if role == "answerer":
            self.objectManager.add_object(obj=SpriteElement(man=self.objectManager,pde=pde, position=[320, 240], scale=[216,82],useCenterForPosition=True, sprite=r"data\aigame\assets\sprites\ui\uranswerer.png"))
        elif role == "questioneer":
            self.objectManager.add_object(obj=SpriteElement(man=self.objectManager,pde=pde, position=[320, 240], scale=[216,82],useCenterForPosition=True, sprite=r"data\aigame\assets\sprites\ui\urquestioner.png"))
        elif role == "voter":
            self.objectManager.add_object(obj=SpriteElement(man=self.objectManager,pde=pde, position=[320, 240], scale=[216,82],useCenterForPosition=True, sprite=r"data\aigame\assets\sprites\ui\urvoter.png"))



        for inx, player in enumerate(self.pde.game.playerinfo.keys()):
            name = self.pde.game.playerinfo[player]["name"]
            role = self.pde.game.playerinfo[player]["role"]
            text = f"{name} - {role}"
            self.objectManager.add_object(obj=FadeInTextElement(man=self.objectManager,pde=pde, position=[320, 300 + inx*32], scale=[128,32],useCenterForPosition=True, text=text))


