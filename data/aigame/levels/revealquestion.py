from data.aigame.objects.ui.fadeintext import FadeInTextElement
from data.engine.level.level import Level
from data.engine.widgets.element.e_button import ButtonElement
from data.engine.widgets.element.e_sprite import SpriteElement
from data.engine.widgets.element.e_textbox import TextBoxElement

class RevealQuestionLevel(Level):
    def __init__(self, man, pde):
        super().__init__(man, pde)



        self.changebackground(bg=r"data\aigame\assets\sprites\ui\bg.png")

        self.objectManager.add_object(obj=SpriteElement(man=self.objectManager,pde=pde, position=[320, 64], scale=[196,64],useCenterForPosition=True, sprite=r"data\aigame\assets\sprites\ui\foolmetwice.png"))
        
        for inx, player in enumerate(self.pde.game.playerinfo.keys()):
            if self.pde.game.playerinfo[player]["role"] == "questioneer":
                asker = self.pde.game.playerinfo[player]["name"]

        text = f"{asker} asks... {self.pde.game.question}"
        self.objectManager.add_object(obj=FadeInTextElement(man=self.objectManager,pde=pde, position=[320, 240], scale=[400,32],useCenterForPosition=True, text=text))

        if self.pde.game.player.role == "answerer":
            self.objectManager.add_object(obj=ButtonElement(man=self.objectManager,pde=pde, position=[220, 320], scale=[64,32],useCenterForPosition=True, sprite=r"data\aigame\assets\sprites\ui\manual.png", bind=self.send_manual_response))
            self.objectManager.add_object(obj=ButtonElement(man=self.objectManager,pde=pde, position=[420, 320], scale=[64,32],useCenterForPosition=True, sprite=r"data\aigame\assets\sprites\ui\ai-gen.png", bind=self.send_ai_response))

    def send_manual_response(self):
        self.objectManager.add_object(obj=TextBoxElement(man=self.objectManager,pde=self.pde, position=[320, 140], scale=[240,64],useCenterForPosition=True)).confirm_event.bind(self.confirm_manual_response)

    def confirm_manual_response(self, text):
        self.pde.game.send_manual_response(response=text)

    def send_ai_response(self):
        self.pde.game.send_ai_response()