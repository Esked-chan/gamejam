import pygame

class ScaleSprite(pygame.sprite.Sprite):
    def __init__(self, center, image):
        super().__init__()
        self.original_image = image
        self.image = image
        self.rect = self.image.get_rect(center = center)
        self.mode = 1
        self.grow = 0

    def update(self):
        if self.grow > 100:
            self.mode = -1
        if self.grow < 1:
            self.mode = 1
        self.grow += 1 * self.mode

        orig_x, orig_y = self.original_image.get_size()
        size_x = orig_x + round(self.grow)
        size_y = orig_y + round(self.grow)
        self.image = pygame.transform.scale(self.original_image, (size_x, size_y))
        self.rect = self.image.get_rect(center = self.rect.center)

pygame.init()
window = pygame.display.set_mode((300, 300))
clock = pygame.time.Clock()

sprite = ScaleSprite(window.get_rect().center, pygame.image.load("Mainguy_frame_0.png"))
group = pygame.sprite.Group(sprite)

run = True
while run:
    clock.tick(60)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False

    group.update()

    window.fill(0)
    group.draw(window)
    pygame.display.flip()

pygame.quit()
exit()