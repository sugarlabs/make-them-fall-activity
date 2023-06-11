import pygame


class Guy:

    def __init__(self, x_range, y):
        self.graphic = pygame.image.load("data/images/man.png")
        self.rect = self.graphic.get_rect()

        self.y = y
        self.x_range = x_range
        self.x = self.x_range[0]
        self.x_range[1] = self.x_range[1] - self.rect.width

        self.gameDisplay = pygame.display.get_surface()

        self.moving = False
        self.position = 1  # 1 -> left (x_range[0]) ; -1 -> right (x_range[1])
        self.speed = 25

    def move(self):
        if not self.moving:
            self.moving = True

    def update(self):
        if self.moving:
            self.x += self.position * self.speed
            if self.x > self.x_range[1]:
                self.graphic = pygame.transform.flip(self.graphic, True, False)
                self.x = self.x_range[1]
                self.position = -1
                self.moving = False
            if self.x < self.x_range[0]:
                self.graphic = pygame.transform.flip(self.graphic, True, False)
                self.x = self.x_range[0]
                self.moving = False
                self.position = 1
        self.draw()

    def draw(self):
        self.gameDisplay.blit(self.graphic, (self.x, self.y))

    def check_collision(self, other_x, other_y, other_width, other_height):
        self_rect = pygame.Rect(self.x, self.y,
                                self.rect.width,
                                self.rect.height)
        other_rect = pygame.Rect(other_x, other_y,
                                 other_width,
                                 other_height)
        if self_rect.colliderect(other_rect):
            return True
