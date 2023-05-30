
import os
from gi.repository import Gtk
import pickle
import pygame

from sugar3.activity.activity import get_activity_root
from button import Button

black = (0, 0, 0)
white = (255, 255, 255)


class scorewindow:

    def __init__(self, gameDisplay, score, gamenumber):
        background = pygame.image.load(
            "data/images/scorescreen/whitebackground.png")
        gameover = pygame.image.load("data/images/scorescreen/gameover.png")
        newbestscore = pygame.image.load(
            "data/images/scorescreen/newbestscore.png")
        scoreboard = pygame.image.load(
            "data/images/scorescreen/scoreboard.png")

        background = pygame.transform.scale(background, (600 - 100, 768))

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
        gameDisplay.blit(background, (0 + 350, 0))
        gameDisplay.blit(gameover, (350 + 60, 50 + 30))

        self.buttons = []

        if ifbest is True:
            gameDisplay.blit(newbestscore, (450, 160))
            gameDisplay.blit(best, (560, 190))
            self.buttons.append(Button(450, 250,
                                       "data/images/scorescreen/tryagain.png",
                                       self._try_again_cb))
            self.buttons.append(Button(450, 340,
                                       "data/images/scorescreen/back.png",
                                       self._back_home_cb))
        else:
            gameDisplay.blit(scoreboard, (450 + 5, 160))
            gameDisplay.blit(score, (570, 210))
            gameDisplay.blit(best, (560, 320))
            self.buttons.append(Button(450, 250 + 150,
                                       "data/images/scorescreen/tryagain.png",
                                       self._try_again_cb))
            self.buttons.append(Button(450, 340 + 150,
                                       "data/images/scorescreen/back.png",
                                       self._back_home_cb))

        self.crashed = False

    def _try_again_cb(self):
        self.tryagain = True

    def _back_home_cb(self):
        self.backhome = True

    def run(self):
        if self.crashed:
            return

        clock = pygame.time.Clock()

        while not self.crashed:
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
