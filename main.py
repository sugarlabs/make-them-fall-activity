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
import pygame
import pickle
import gi
gi.require_version('Gtk', '3.0')
from gi.repository import Gtk

from sugar3.activity.activity import get_activity_root

from normal import pane2window
from nightmare import pane3window
from fear import pane4window
from cardiac import pane2heartwindow
from inferno import pane5window
from impossible import pane6window
from scorescreen import scorewindow
from howtoplay import rules
from button import Button

disp_width = 600
disp_height = 600

try:
    score_path = os.path.join(get_activity_root(), 'data', 'score.pkl')
except KeyError:
    score_path = '/tmp/score.pkl'

black = (0, 0, 0)
white = (255, 255, 255)


class MakeThemFallGame:

    sound = True

    def __init__(self):
        self.running = True
        self.running_mode = None
        self.clock = pygame.time.Clock()

        self.gameDisplay = None
        self.info = None
        self.screen_origin = [0, 0]
        self.visible_size = [0, 0]

        self.buttons = []

        self.maxscore = [0, 0, 0, 0, 0, 0]

    def run_game(self, window, gamenumber):
        self.running_mode = window()
        self.running_mode.running = self.running
        score_data = self.running_mode.run(self.gameDisplay, self.info)

        if scorewindow(self.gameDisplay, score_data, gamenumber, self).run():
            self.run_game(window, gamenumber)

        self.start()

    def show_help(self):
        self.running_mode = rules()
        self.running_mode.running = self.running
        self.running_mode = self.running_mode.run(self.gameDisplay,
                                                  self.visible_size,
                                                  self.screen_origin)

        self.start()

    def update_highscore(self):
        if os.path.getsize(score_path) > 0:
            with open(score_path, 'rb') as inp:  # Reading
                self.maxscore = pickle.load(inp)

    def vw(self, x):
        return self.screen_origin[0] + (x / 100) * self.visible_size[0]

    def vh(self, y):
        return self.screen_origin[1] + (y / 100) * self.visible_size[1]

    def place_centered(self, surf, x, y):
        rect = surf.get_rect()
        centered_coords = (x - rect.width // 2, y - rect.height // 2)
        self.gameDisplay.blit(surf, centered_coords)

    def start(self):

        self.gameDisplay = pygame.display.get_surface()

        self.info = pygame.display.Info()

        if not (self.gameDisplay):

            self.gameDisplay = pygame.display.set_mode(
                (self.info.current_w, self.info.current_h))

            pygame.display.set_caption("Make Them Fall")
            gameicon = pygame.image.load('data/images/icon.png')
            pygame.display.set_icon(gameicon)

        self.gameDisplay.fill(black)

        background = pygame.image.load(
            "data/images/welcomescreen/background.png")

        bg_rect = background.get_rect()
        display_rect = self.gameDisplay.get_rect()

        self.screen_origin[0] = (display_rect.width - bg_rect.width) // 2
        self.visible_size = [bg_rect.width, bg_rect.height]

        self.gameDisplay.blit(background, self.screen_origin)

        font_path = "fonts/arial.ttf"
        font_size = 18
        font1 = pygame.font.Font(font_path, font_size)
        font1.set_bold(True)

        if not os.path.exists(score_path):
            open(score_path, 'w+')

        self.update_highscore()

        maxnormal = font1.render("Best: " + str(self.maxscore[0]), True, black)
        maxnightmare = font1.render(
            "Best: " + str(self.maxscore[1]), True, black)
        maxfear = font1.render("Best: " + str(self.maxscore[2]), True, black)
        maxinferno = font1.render(
            "Best: " + str(self.maxscore[3]), True, black)
        maximpossible = font1.render(
            "Best: " + str(self.maxscore[4]), True, black)
        maxcardiac = font1.render(
            "Best: " + str(self.maxscore[5]), True, black)

        self.buttons.append(Button(self.vw(50), self.vh(26),
                                   "data/images/welcomescreen/2pane.png",
                                   lambda: self.run_game(pane2window, 1),
                                   maxnormal))

        self.buttons.append(Button(self.vw(50), self.vh(38),
                                   "data/images/welcomescreen/3pane.png",
                                   lambda: self.run_game(pane3window, 2),
                                   maxnightmare))

        self.buttons.append(Button(self.vw(20), self.vh(38),
                                   "data/images/welcomescreen/4pane.png",
                                   lambda: self.run_game(pane4window, 3),
                                   maxfear))

        self.buttons.append(Button(self.vw(80), self.vh(38),
                                   "data/images/welcomescreen/5pane.png",
                                   lambda: self.run_game(pane5window, 4),
                                   maxinferno))

        self.buttons.append(Button(self.vw(50), self.vh(50),
                                   "data/images/welcomescreen/6pane.png",
                                   lambda: self.run_game(pane6window, 5),
                                   maximpossible))

        self.buttons.append(Button(self.vw(50), self.vh(62),
                                   "data/images/welcomescreen/2paneheart.png",
                                   lambda: self.run_game(pane2heartwindow, 6),
                                   maxcardiac))

        self.buttons.append(Button(self.vw(50), self.vh(74),
                                   "data/images/welcomescreen/help.png",
                                   self.show_help))

        howto = pygame.image.load("data/images/welcomescreen/howtoplay.png")

        self.place_centered(howto, self.vw(50), self.vh(82))

    def run(self):
        self.start()

        while self.running:
            # Gtk events
            while Gtk.events_pending():
                Gtk.main_iteration()
            if not self.running:
                break

            # Pump PyGame messages.
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    return
                elif event.type == pygame.VIDEORESIZE:
                    pass

            for btn in self.buttons:
                btn.update()

            self.f = 1
            pygame.display.update()
            self.clock.tick(30)

        return


def main():
    pygame.init()
    pygame.display.set_mode((0, 0), pygame.RESIZABLE)
    game = MakeThemFallGame()
    game.run()


if __name__ == "__main__":
    main()
