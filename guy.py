# Copyright (C) 2023 Riya Jain
#
# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with this program.  If not, see <http://www.gnu.org/licenses/>.
#
# Contact information:
# Riya Jain   riya1jain567@gmail.com


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
