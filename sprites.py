import pygame

class SpriteSheet():
    def __init__(self, image):
        self.sheet = image
    def get_image(self, frame, width, height,scale):
        image = pygame.Surface((width,height),pygame.SRCALPHA)
        image.blit(self.sheet, (0, 0), ((frame * width), 0, width, height))
        image = pygame.transform.scale(image ,(width * scale, height * scale))
        self.rect = image.get_rect()
        return image
    
class Animation():
    def __init__(self, sprite_sheet):
        self.list = []
        self.f_list = []
        self.sheet = sprite_sheet
        self.current_time = 0
        self.last_time = 0
        self.frame = 0
        self.frame_count = 0

    def load_image(self, frame_count):
        self.frame_count = frame_count
        for i in range(frame_count):
            self.list.append(self.sheet.get_image(i, 128, 128, 0.8))

        for images in self.list:
            self.f_list.append(pygame.transform.flip(images,True,False))

    def cooldown(self,sprite_cooldown):
        self.current_time = pygame.time.get_ticks()
        if self.current_time - self.last_time >= sprite_cooldown:
            self.frame  +=1
            self.last_time = self.current_time
            if self.frame >= len(self.list):
                self.frame = 0

        return self.list
    
