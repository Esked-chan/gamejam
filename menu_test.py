import pygame
from enum import Enum
import os
from refactored_very_epic_code_less_go import *
from moviepy.editor import *
from video_preview import *

def drawMenu():
    pass


def drawGame(worldx, worldy):
    gameStart(worldx, worldy)


def drawOptions():
    pass


def drawGameOver(worldx, worldy, win):
    bg = pygame.image.load("images/forest.png")
    bg = pygame.transform.scale(bg, (worldx, worldy))
    font = pygame.font.Font('herculanum.ttf', 64)
    text = font.render('YOU WON', True, (200, 200, 200))
    textRect = text.get_rect()
    textRect.center = (worldx / 2, worldy / 2 - 50)

    text2 = font.render("PLAY AGAIN?", True, (200, 200, 200))
    textRect2 = text2.get_rect()
    textRect2.center = (worldx / 2, worldy / 2 + 50)

    text3 = font.render("QUIT", True, (200, 200, 200))
    textRect3 = text3.get_rect()
    textRect3.center = (worldx / 2, worldy / 2 + 150)

    win.blit(bg, (0, 0))
    win.blit(text, textRect)
    win.blit(text2, textRect2)
    win.blit(text3, textRect3)

    main = True
    while main:
        mouse_pos = pygame.mouse.get_pos()

        event = pygame.event.poll()
        if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
            mouseDown = True
        else:
            mouseDown = False
        if (textRect2.collidepoint(mouse_pos) and mouseDown):
            drawGame(worldx, worldy)
            main = False
        if (textRect3.collidepoint(mouse_pos) and mouseDown):
            pygame.quit; sys.quit()

        win.blit(bg, (0, 0))
        win.blit(text, textRect)
        win.blit(text2, textRect2)
        win.blit(text3, textRect3)

        pygame.display.update()



def gameEnded():
    pygame.quit()
    sys.exit()






def main():
    class gameState(Enum):
        MENU = 0
        INGAME = 1
        OPTIONS = 2
        GAMEOVER = 3
        ENDED = 4

    worldx = 800
    worldy = 600

    abspath = os.path.abspath(__file__)
    dname = os.path.dirname(abspath)
    os.chdir(dname)

    pygame.init()

    win = pygame.display.set_mode((worldx, worldy))
    pygame.display.set_caption('Flame Frame')
    icon = pygame.image.load('images/Logo.png')
    pygame.display.set_icon(icon)

    #videoPlay(worldx, worldy)

    font = pygame.font.Font('herculanum.ttf', 32)
    text = font.render('START', True, (30, 30, 30))
    textRect = text.get_rect()
    textRect.center = (650, 260)

    mouse_pos = pygame.mouse.get_pos()

    run = True
    mouseDown = False

    bg = pygame.image.load("images/map.png")
    bg = pygame.transform.scale(bg, (worldx, worldy))

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
            drawGame(worldx, worldy)
            state = gameState.GAMEOVER
        elif (state == gameState.OPTIONS):
            drawOptions()
        elif (state == gameState.GAMEOVER):
            drawGameOver(worldx, worldy, win)
        elif (state == gameState.ENDED):
            gameEnded()

        
        pygame.display.update() 
        

if __name__ == "__main__":
    main()
