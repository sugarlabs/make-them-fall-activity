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


class Spike:

    def __init__(self, x, y, flip, speed, path_length):
        self.x = x
        self.initial = y

        self.graphic = pygame.image.load("data/images/Spike.png")
        if flip == 1:
            self.graphic = pygame.transform.flip(self.graphic, True, False)
        self.rect = self.graphic.get_rect()

        if flip:
            self.x -= self.rect.width
        self.y = y - self.rect.height

        self.gameDisplay = pygame.display.get_surface()

        self.speed = speed
        self.path_length = path_length

    def update(self):
        self.draw()
        self.y -= self.speed
        if self.y < (self.initial - self.path_length):
            return True
        return False

    def draw(self):
        self.gameDisplay.blit(self.graphic, (self.x, self.y))
