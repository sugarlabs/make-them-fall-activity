
import pygame


class Button:

    def __init__(self, x, y, image_path, action, text=None):
        self.graphic = pygame.image.load(image_path)
        self.rect = self.graphic.get_rect()

        self.x = x
        self.y = y
        self.rect.x = self.x
        self.rect.y = self.y

        self.text = text
        self.gameDisplay = pygame.display.get_surface()

        self.action = action

        self.draw()

    def draw(self):
        if self.hovered():
            scaled_graphic = pygame.transform.scale(
                self.graphic, (self.rect.width + 10, self.rect.height + 5))
            self.gameDisplay.blit(scaled_graphic, (self.x - 5, self.y))
        else:
            self.gameDisplay.blit(self.graphic, (self.x, self.y))

        if self.text is not None:
            text_rect = self.text.get_rect()
            self.gameDisplay.blit(self.text, (self.x + self.rect.width / 2 -
                                  text_rect.width / 2, self.y + self.rect.height - 1.5 * text_rect.height))

    def hovered(self):
        return self.rect.collidepoint(pygame.mouse.get_pos())

    def update(self):
        self.draw()

        if self.hovered() and pygame.mouse.get_pressed()[0] == 1:
            self.action()
            