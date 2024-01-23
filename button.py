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
import inspect

class Button:

    def __init__(self, x, y, text=None,colors=None, image_path=None, action=None, scale=None, gid=None,config=None):
        if(image_path!=None):
           self.graphic = pygame.image.load(image_path)

           self.gid=gid
           self.config=config
           if scale:
               self.graphic = pygame.transform.scale(self.graphic, scale)

           self.rect = self.graphic.get_rect()
           self.colors=colors
           print(x)
           print(y)

           self.x = x - self.rect.width // 2
           print(self.x)
           self.y = y - self.rect.height // 2
           print(self.y)
           self.rect.x = self.x
           self.rect.y = self.y

           self.text = text
           self.gameDisplay = pygame.display.get_surface()

           self.action = action

           self.press = False

           self.draw()
        else:
           self.text = text
           self.config=config
           self.gameDisplay = pygame.display.get_surface()
           self.colors=colors
           self.action = action
           width,height=scale
        #    self.x = x - self.rect.width // 2
        #    self.y = y - self.rect.height // 2
           self.rect = pygame.Rect(x - width // 2, y - height // 2, width, height)
           self.x = x - self.rect.width // 2
           self.y = y - self.rect.height // 2

           self.press = False
           self.custom_draw()
           self.gid=gid

    def draw(self):
        print("two")
        if self.hovered():
             scaled_graphic = pygame.transform.scale(
                self.graphic, (self.rect.width + 10, self.rect.height + 5))
             self.gameDisplay.blit(scaled_graphic, (self.x - 5, self.y))
        else:
            self.gameDisplay.blit(self.graphic, (self.x, self.y))

        if self.text is not None:
            # print(self.text)
            text_rect = self.text.get_rect()
            m_x = self.x + self.rect.width // 2 - text_rect.width // 2
            m_y = self.y + self.rect.height - 1.5 * text_rect.height
            self.gameDisplay.blit(self.text, (m_x, m_y))

    def custom_draw(self):
        print("one")
        color=self.colors[0]
        #  print(self.config["diffi
        if(hasattr(self,'gid') and hasattr(self,'config')):
           print("one-2")
           if(self.gid == self.config["difficulty"]):
              print("hey")
              color=self.colors[1]
        pygame.draw.rect(self.gameDisplay, color, self.rect)

        if self.text is not None:
            font1 = pygame.font.Font("fonts/arial.ttf", 36)
            text_sur = font1.render(
            self.text, True, (0,0,0))
            font1.set_bold(True)
            text_rect=text_sur.get_rect()
            m_x = self.x + self.rect.width // 2 - text_rect.width // 2
            m_y = self.y + self.rect.height - 1.5 * text_rect.height -10
            self.gameDisplay.blit(text_sur, (m_x, m_y))

    def hovered(self):
        return self.rect.collidepoint(pygame.mouse.get_pos())

    def update(self):
        # print("hello")
        if(hasattr(self, 'graphic')):
          self.draw()
        else:
            self.custom_draw()
        pressed_btn = pygame.mouse.get_pressed()[0]
        if self.press and self.hovered() and pressed_btn != 1:
            if inspect.signature(self.action).parameters:
                self.action(number=self.gid)
            else:
                self.action()


        if self.hovered() and pressed_btn == 1:
            self.press = True
        else:
            self.press = False
