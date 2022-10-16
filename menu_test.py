import pygame
from enum import Enum
import os
from refactored_very_epic_code_less_go import *

def drawMenu():
    pass


def drawGame():
    gameStart()


def drawOptions():
    pass


def drawGameOver():
    pass


def gameEnded():
    pygame.quit()
    quit()






def main():
    class gameState(Enum):
        MENU = 0
        INGAME = 1
        OPTIONS = 2
        GAMEOVER = 3
        ENDED = 4

    pygame.init()

    win = pygame.display.set_mode((1080, 720))
    pygame.display.set_caption("peepee poopoo")

    font = pygame.font.Font('freesansbold.ttf', 32)
    text = font.render('START', True, (0, 0, 128))
    textRect = text.get_rect()
    textRect.center = (250, 250)

    mouse_pos = pygame.mouse.get_pos()

    run = True
    mouseDown = False

    path = os.path.dirname(os.path.realpath(__file__))
    # print(path)
    bg = pygame.image.load(path + "/epic_bg.png")

    state = gameState.MENU

    while run:

        win.blit(bg, (0, 0))

        mouse_pos = pygame.mouse.get_pos()

        event = pygame.event.poll()
        if event.type == pygame.QUIT:
            state = gameState.ENDED
        if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
            mouseDown = True
        else:
            mouseDown = False
        
        if (state == gameState.MENU):
            win.blit(text, textRect)
            if (textRect.collidepoint(mouse_pos) and mouseDown):
                state = gameState.INGAME
        elif (state == gameState.INGAME):
            drawGame()
        elif (state == gameState.OPTIONS):
            drawOptions()
        elif (state == gameState.GAMEOVER):
            drawGameOver()
        elif (state == gameState.ENDED):
            gameEnded()

        
        pygame.display.update() 
        

if __name__ == "__main__":
    main()
