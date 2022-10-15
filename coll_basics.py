import pygame
import sys
import os

# VARIABLES

main = True
worldx = 800
worldy = 600
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
        self.moving = False
        self.velocity = 10
        self.hitbox = self.rect
        self.hitbox.w += self.velocity
        self.hitbox.h += self.velocity
    def control(self,x,y):
        self.rect.x += x
        self.rect.y += y
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
        self.velocityx = 5
        self.velocityy = 5
    def control(self,x,y):
        self.movex += x
        self.movey += y
    def update(self):
        self.rect.x = self.rect.x + self.movex
        self.rect.y = self.rect.y + self.movey

class Obstacle(Player):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.images = []
        img = pygame.image.load(os.path.join('images', 'stones.png')).convert()
        self.images.append(img)
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
    tmp.rect.x = 300 + i * 150
    tmp.rect.y = 300 + i * 150
    enemy_list.add(tmp)
player.rect.x = 0
player.rect.y = 0
player_list = pygame.sprite.Group()
player_list.add(player)
stone = Obstacle()
stone.rect.x = worldx / 2
stone.rect.y = worldy / 2
obstacle_list = pygame.sprite.Group()
obstacle_list.add(stone)

# MAIN LOOP

pygame.key.set_repeat(10,10)

while main:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit(); sys.exit()
            main = False
        if event.type == pygame.KEYDOWN:
            player.moving = True
            if event.key == ord('q'):
                pygame.quit()
                sys.exit()
                main = False
        if event.type == pygame.KEYUP:
            player.moving = False
        if (player.moving):
            if event.key == pygame.K_LEFT or event.key == ord('a'):
                if not (player.rect.x - player.velocity < 0) and not (pygame.Rect.colliderect(player.hitbox, stone.rect)):
                    player.control(-player.velocity, 0)
            if event.key == pygame.K_RIGHT or event.key == ord('d'):
                if not (player.rect.x + player.velocity > worldx - player.rect.w) and not (pygame.Rect.colliderect(player.hitbox, stone.rect)):
                    player.control(player.velocity, 0)
            if event.key == pygame.K_DOWN or event.key == ord('s'):
                if not (player.rect.y + player.velocity > worldy - player.rect.h) and not (pygame.Rect.colliderect(player.hitbox, stone.rect)):
                    player.control(0, player.velocity)
            if event.key == pygame.K_UP or event.key == ord('w'):
                if not (player.rect.y - player.velocity < 0) and not (pygame.Rect.colliderect(player.hitbox, stone.rect)):
                    player.control(0, -player.velocity)
            
                


    world.blit(backdrop, backdropbox)
    #player.update()
    for i in range (2):
        enemy_list.sprites()[i].control(enemy_list.sprites()[i].velocityx, enemy_list.sprites()[i].velocityy)
        enemy_list.sprites()[i].update()
        enemy_list.sprites()[i].control(-enemy_list.sprites()[i].velocityx, -enemy_list.sprites()[i].velocityy)
        if (enemy_list.sprites()[i].rect.x > (worldx - 100) or enemy_list.sprites()[i].rect.x < 0):
            enemy_list.sprites()[i].velocityx *= -1
        if (enemy_list.sprites()[i].rect.y > (worldy - 100) or enemy_list.sprites()[i].rect.y < 0):
            enemy_list.sprites()[i].velocityy *= -1
            
    enemy_list.draw(world)
    player_list.draw(world)
    obstacle_list.draw(world)
    pygame.display.flip()
    clock.tick(fps)
