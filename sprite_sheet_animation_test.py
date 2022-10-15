import pygame
import os

class spritesheet(object):
    def image_at(self, rectangle, colorkey = None):
        rect = pygame.Rect(rectangle)
        image = pygame.Surface(rect.size).convert()
        image.blit(self.sheet(0, 0,), rect)
        if colorkey is not None:
            if colorkey is -1:
                colorkey = image.get_at((0, 0))
            image.set_colorkey(colorkey, pygame.RLEACCEL) # RLEACCEL = Run-length encoding, you're welcome, now you understand it
        return image

    def images_at(self, rects, colorkey = None):
        return [self.image_at(rect, colorkey) for rect in rects] # why can you use a variable before even creating it? python

    def load_strip(self, rect, image_count, colorkey = None):
        tups = [(rect[0] + rect[2] * x, rect[1], rect[2], rect[3]) for x in range(image_count)] # what the fuck does this even mean?
        return self.images_at(tups, colorkey)

    def load_grid_images(self, num):
        sheet_rect = self.sheet.get_rect()
        sheet_width, sheet_height = sheet_rect.size()
        sprite_size = 100

        sprite_rects = []
        for thingy in range(num):
            x = thingy * sprite_size
            sprite_rect = (x, 0, sprite_size, sprite_size)
            sprite_rects.append(sprite_rect)

        grid_images = self.images_at(sprite_rects)
        print(F"Loaded {len(grid_images)} grid images.")
        
        return grid_images



def main():
    path = os.path.dirname(os.path.realpath(__file__))
    ss = spritesheet("path/animation_text.png")
    images = ss.load_grid_images(6)

    while True:
        event = pygame.event.poll()
        if event.type == pygame.QUIT:
            pygame.quit()
            quit()

    win = pygame.display.set_mode((500,500))
    pygame.display.set_caption("peepee poopoo")

    


if __name__== "__main__":
    main()
