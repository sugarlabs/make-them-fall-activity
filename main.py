#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
# Make Them Fall
# Copyright (C) 2015  Utkarsh Tiwari
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
# Utkarsh Tiwari    iamutkarshtiwari@gmail.com


import os
import gtk
import pickle
import pygame
import sys
from gettext import gettext as _

from normal import *
from nightmare import *
from fear import *
from cardiac import *
from impossible import *
from inferno import *
from scorescreen import *
from howtoplay import *


class game:

    def make(self):

        pygame.init()
        sound = True

        try:
            pygame.mixer.init()
        except Exception, err:
            sound = False
            print 'error with sound', err

        black = (0, 0, 0)
        white = (255, 255, 255)
        clock = pygame.time.Clock()
        timer = pygame.time.Clock()

        crashed = False
        disp_width = 600
        disp_height = 600

        press = 0

        info = pygame.display.Info()
        gameDisplay = pygame.display.get_surface()

        if not(gameDisplay):

            gameDisplay = pygame.display.set_mode(
                (info.current_w, info.current_h))

            pygame.display.set_caption("Make Them Fall")
            gameicon = pygame.image.load('data/images/icon.png')
            pygame.display.set_icon(gameicon)

        title = pygame.image.load("data/images/welcomescreen/title.png")
        pane2 = pygame.image.load("data/images/welcomescreen/2pane.png")
        pane3 = pygame.image.load("data/images/welcomescreen/3pane.png")
        pane4 = pygame.image.load("data/images/welcomescreen/4pane.png")
        pane5 = pygame.image.load("data/images/welcomescreen/5pane.png")
        pane6 = pygame.image.load("data/images/welcomescreen/6pane.png")
        hlp = pygame.image.load("data/images/welcomescreen/help.png")
        howto = pygame.image.load("data/images/welcomescreen/howtoplay.png")
        paneheart2 = pygame.image.load(
            "data/images/welcomescreen/2paneheart.png")
        background = pygame.image.load(
            "data/images/welcomescreen/background.png")

        maxnormal = 0
        maxnightmare = 0
        maxfear = 0
        maxcardiac = 0
        maximpossible = 0
        maxinferno = 0
        f = 1
        maxscore = [0, 0, 0, 0, 0, 0]

        font_path = "fonts/arial.ttf"
        font_size = 18
        font1 = pygame.font.Font(font_path, font_size)
        font1.set_bold(True)

        if os.path.getsize("score.pkl") > 0:

            with open('score.pkl', 'rb') as input:  # REading
                maxscore = pickle.load(input)

        maxnormal = maxscore[0]
        maxnightmare = maxscore[1]
        maxfear = maxscore[2]
        maxinferno = maxscore[3]
        maximpossible = maxscore[4]
        maxcardiac = maxscore[5]

        maxnormal = font1.render(str("Best: ") + str(maxnormal), 1, (0, 0, 0))
        maxnightmare = font1.render(str("Best: ") + str(maxnightmare), 1, (0, 0, 0))
        maxcardiac = font1.render(str("Best: ") + str(maxcardiac), 1, (0, 0, 0))
        maxfear = font1.render(str("Best: ") + str(maxfear), 1, (0, 0, 0))
        maxinferno = font1.render(str("Best: ") + str(maxinferno), 1, (0, 0, 0))
        maximpossible = font1.render(
            str("Best: ") + str(maximpossible), 1, (0, 0, 0))

        while not crashed:
            # Gtk events

            while gtk.events_pending():
                gtk.main_iteration()
            event = pygame.event.poll()
            # totaltime+=timer.tick()
            if event.type == pygame.QUIT:
                crashed = True

            mos_x, mos_y = pygame.mouse.get_pos()

            # print event

            gameDisplay.fill(black)
            gameDisplay.blit(background, (350, 0))

            # 2 pane game
            if pane2.get_rect(center=(390 + 80 + 120, 150 + 50)).collidepoint(mos_x, mos_y):
                gameDisplay.blit(pygame.transform.scale(
                    pane2, (420, 90)), (385, 150))
                if(pygame.mouse.get_pressed())[0] == 1 and press == 0:
                    # print 'yes'
                    press = 1
                    while f == 1:

                        a = pane2window()
                        a = a.run(gameDisplay, info)

                        f = scorewindow()
                        f = f.run(gameDisplay, a, 1)

                if event.type == pygame.MOUSEBUTTONUP:
                    press = 0

            else:
                gameDisplay.blit(pane2, (390, 150))  # 2pane

            if pane3.get_rect(center=(390 + 60, 250 + 50)).collidepoint(mos_x, mos_y):  # 3pane game
                gameDisplay.blit(pygame.transform.scale(
                    pane3, (135, 95)), (385, 250))
                if(pygame.mouse.get_pressed())[0] == 1 and press == 0:
                    press = 1
                    while f == 1:

                        a = pane3window()
                        a = a.run(gameDisplay, info)

                        f = scorewindow()
                        f = f.run(gameDisplay, a, 2)

                if event.type == pygame.MOUSEBUTTONUP:
                    press = 0

            else:
                gameDisplay.blit(pane3, (390, 250))  # 3pane

            if pane4.get_rect(center=(530 + 60, 250 + 50)).collidepoint(mos_x, mos_y):
                gameDisplay.blit(pygame.transform.scale(
                    pane4, (135, 95)), (525, 250))
                # 4Pane Window
                if(pygame.mouse.get_pressed())[0] == 1 and press == 0:

                    press = 1
                    while f == 1:

                        a = pane4window()
                        a = a.run(gameDisplay, info)

                        f = scorewindow()
                        f = f.run(gameDisplay, a, 3)

                if event.type == pygame.MOUSEBUTTONUP:
                    press = 0

            else:
                gameDisplay.blit(pane4, (530, 250))  # 4pane

            if pane5.get_rect(center=(670 + 60, 250 + 50)).collidepoint(mos_x, mos_y):  # 5pane Windoe
                gameDisplay.blit(pygame.transform.scale(
                    pane5, (135, 95)), (665, 250))

                if(pygame.mouse.get_pressed())[0] == 1 and press == 0:
                    press = 1
                    while f == 1:

                        a = pane5window()
                        a = a.run(gameDisplay, info)

                        f = scorewindow()

                        f = f.run(gameDisplay, a, 4)

                if event.type == pygame.MOUSEBUTTONUP:
                    press = 0

            else:
                gameDisplay.blit(pane5, (670, 250))  # 5pane

            # Impossible module connect
            if pane6.get_rect(center=(390 + 200, 350 + 50)).collidepoint(mos_x, mos_y):
                gameDisplay.blit(pygame.transform.scale(
                    pane6, (420, 90)), (385, 350))
                if(pygame.mouse.get_pressed())[0] == 1 and press == 0:
                    press = 1
                    while f == 1:

                        a = pane6window()
                        a = a.run(gameDisplay, info)

                        f = scorewindow()
                        f = f.run(gameDisplay, a, 5)

                if event.type == pygame.MOUSEBUTTONUP:
                    press = 0

            else:
                gameDisplay.blit(pane6, (390, 350))  # 6pane

            # heart collect game
            if paneheart2.get_rect(center=(390 + 200, 450 + 50)).collidepoint(mos_x, mos_y):
                gameDisplay.blit(pygame.transform.scale(
                    paneheart2, (420, 90)), (385, 450))
                if(pygame.mouse.get_pressed())[0] == 1 and press == 0:
                    press = 1
                    while f == 1:

                        a = pane2heartwindow()
                        a = a.run(gameDisplay, info)

                        f = scorewindow()
                        f = f.run(gameDisplay, a, 6)

                if event.type == pygame.MOUSEBUTTONUP:
                    press = 0

            else:
                gameDisplay.blit(paneheart2, (390, 450))  # paneheart

            gameDisplay.blit(howto, (490, 550))

            if hlp.get_rect(center=(550 + 20, 580 + 20)).collidepoint(mos_x, mos_y):  # RULES
                gameDisplay.blit(pygame.transform.scale(
                    hlp, (88, 88)), (548, 580))

                if(pygame.mouse.get_pressed())[0] == 1 and press == 0:
                    press = 1
                    a = rules()
                    a = a.run(gameDisplay, info)

                if event.type == pygame.MOUSEBUTTONUP:
                    press = 0

            else:

                gameDisplay.blit(hlp, (550, 580))     # help

            maxnormal = font1.render("Best: " + str(maxnormal), 1, (0, 0, 0))
            maxnightmare = font1.render(
                "Best: " + str(maxnightmare), 1, (0, 0, 0))
            maxfear = font1.render("Best: " + str(maxfear), 1, (0, 0, 0))
            maxinferno = font1.render("Best: " + str(maxinferno), 1, (0, 0, 0))
            maximpossible = font1.render(
                "Best: " + str(maximpossible), 1, (0, 0, 0))
            maxcardiac = font1.render("Best: " + str(maxcardiac), 1, (0, 0, 0))

            # Scores Display

            gameDisplay.blit(maxnormal, (540, 200))
            gameDisplay.blit(maxnightmare, (410, 300))
            gameDisplay.blit(maxfear, (560, 300))
            gameDisplay.blit(maxinferno, (700, 300))
            gameDisplay.blit(maximpossible, (560, 410))
            gameDisplay.blit(maxcardiac, (560, 510))

            if os.path.getsize("score.pkl") > 0:

                with open('score.pkl', 'rb') as input:  # REading
                    maxscore = pickle.load(input)

            maxnormal = maxscore[0]
            maxnightmare = maxscore[1]
            maxfear = maxscore[2]
            maxinferno = maxscore[3]
            maximpossible = maxscore[4]
            maxcardiac = maxscore[5]

            f = 1
            # press=0
            pygame.display.update()
            clock.tick(60)

            if crashed == True:                                   # Game crash or Close check
                pygame.quit()
                sys.exit()

        # Just a window exception check condition

        event1 = pygame.event.get()
        if event1.type == pygame.QUIT:
            crashed = True

        if crashed == True:
            pygame.quit()
            sys.exit()


if __name__ == "__main__":
    g = game()
    g.make()
