import pygame
import sys
import os

worldx = 800
worldy = 600
fps = 60
ani = 10
ALPHA = (0, 255, 0)

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
        self.rect.x = 50
        self.rect.y = 50
        self.frame = 0
        self.velocityX = 0
        self.velocityY = 0
        self.speed = 5
        self.hitbox = self.rect
        self.hitbox.w += self.speed
        self.hitbox.h += self.speed
        self.facing = 1 # -1: LEFT    0: UP    1: RIGHT    2: DOWN
        self.hit = False
        self.reloading = 500
        self.flipped = False

    def move(self):
        if (self.rect.x < 0):
            self.velocityX = 1
        if (self.rect.x + self.rect.w > worldx):
            self.velocityX = -1
        if (self.rect.y - self.speed < 0):
            self.velocityY = 1
        if (self.rect.y + self.rect.h > worldy):
            self.velocityY = -1 

        self.rect.x += self.velocityX
        self.rect.y += self.velocityY

    def coll_adj(self, rectB):
        #self.velocityX = 0
        #self.velocityY = 0

        array = [0, 0, 0, 0]
        # I tried to make comments and they made this even more confusing

        tmp = abs(self.rect.x - (rectB.x + rectB.w))
        array[0] = tmp

        tmp = abs(self.rect.y - (rectB.y + rectB.h))
        array[1] = tmp

        tmp = abs(self.rect.x - (rectB.x - self.rect.w))
        array[2] = tmp

        tmp = abs(self.rect.y - (rectB.y - self.rect.h))
        array[3] = tmp

        min_ix = 0
        for i in range(1, 4):
            if (array[i] < array[min_ix]):
                min_ix = i

        if min_ix == 0:
            while(pygame.Rect.colliderect(self.rect, rectB)):
                self.rect.x += 1
        if min_ix == 1:
            while(pygame.Rect.colliderect(self.rect, rectB)):
                self.rect.y += 1
        if min_ix == 2:
            while(pygame.Rect.colliderect(self.rect, rectB)):
                self.rect.x -= 1
        if min_ix == 3:
            while(pygame.Rect.colliderect(self.rect, rectB)):
                self.rect.y -= 1  
        

    def animate(self):
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
        if self.flipped:
            self.image = pygame.transform.flip(self.images[self.frame // ani], True, False)

#hERE WAS mISHA AND mERI!
class Obstacle(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.images = []
        img = pygame.image.load(os.path.join('images', 'stones.png')).convert()
        self.images.append(img)
        img.convert_alpha()
        img.set_colorkey(ALPHA)
        self.image = self.images[0]
        self.rect = self.image.get_rect()

class Bullet(pygame.sprite.Sprite):
    def __init__(self, flip):
        pygame.sprite.Sprite.__init__(self)
        self.images = []
        for fireball in range(0, 3):
            img = pygame.image.load(os.path.join('images/Fireball', 'Fireball' + str(fireball) + '.png')).convert()
            img = pygame.transform.scale(img, (60, 90))
            self.images.append(img)
            img.convert_alpha()
            img.set_colorkey(ALPHA)
            self.image = self.images[0]
            self.rect = self.image.get_rect()
        self.frame = 0
        self.speed = 10
        self.velocityX = 0
        self.velocityY = 0
        self.player_flipped = flip

    def move(self):
        if not self.player_flipped:
            self.velocityX = self.speed
        else:
            self.velocityX = -self.speed
        self.rect.x += self.velocityX
        self.rect.y += self.velocityY

    def animate(self):
        xy = self.rect.x
        yx = self.rect.y
        if xy < 0:
            self.frame += 1
            if self.frame >= 3 * ani:
                self.frame = 0
            self.image = pygame.transform.flip(self.images[self.frame // ani], True, False)
        if xy > 0:
            self.frame += 1
            if self.frame >= 3 * ani:
                self.frame = 0
            self.image = self.images[self.frame // ani]
        if yx < 0:
            self.frame += 1
            if self.frame >= 3 * ani:
                self.frame = 0
            self.image = pygame.transform.flip(self.images[self.frame // ani], True, False)
        if yx > 0:
            self.frame += 1
            if self.frame >= 3 * ani:
                self.frame = 0
            self.image = self.images[self.frame // ani]
        
        if not self.player_flipped:
            self.image = pygame.transform.flip(self.images[self.frame // ani], True, False)
        

class Enemy(Player):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.images = []
        for e1 in range (0, 7):
            img = pygame.image.load(os.path.join('images/Enemy1', 'Enemy1_' + str(e1) + '.png')).convert()
            self.images.append(img)
            img.convert_alpha()
            img.set_colorkey(ALPHA)
            self.image = self.images[0]
            self.rect = self.image.get_rect()
        self.frame = 0
        self.speed = 2
        self.velocityX = self.speed
        self.velocityY = self.speed
        self.facing = 1 # -1: LEFT    0: UP    1: RIGHT    2: DOWN
        self.hit = False

    def move(self):
        self.rect.x += self.velocityX
        self.rect.y += self.velocityY

        if (self.rect.x < 0):
            self.velocityX *= -1
        if (self.rect.x + self.rect.w > worldx):
            self.velocityX *= -1
        if (self.rect.y - self.speed < 0):
            self.velocityY *= -1
        if (self.rect.y + self.rect.h > worldy):
            self.velocityY *= -1

    def coll_adj(self, rectB):
        array = [0, 0, 0, 0]

        tmp = abs(self.rect.x - (rectB.x + rectB.w))
        array[0] = tmp

        tmp = abs(self.rect.y - (rectB.y + rectB.h))
        array[1] = tmp

        tmp = abs(self.rect.x - (rectB.x - self.rect.w))
        array[2] = tmp

        tmp = abs(self.rect.y - (rectB.y - self.rect.h))
        array[3] = tmp

        min_ix = 0
        for i in range(1, 4):
            if (array[i] < array[min_ix]):
                min_ix = i

        if min_ix == 0:
            self.velocityX = self.speed
        if min_ix == 1:
            self.velocityY = self.speed
        if min_ix == 2:
            self.velocityX = -self.speed
        if min_ix == 3:
            self.velocityY = -self.speed

    def animate(self):
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


abspath = os.path.abspath(__file__)
dname = os.path.dirname(abspath)
os.chdir(dname)

pygame.init()
clock = pygame.time.Clock()
world = pygame.display.set_mode([worldx, worldy])
backdrop = pygame.image.load(os.path.join('images', 'beach.png'))
backdropbox = world.get_rect()

player = Player()
player_list = pygame.sprite.Group()
player_list.add(player)

stone = Obstacle()
stone.rect.x = 200
stone.rect.y = 300
stone_list = pygame.sprite.Group()
stone_list.add(stone)
stone2 = Obstacle()
stone2.rect.x = 300
stone2.rect.y = 410
stone_list.add(stone2)

bullet_list = pygame.sprite.Group()
 
#guys ur crazy, PiiPiiPooPoo LETSGOOOOOOOOOOOOOOOOOOOOOOOOO

enemy1 = Enemy()
enemy1.rect.x = 200
enemy1.rect.y = 300
enemy_list = pygame.sprite.Group()
enemy_list.add(enemy1)
enemy2 = Enemy()
enemy2.rect.x = 500
enemy2.rect.y = 100
enemy_list.add(enemy2)

prev_time = pygame.time.get_ticks()

while True:

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit(); sys.exit()

    keys = pygame.key.get_pressed()
    if (keys[pygame.K_LEFT] and not keys[pygame.K_RIGHT]):
        player.facing = -1
        player.velocityX = -player.speed
        player.flipped = True
    elif (keys[pygame.K_RIGHT] and not keys[pygame.K_LEFT]):
        player.facing = 1
        player.velocityX = player.speed
        player.flipped = False
    else:
        player.velocityX = 0
    if (keys[pygame.K_UP] and not keys[pygame.K_DOWN]):
        player.facing = 0
        player.velocityY = -player.speed
    elif (keys[pygame.K_DOWN] and not keys[pygame.K_UP]):
        player.facing = 2
        player.velocityY = player.speed
    else:
        player.velocityY = 0
    if (keys[pygame.K_SPACE]):
        current_time = pygame.time.get_ticks()
        if (current_time - prev_time > player.reloading):
            bullet = Bullet(player.flipped)
            bullet.rect.x = player.rect.x
            bullet.rect.y = player.rect.y
            bullet_list.add(bullet)
            prev_time = current_time

    for i in range(len(stone_list)):
        if (pygame.Rect.colliderect(player.hitbox, stone_list.sprites()[i].rect)):
            player.coll_adj(stone_list.sprites()[i].rect)

    for i in range(len(bullet_list)):
        bullet_list.sprites()[i].move()

    for i in range(len(enemy_list)):
        for j in range(len(stone_list)):
            if (pygame.Rect.colliderect(enemy_list.sprites()[i].rect, stone_list.sprites()[j].rect)):
                enemy_list.sprites()[i].coll_adj(stone_list.sprites()[j].rect)
            enemy_list.sprites()[i].move()

    world.blit(backdrop, backdropbox)
    player.animate()
    player.move()
    for i in range(len(enemy_list.sprites())):
        enemy_list.sprites()[i].animate()
    for i in range(len(bullet_list.sprites())):
        bullet_list.sprites()[i].animate()

    player_list.draw(world)
    stone_list.draw(world)
    bullet_list.draw(world)
    enemy_list.draw(world)

    clock.tick(fps)
    pygame.display.flip()
            