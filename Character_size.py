import pygame

# intialize the pygame
#pygame.init()

# screen width
screen_X = 1920
screen_Y = 1080


# create the screen
screen = pygame.display.set_mode((screen_X, screen_Y))

# caption and icon
pygame.display.set_caption("one of the game ever created")
icon = pygame.image.load("Characters/Mainguy_frame_0.png")
pygame.display.set_icon(icon)


# Player
playerimg = pygame.image.load("Characters/Mainguy_frame_0.png")

# Player size
playerimg = pygame.transform.scale(playerimg, (200, 300))

# player position
player_X = 370
player_Y = 480


def player():
    screen.blit(playerimg, (player_X, player_Y))

# Game loop
running = True
while running:



    # RGB = Red, Green, Blue
    screen.fill((0, 0, 0))



    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False



    player()
    pygame.display.update()
pygame.quit()