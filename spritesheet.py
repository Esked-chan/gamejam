import pygame


class SpriteSheet(object):
    def __init__(self, filename):
        try:
            self.sheet = pygame.image.load(filename).convert()
        except pygame.error as e:
            print(F"Unable to load spritesheet image: {filename}")
            raise SystemExit(e)


    def image_at(self, rectangle, colorkey = None):
        rect = pygame.Rect(rectangle)
        image = pygame.Surface(rect.size).convert()
        image.blit(self.sheet, (0, 0), rect)
        if colorkey is not None:
            if colorkey is -1:
                colorkey = image.get_at((0,0))
            image.set_colorkey((0, 255, 0), pygame.RLEACCEL)
        return image


    def images_at(self, rects, colorkey = None):
        return [self.image_at(rect, colorkey) for rect in rects]


    def load_strip(self, rect, image_count, colorkey = None):
        tups = [(rect[0]+rect[2]*x, rect[1], rect[2], rect[3])
                for x in range(image_count)]
        return self.images_at(tups, colorkey)


    def load_grid_images(self, num_frames, sprite_size):
        sheet_rect = self.sheet.get_rect()
        sprite_size = sprite_size

        sprite_rects = []

        for i in range(num_frames):
            x = i * sprite_size
            sprite_rect = (x, 0, sprite_size, sprite_size)
            sprite_rects.append(sprite_rect)
     
        return self.images_at(sprite_rects, None)
    