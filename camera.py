import pygame
from player import Player

class Camera(Player):
    def __init__(self):
        super().__init__()
        self.offset = pygame.math.Vector2()
        self.width = 960
        self.height = 540 
    def center_target_camera(self, target):
        self.offset.x = min(720, max(0, target[0]))
        self.offset.y = min(450, max(0,target[1])) + 20

