
import os
from gi.repository import Gtk
import pickle
import pygame

from sugar3.activity.activity import get_activity_root
from button import Button

black = (0, 0, 0)
white = (255, 255, 255)


class scorewindow:

    def __init__(self, gameDisplay, score, gamenumber, game):
        background = pygame.image.load(
            "data/images/scorescreen/whitebackground.png")
        gameover = pygame.image.load("data/images/scorescreen/gameover.png")
        newbestscore = pygame.image.load(
            "data/images/scorescreen/newbestscore.png")
        scoreboard = pygame.image.load(
            "data/images/scorescreen/scoreboard.png")

        background = pygame.transform.scale(background, game.visible_size)

        font_path = "fonts/arial.ttf"
        font_size = 50
        font_size_large = 35

        font1 = pygame.font.Font(font_path, font_size)
        font1.set_bold(True)
        font2 = pygame.font.Font(font_path, font_size_large)
        font2.set_bold(True)

        self.tryagain = False
        self.backhome = False

        ifbest = False

        maxscore = [0, 0, 0, 0, 0, 0]

        try:
            score_path = os.path.join(get_activity_root(), 'data', 'score.pkl')
        except KeyError:
            score_path = '/tmp/score.pkl'

        if not os.path.exists(score_path):
            open(score_path, 'w+')

        if os.path.getsize(score_path) > 0:

            with open(score_path, 'rb') as inp:  # Reading
                maxscore = pickle.load(inp)

        if score is not None and score > maxscore[gamenumber - 1]:
            best = score
            ifbest = True
            maxscore[gamenumber - 1] = score
            with open(score_path, 'wb') as output:  # Writiing if max
                pickle.dump(maxscore, output, pickle.HIGHEST_PROTOCOL)
        else:
            best = maxscore[gamenumber - 1]

        score = font2.render(str(score), 1, (255, 255, 255))
        best = font2.render(str(best), 1, white)

        gameDisplay.fill(black)
        gameDisplay.blit(background, game.screen_origin)
        game.place_centered(gameover, game.vw(50), game.vh(10))

        self.buttons = []

        if ifbest is True:
            game.place_centered(newbestscore, game.vw(50), game.vh(20))
            game.place_centered(best, game.vw(50), game.vh(22))
            self.buttons.append(Button(game.vw(50), game.vh(30),
                                       "data/images/scorescreen/tryagain.png",
                                       self._try_again_cb))
            self.buttons.append(Button(game.vw(50), game.vh(40),
                                       "data/images/scorescreen/back.png",
                                       self._back_home_cb))
        else:
            game.place_centered(scoreboard, game.vw(50), game.vh(28))
            game.place_centered(score, game.vw(50), game.vh(24))
            game.place_centered(best, game.vw(50), game.vh(36))
            self.buttons.append(Button(game.vw(50), game.vh(48),
                                       "data/images/scorescreen/tryagain.png",
                                       self._try_again_cb))
            self.buttons.append(Button(game.vw(50), game.vh(60),
                                       "data/images/scorescreen/back.png",
                                       self._back_home_cb))

        self.running = True

    def _try_again_cb(self):
        self.tryagain = True

    def _back_home_cb(self):
        self.backhome = True

    def run(self):
        if not self.running:
            return

        clock = pygame.time.Clock()

        while self.running:
            if self.tryagain:
                return 1
            if self.backhome:
                return 0

            # Gtk events
            while Gtk.events_pending():
                Gtk.main_iteration()
            event = pygame.event.poll()

            if event.type == pygame.KEYDOWN:
                return 1
            if event.type == pygame.QUIT:
                return

            for btn in self.buttons:
                btn.update()

            pygame.display.update()
            clock.tick(60)
