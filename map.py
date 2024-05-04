import pygame as pg
import camera
from pytmx.util_pygame import load_pygame

camera = camera.Camera()

class TiledMap:
    def __init__(self, filename):
        self.tmx_data = load_pygame(filename)
        self.width = self.tmx_data.width*self.tmx_data.tilewidth
        self.height = self.tmx_data.height*self.tmx_data.tileheight
        self.falling = True
        self.active = True

    def render(self, surface, player):
        camera.center_target_camera(player)
        for layer in self.tmx_data.visible_layers:
            if hasattr(layer, 'data'):
                if not layer.name.startswith('floor-flt'):
                    for x, y, gid in layer:
                        tile = self.tmx_data.get_tile_image_by_gid(gid)
                        if tile:
                            tile_rect = tile.get_rect()
                            tile_rect.topleft = (x*self.tmx_data.tilewidth, y*self.tmx_data.tileheight)
                            offset_pos = tile_rect.topleft - camera.offset * 2
                            surface.blit(tile, offset_pos)
                
                                    



    def ground_rect(self, player, surface, object):
        for layer in self.tmx_data.visible_layers:
            if hasattr(layer,'data'):
                if layer.name == 'Floor':
                    for x, y, gid in layer:
                        tile = self.tmx_data.get_tile_image_by_gid(gid)
                        if tile:
                            tile_rect = tile.get_rect()
                            tile_rect.topleft = (x*32, y*32 )
                            tile_rect.topleft = tile_rect.topleft - camera.offset * 2

                            if tile_rect.colliderect((player[0] + object.vel_x , player[1], player[2] + 4, player[3])):
                                object.vel_x = 0

                            if tile_rect.colliderect((player[0], player[1] + 2, player[2],player[3])):
                                object.vel_y = 0
                                if object.jumping:
                                    object.vel_y = -30 
                            
                            if tile_rect.colliderect((player[0], player[1] - 2, player[2],player[3])):
                                object.vel_y = tile_rect.bottom - player.top




                                                               
                            

                if layer.name == 'chest':
                    for a, b, surf in layer:
                        winning = self.tmx_data.get_tile_image_by_gid(surf)
                        if winning:
                            win_rect = winning.get_rect()
                            win_rect.topleft = (x*self.tmx_data.tilewidth, y*self.tmx_data.tileheight )
                            win_rect.topleft = win_rect.topleft - camera.offset * 2
                            pg.draw.rect(surface, 'blue', win_rect,2)

                            if win_rect.colliderect(player):
                                self.active = False


