import pygame
import sys
import os

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
        self.images = []
        img = pygame.image.load(os.path.join('images', 'hero.png')).convert()
        self.images.append(img)
        img.convert_alpha()
        img.set_colorkey(ALPHA)
        self.image = self.images[0]
        self.rect = self.image.get_rect()
        self.movex = 0
        self.movey = 0
        self.frame = 0
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
    def control(self,x,y):
        self.movex += x
        self.movey += y
    def update(self):
        self.rect.x = self.rect.x + self.movex
        self.rect.y = self.rect.y + self.movey

class Stone(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.images = []
        img = pygame.image.load(os.path.join('images', 'stones.png')).convert()
        self.images.append(img)
        img.convert_alpha()
        img.set_colorkey(ALPHA)
        self.image = self.images[0]
        self.rect = self.image.get_rect()

# SETUP

abspath = os.path.abspath(__file__)
dname = os.path.dirname(abspath)
os.chdir(dname)

clock = pygame.time.Clock()
pygame.init()
world = pygame.display.set_mode([worldx, worldy])
backdrop = pygame.image.load(os.path.join('images', 'beach.png'))
backdropbox = world.get_rect()
player = Player()
enemy_list = pygame.sprite.Group()
for i in range (2):
    tmp = Enemy()
    tmp.rect.x = 100 + i * 50
    tmp.rect.y = 100 + i * 50
    enemy_list.add(tmp)
player.rect.x = 0
player.rect.y = 0
player_list = pygame.sprite.Group()
player_list.add(player)
steps = 10
stone = Stone()
stone.rect.x = 800
stone.rect.y = 400
object_list = pygame.sprite.Group()
object_list.add(stone)

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
                sys.exit()
                main = False

    if pygame.Rect.colliderect(player.rect, stone.rect) == True:
        print("Collision!")
    world.blit(backdrop, backdropbox)
    player.update()
    for i in range (2):
        enemy_list.sprites()[i].control(steps / 10, 0)
        enemy_list.sprites()[i].update()
        enemy_list.sprites()[i].control(-steps / 10, 0)
    enemy_list.draw(world)
    player_list.draw(world)
    object_list.draw(world)
    pygame.display.flip()
    clock.tick(fps)
