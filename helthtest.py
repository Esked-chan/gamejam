import pygame
import sys
import os
import random

# VARIABLES

main = True
worldx = 1080
worldy = 608
fps = 60
ani = 4
ALPHA = (0, 255, 0)

# OBJECTS		

class Player(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.images = []
        for p in range(0, 5):
            img = pygame.image.load(os.path.join('images', 'Mainguy_frame_' + str(p) +'.png')).convert()
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
        xy = self.rect.x
        yx = self.rect.y
        if xy < 0:
            self.frame += 1
            if self.frame > 3 * ani:
                self.frame = 0
            self.image = pygame.transform.flip(self.images[self.frame // ani], True, False)
        if xy > 0:
            self.frame += 1
            if self.frame > 3 * ani:
                self.frame = 0
            self.image = self.images[self.frame // ani]
        if yx < 0:
            self.frame += 1
            if self.frame > 3 * ani:
                self.frame = 0
            self.image = pygame.transform.flip(self.images[self.frame // ani], True, False)
        if yx > 0:
            self.frame += 1
            if self.frame > 3 * ani:
                self.frame = 0
            self.image = self.images[self.frame // ani]
    

class Enemy(Player):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.images = []
        img = pygame.image.load(os.path.join('images', 'enemy.png')).convert()
        self.images.append(img)
        img.convert_alpha()
        img.set_colorkey(ALPHA)
        self.image = self.images[0]
        self.rect = self.image.get_rect()
        self.movex = 0
        self.movey = 0
        self.frame = 0
        self.velocityx = 5
        self.velocityy = 5
        self.hitbox = self.rect
        self.hitbox.w += self.velocityx
        self.hitbox.h += self.velocityy
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
        img.convert_alpha()
        img.set_colorkey(ALPHA)
        self.image = self.images[0]
        self.rect = self.image.get_rect()

class Bullet(Player):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.images = []
        img = pygame.image.load(os.path.join('images', 'Bullet.png')).convert()
        img = pygame.transform.scale(img, (20, 30))
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
    def update(self):
        self.rect.x = self.rect.x + self.movex

class Helthbar(Player):
    def __init__(self,x,y,z):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.Surface((200, 30))
        self.image.fill((x, y, z))
        self.rect = self.image.get_rect()
    


        

# SETUP

abspath = os.path.abspath(__file__)
dname = os.path.dirname(abspath)
os.chdir(dname)

clock = pygame.time.Clock()
pygame.init()
world = pygame.display.set_mode([worldx, worldy])
backdrop = pygame.image.load('C:/Users/toufi/Downloads/gamejam-main/gamejam-main/images/beach (1).png')
backdropbox = world.get_rect()
player = Player()

obstacle_list = pygame.sprite.Group()
for i in range (6):
    tmp2 = Obstacle()
    tmp2.rect.x = 700
    tmp2.rect.y = i * 100
    obstacle_list.add(tmp2)


enemy_list = pygame.sprite.Group()
for i in range (0,2):
    tmp = Enemy()
    if i == 0:
        tmp.rect.x = 0
        tmp.rect.y = (worldy / 2)
    else:
        tmp.rect.x = (worldx / 2)
        tmp.rect.y = 0
    enemy_list.add(tmp)
player.rect.x = 0
player.rect.y = 0
player_list = pygame.sprite.Group()
player_list.add(player)
bullet_list = pygame.sprite.Group()

helth = Helthbar(200, 30, 30)
helth.rect.x = 860
helth.rect.y = 10
helth_list = pygame.sprite.Group()
helth_list.add(helth)

helth1 = Helthbar(0,0,255)
helth1.rect.x = 860
helth1.rect.y = 50
helth1_list = pygame.sprite.Group()
helth1_list.add(helth1)

helth2 = Helthbar(0,0,255)
helth2.rect.x = 860
helth2.rect.y = 90
helth2_list = pygame.sprite.Group()
helth2_list.add(helth2)






        


# MAIN LOOP

pygame.key.set_repeat(20,20)

while main:
    """
    iii = 1

    while iii < 850:
        bullet.control(bullet.velocity , 0)
        iii += 5
        """
    fire = False
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
            if event.key == pygame.K_SPACE:
                fire = True
                pass
            
        else:
            player.moving = False
            if fire:
                bullet = Bullet()
                bullet.rect.x = player.rect.x + 60
                bullet.rect.y = player.rect.y + 50
                bullet_list.add(bullet)
                fire = False
                pass
            
        if (player.moving):
            if event.key == pygame.K_LEFT or event.key == ord('a'):
                if not (player.rect.x - player.velocity < 0):
                    player.control(-player.velocity, 0)
                for i in range (6):
                    if (pygame.Rect.colliderect(player.hitbox, obstacle_list.sprites()[i].rect)):
                        player.control(player.velocity, 0)
            if event.key == pygame.K_RIGHT or event.key == ord('d'):
                if not (player.rect.x + player.velocity > worldx - player.rect.w):
                    player.control(player.velocity, 0)
                for i in range (6):
                    if (pygame.Rect.colliderect(player.hitbox, obstacle_list.sprites()[i].rect)):
                        player.control(-player.velocity, 0)
            if event.key == pygame.K_DOWN or event.key == ord('s'):
                if not (player.rect.y + player.velocity > worldy - player.rect.h):
                    player.control(0, player.velocity)
                for i in range (6):
                    if (pygame.Rect.colliderect(player.hitbox, obstacle_list.sprites()[i].rect)):
                        player.control(0, -player.velocity)
            if event.key == pygame.K_UP or event.key == ord('w'):
                if not (player.rect.y - player.velocity < 0):
                    player.control(0, -player.velocity)
                for i in range (6):
                    if (pygame.Rect.colliderect(player.hitbox, obstacle_list.sprites()[i].rect)):
                        player.control(0, player.velocity)
            
                    
            
                


    world.blit(backdrop, backdropbox)
    player.update()
    for i in range (2):
        enemy_list.sprites()[i].control(enemy_list.sprites()[i].velocityx, enemy_list.sprites()[i].velocityy)
        enemy_list.sprites()[i].update()
        enemy_list.sprites()[i].control(-enemy_list.sprites()[i].velocityx, -enemy_list.sprites()[i].velocityy)
        if (enemy_list.sprites()[i].rect.x > (worldx - 100) or enemy_list.sprites()[i].rect.x < 0):
            enemy_list.sprites()[i].velocityx *= -1
        if (enemy_list.sprites()[i].rect.y > (worldy - 100) or enemy_list.sprites()[i].rect.y < 0):
            enemy_list.sprites()[i].velocityy *= -1
        for j in range (6):
            if (pygame.Rect.colliderect(enemy_list.sprites()[i].hitbox, obstacle_list.sprites()[j].rect)):
                enemy_list.sprites()[i].velocityx *= -1
                enemy_list.sprites()[i].velocityy *= -1

        if (pygame.Rect.colliderect(player.hitbox, enemy_list.sprites()[i].hitbox)):
            print("Collll")
                

    for i in range(len(bullet_list.sprites())):
        bullet_list.sprites()[i].control(bullet_list.sprites()[i].velocity, 0)
    
    enemy_list.draw(world)
    player_list.draw(world)
    obstacle_list.draw(world)
    bullet_list.draw(world)
    helth_list.draw(world)
    helth1_list.draw(world)
    helth2_list.draw(world)


        
    pygame.display.flip()
    clock.tick(fps)
