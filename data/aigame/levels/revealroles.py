from data.engine.level.level import Level
from data.engine.widgets.element.e_button import ButtonElement
from data.engine.widgets.element.e_sprite import SpriteElement

class RevealRolesLevel(Level):
    def __init__(self, man, pde):
        super().__init__(man, pde)

        self.changebackground(bg=r"data\aigame\assets\sprites\ui\bg.png")

        self.pde.network_manager.network.send_event(event={'message_type': 'event', 'message_data': {'event_name': 'retrieve_playerinfo', 'event_args': {'id': self.pde.game.player._id}}})

        self.objectManager.add_object(obj=SpriteElement(man=man,pde=pde, position=[320, 64], scale=[196,64],useCenterForPosition=True, sprite=r"data\aigame\assets\sprites\ui\foolmetwice.png"))
        

        print(f"role: {self.pde.game.player.role}")
        role = self.pde.game.player.role

        if role == "answerer":
            self.objectManager.add_object(obj=SpriteElement(man=man,pde=pde, position=[320, 240], scale=[196,64],useCenterForPosition=True, sprite=r"data\aigame\assets\sprites\ui\uranswerer.png"))
        elif role == "questioneer":
            self.objectManager.add_object(obj=SpriteElement(man=man,pde=pde, position=[320, 240], scale=[196,64],useCenterForPosition=True, sprite=r"data\aigame\assets\sprites\ui\urquestioner.png"))
        elif role == "voter":
            self.objectManager.add_object(obj=SpriteElement(man=man,pde=pde, position=[320, 240], scale=[196,64],useCenterForPosition=True, sprite=r"data\aigame\assets\sprites\ui\urvoter.png"))
