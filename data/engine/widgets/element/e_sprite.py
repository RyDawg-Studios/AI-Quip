from data.engine.actor.actor import Actor
from data.engine.sprite.sprite_component import SpriteComponent

class SpriteElement(Actor):
    def __init__(self, man, pde, position=..., scale=..., checkForOverlap=False, checkForCollision=False, useCenterForPosition=False, lifetime=-1, sprite='', layer=0):
        super().__init__(man, pde, position, scale, checkForOverlap, checkForCollision, useCenterForPosition, lifetime)
        self.sprite = sprite
        self.layer=layer

    def construct(self):
        super().construct()
        self.components["Sprite"] = SpriteComponent(owner=self, sprite=self.sprite, layer=self.layer)
        return
