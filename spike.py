import pygame


class Spike:

    def __init__(self, x, y, flip, speed, path_length):
        self.graphic = pygame.image.load("data/images/Spike.png")
        if flip == 1:
            self.graphic = pygame.transform.flip(self.graphic, True, False)
        self.rect = self.graphic.get_rect()

        self.initial = y

        self.x = x
        if flip:
            self.x -= self.rect.width
        self.y = y - self.rect.height

        self.gameDisplay = pygame.display.get_surface()

        self.speed = speed
        self.path_length = path_length

    def update(self):
        self.draw()
        self.y -= self.speed
        if (self.y < self.initial - self.path_length):
            return True
        return False

    def draw(self):
        self.gameDisplay.blit(self.graphic, (self.x, self.y))
