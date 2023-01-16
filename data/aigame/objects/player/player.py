import pygame
from data.engine.object.object import Object
from data.engine.player.player_controller import PlayerController


class AIQuip_PlayerController(PlayerController):
    def __init__(self, owner):
        super().__init__(owner)

    def on_input(self, input):
        return


class AIQuip_PlayerObject(Object):
    def __init__(self, man, pde):
        super().__init__(man, pde)
        self.ishost = False
        self.name = 'DefaultName'
        self._id = -1

        self.components["PlayerController"] = AIQuip_PlayerController(owner=self)
        