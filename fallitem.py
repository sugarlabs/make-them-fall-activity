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


import pygame


class FallItem:

    def __init__(self, x, y, flip, path_length, type_="spike"):
        self.x = x
        self.initial = y

        self.type = type_

        self.graphic = pygame.image.load("data/images/Spike.png")
        if self.type == "heart":
            self.graphic = pygame.image.load("data/images/heart.png")

        if flip == 1:
            self.graphic = pygame.transform.flip(self.graphic, True, False)
        self.rect = self.graphic.get_rect()

        if flip:
            self.x -= self.rect.width
        self.y = y - self.rect.height

        self.gameDisplay = pygame.display.get_surface()

        self.path_length = path_length

    def update(self, fallitem_speed):
        self.draw()
        self.y -= fallitem_speed
        if self.y < (self.initial - self.path_length):
            return True
        return False

    def draw(self):
        self.gameDisplay.blit(self.graphic, (self.x, self.y))
