import pygame, sys
from map import TiledMap
from player import Player


pygame.init()


pygame.display.set_caption('Chest Heist')
screen = pygame.display.set_mode((960,540))
Clock = pygame.time.Clock()
World = TiledMap("data/map/World.tmx")
font = pygame.font.Font('data/fonts/Pixeltype.ttf', 100)


player = Player()

while World.active:
    player.animate()

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_RIGHT:
                player.move_right()
            if event.key == pygame.K_LEFT:
                player.move_left()
            if event.key == pygame.K_SPACE:
                player.jump()
            if event.key == pygame.K_w:
                player.move_up()
            # if event.key == pygame.K_DOWN:
            #     player.move_down()

        if event.type == pygame.KEYUP:
            player.keyup()

        

    
    screen.fill('black')
    offset = player.render(screen)
    print(offset)
    World.render(screen, offset)
    offset = player.render(screen)
    World.ground_rect(offset, screen, player)
    player.update()
    
    if offset.x == 20 and offset.y == 400 :
        World.active = False
    
    pygame.display.update()
    Clock.tick(60)

while True:
    screen.fill('black')
    win = font.render("You Win", False, 'white')
    screen.blit(win,(370, 20))
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
    pygame.display.update()