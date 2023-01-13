import pygame
from data.engine.object.object import Object
from data.engine.player.player_controller import PlayerController


class AIQuip_PlayerController(PlayerController):
    def __init__(self, owner):
        super().__init__(owner)
        self._id = -1
        self.name = 'DefaultName'

    def on_input(self, input):
        if input == pygame.K_SPACE:
            self.owner.pde.network_manager.activate()
        if input == pygame.K_s:
            self.owner.pde.game.startgame()


class AIQuip_PlayerObject(Object):
    def __init__(self, man, pde):
        super().__init__(man, pde)
        self.ishost = False

        self.components["PlayerController"] = AIQuip_PlayerController(owner=self)
        