
from random import *
import sys
import pygame
import pickle
from gi.repository import Gtk
import gi
gi.require_version('Gtk', '3.0')


class rules:

    def run(self, gameDisplay, info):

        disp_width = 600

        press = 0
        black = (0, 0, 0)
        clock = pygame.time.Clock()
        timer = pygame.time.Clock()

        background = pygame.image.load("data/images/rulesbackground.png")
        back = pygame.image.load("data/images/back.png")

        background = pygame.transform.scale(
            background, (disp_width - 100, info.current_h - 40))
        back = pygame.transform.scale(back, (70, 40))

        sound = True

        while not self.crashed:
            # Gtk events

            while Gtk.events_pending():
                Gtk.main_iteration()
            event = pygame.event.poll()
            # totaltime+=timer.tick()
            if event.type == pygame.QUIT:
                return

            mos_x, mos_y = pygame.mouse.get_pos()

            gameDisplay.fill(black)
            gameDisplay.blit(background, (0 + 350, 0))

            if back.get_rect(center=(750 + 35, 10 + 15)).collidepoint(mos_x, mos_y):
                gameDisplay.blit(pygame.transform.scale(
                    back, (75, 45)), (725, 5))
                if (pygame.mouse.get_pressed())[0] == 1 and press == 0:
                    press = 1
                    return

                if event.type == pygame.MOUSEBUTTONUP:
                    press = 0

            else:
                gameDisplay.blit(back, (725, 5))

            # pygame.draw.circle(gameDisplay,(255,255,255), (750+35,20+15),5,2)

            pygame.display.update()
            clock.tick(60)