import pygame
from sprites import Animation, SpriteSheet

idle = SpriteSheet(pygame.image.load('data/player/idle.png'))
run = SpriteSheet(pygame.image.load('data/player/run.png'))
jump = SpriteSheet(pygame.image.load('data/player/jump.png'))


class Player():
    def __init__(self):
        self.idle_list = Animation(idle)
        self.run_list = Animation(run)
        self.jump_list = Animation(jump)
        self.idle_list.load_image(6)
        self.run_list.load_image(8)
        self.jump_list.load_image(11)
        self.action = 0
        self.x = -20
        self.y = -50
        self.vel_x = 0
        self.vel_x = 0
        self.vel_y = 0
        self.jumping = False
        self.last_action = 0
        self.right = True
        self.left = True
        self.grav_y = 0

    def animate(self):
        self.idle_list.cooldown(600)
        self.run_list.cooldown(100)
        self.jump_list.cooldown(100)

    def move_right(self):
        if self.right:
            self.vel_x = 1
            self.action = 1
            self.last_action = 0
    
    def move_left(self):
        if self.left:
            self.vel_x = -1
            self.action = 2
            self.last_action = 1

    def move_up(self):
        self.vel_y = -2

    # def move_down(self):
    #     self.vel_y = 1

    def jump(self):
        self.jumping = True
        self.grav_y = -20
        self.action = 3

    def gravity(self):
        self.vel_y = 1

    def keyup(self):
        self.vel_x = 0
        self.vel_y = 0
        self.action = 0
        self.jumping = False

    def update(self):
        self.x += self.vel_x
        self.y += self.vel_y
        self.gravity()
        

    def render(self,surf):
        
        if self.action == 0 and self.last_action == 0:
            rect = self.idle_list.list[self.idle_list.frame].get_rect(midbottom = (self.x +85,self.y + 134))
            rect.width -= 60
            rect.height -= 30
            surf.blit(self.idle_list.list[self.idle_list.frame],(self.x,self.y))

        if self.action == 0 and self.last_action == 1:
            rect = self.idle_list.f_list[self.idle_list.frame].get_rect(midbottom = (self.x +85,self.y + 134))
            surf.blit(self.idle_list.f_list[self.idle_list.frame],(self.x,self.y))
            rect.width -= 60
            rect.height -= 30

        if self.action == 1:
            rect = self.run_list.list[self.run_list.frame].get_rect(midbottom = (self.x + 85,self.y + 134))
            surf.blit(self.run_list.list[self.run_list.frame],(self.x,self.y))
            rect.width -= 60
            rect.height -= 30

        if self.action == 2:
            rect = self.run_list.f_list[self.run_list.frame].get_rect(midbottom = (self.x +85,self.y + 134))
            surf.blit(self.run_list.f_list[self.run_list.frame],(self.x,self.y))
            rect.width -= 60
            rect.height -= 30

        if self.action == 3 and self.last_action == 0:
            rect = self.jump_list.list[self.jump_list.frame].get_rect(midbottom = (self.x +85,self.y + 134))
            surf.blit(self.jump_list.list[self.jump_list.frame],(self.x,self.y))
            rect.width -= 60
            rect.height -= 30

        if self.action == 3 and self.last_action == 1:
            rect = self.jump_list.f_list[self.jump_list.frame].get_rect(midbottom = (self.x +85,self.y + 134))
            surf.blit(self.jump_list.f_list[self.jump_list.frame],(self.x,self.y))
            rect.width -= 60
            rect.height -= 30


        return rect
