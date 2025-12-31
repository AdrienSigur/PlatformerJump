import pygame # type: ignore
from Player import Player
from debuggrid import debug_grid
from Environnement import Block

# pygame setup
pygame.init()
screen = pygame.display.set_mode((1280, 720))
clock = pygame.time.Clock()
running = True
dt = 0

green = (50, 200, 50)
brown = (102, 51, 0)

mur_droit = Block(700,450,250,270, brown)
ground = Block(0, 670, 1280, 50 , brown) 
mur_haut = Block(700, 440, 250, 20 , green)    
groundGrass = Block(0, 660, 1280, 10 , green) 

Environnement = [ ground , groundGrass , mur_droit , mur_haut ]
Sky = pygame.image.load('Models\\sky.png').convert()
player = Player(screen.get_width() , screen.get_height())


# background = pygame.transform.scale(Sky , (screen.get_width(), screen.get_height()))

while running:
    # poll for events
    # pygame.QUIT event means the user clicked X to close your window
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # fill the screen with a color to wipe away anything from last frame
    screen.fill("Grey")
    # debug_grid(screen)
    player.draw(screen)

    player.move(dt , Environnement)

    for Drawing in Environnement:
        Drawing.draw(screen)

    # flip() the display to put your work on screen
    pygame.display.flip()

    dt = clock.tick(60) / 1000 

pygame.quit()