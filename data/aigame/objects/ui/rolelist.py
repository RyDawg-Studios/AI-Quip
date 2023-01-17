import pygame
from data.engine.actor.actor import Actor
from data.engine.widgets.text import TextComponent

class RoleList(Actor):
    def __init__(self, man, pde, position=..., scale=..., checkForOverlap=True, checkForCollision=True, useCenterForPosition=False, lifetime=-1, text=''):
        super().__init__(man, pde, position, scale, checkForOverlap, checkForCollision, useCenterForPosition, lifetime)
        self.text = text
        self.opacity = 0

    def construct(self):
        super().construct()
        self.components["role"] = TextComponent(owner=self, text=self.text, font=pygame.font.SysFont('impact.ttf', 72), layer=3)



    def update(self):
        super().update()
        if self.opacity <= 255:
            self.opacity += 1
            self.components["role"].sprite.opacity = self.opacity
