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


class Button:

    def __init__(self, x, y, image_path, action, text=None):
        self.graphic = pygame.image.load(image_path)
        self.rect = self.graphic.get_rect()

        self.x = x - self.rect.width // 2
        self.y = y - self.rect.height //  2
        self.rect.x = self.x
        self.rect.y = self.y

        self.text = text
        self.gameDisplay = pygame.display.get_surface()

        self.action = action

        self.press = False

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
            m_x = self.x + self.rect.width // 2 - text_rect.width // 2
            m_y = self.y + self.rect.height - 1.5 * text_rect.height
            self.gameDisplay.blit(self.text, (m_x, m_y))

    def hovered(self):
        return self.rect.collidepoint(pygame.mouse.get_pos())

    def update(self):
        self.draw()
        pressed_btn = pygame.mouse.get_pressed()[0]
        if self.press and self.hovered() and pressed_btn != 1:
            self.action()

        if self.hovered() and pressed_btn == 1:
            self.press = True
        else:
            self.press = False
