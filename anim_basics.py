import pygame
import os
import sys
from spritesheet import SpriteSheet

# VARIABLES

main = True
worldx = 1920
worldy = 1080
fps = 60
ani = 4
ALPHA = (0, 255, 0)

# OBJECTS

class Player(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.movex = 0
        self.movey = 0
        self.frame = 0
        filename = "animation_test.png"
        ss = SpriteSheet(filename)
        self.test = ss.image_at((0, 0, 100, 100), None)
        self.rect = self.test.get_rect()
        #self.images = ss.load_grid_images(6, 100)
        #self.rect = self.images[0].get_rect()
    def control(self,x,y):
        self.movex += x
        self.movey += y
    def update(self):
        self.rect.x = self.rect.x + self.movex
        self.rect.y = self.rect.y + self.movey
  



class Enemy(Player):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.images = []
        img = pygame.image.load(os.path.join('images', 'enemy.png')).convert()
        self.images.append(img)
        self.image = self.images[0]
        self.rect = self.image.get_rect()
        self.movex = 0
        self.movey = 0
        self.frame = 0


# SETUP

abspath = os.path.abspath(__file__)
dname = os.path.dirname(abspath)
os.chdir(dname)

clock = pygame.time.Clock()
pygame.init()
world = pygame.display.set_mode([worldx, worldy])
player = Player()
#backdrop = pygame.image.load(os.path.join('images', 'beach.png'))
#backdrop = player.images[0]
backdrop = player.test
backdropbox = world.get_rect()

enemy_list = pygame.sprite.Group()
for i in range (2):
    tmp = Enemy()
    tmp.rect.x = 100 + i * 50
    tmp.rect.y = 100 + i * 50
    enemy_list.add(tmp)
player.rect.x = 0
player.rect.y = 0
steps = 10
index = 0

# MAIN LOOP

while main:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit(); sys.exit()
            main = False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT or event.key == ord('a'):
                player.control(-steps, 0)
            if event.key == pygame.K_RIGHT or event.key == ord('d'):
                player.control(steps, 0)
            if event.key == pygame.K_DOWN or event.key == ord('s'):
                player.control(0, steps)
            if event.key == pygame.K_UP or event.key == ord('w'):
                player.control(0, -steps)

        if event.type == pygame.KEYUP:
            if event.key == pygame.K_LEFT or event.key == ord('a'):
                player.control(steps, 0)
            if event.key == pygame.K_RIGHT or event.key == ord('d'):
                player.control(-steps, 0)
            if event.key == pygame.K_DOWN or event.key == ord('s'):
                player.control(0, -steps)
            if event.key == pygame.K_UP or event.key == ord('w'):
                player.control(0, steps)
            if event.key == ord('q'):
                pygame.quit()
                quit()
                main = False
    world.blit(backdrop, backdropbox)
    player.update()
    for i in range (len(enemy_list.sprites())):
        enemy_list.sprites()[i].control(steps / 10, 0)
        enemy_list.sprites()[i].update()
        enemy_list.sprites()[i].control(-steps / 10, 0)
    enemy_list.draw(world)
    #world.blit(player.images[index], (0, 0))
    world.blit(player.test, (0, 0))
    pygame.display.update()
    if (index == 5):
        index = 0
    else:
        index += 1
    clock.tick(fps)
