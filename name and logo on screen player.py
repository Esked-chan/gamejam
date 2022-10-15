# import package to create a game
import pygame

pygame.init()

# creating variable for display
display_width = 1920
display_height = 1080

display = pygame.display.set_mode((display_width, display_height))

# gave a name to the game
pygame.display.set_caption('Flame Frame')

# make an icon of the game
icon = pygame.image.load('Logo.png')
pygame.display.set_icon(icon)



# funciton to start the game

game = True

# when an user click "exit" the game is finished
while game:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            quit()
    # create a colorful background
    display.fill((255, 255, 255))
    pygame.display.update()
