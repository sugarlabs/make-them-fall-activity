
import os
import gi
gi.require_version('Gtk', '3.0')
from gi.repository import Gtk
import pickle
import pygame
import sys
from random import *\

from sugar3.activity.activity import get_activity_root 


class scorewindow:

    def run(self, gameDisplay, score, gamenumber):
        if self.crashed:
            return
        background = pygame.image.load(
            "data/images/scorescreen/whitebackground.png")
        gameover = pygame.image.load("data/images/scorescreen/gameover.png")
        newbestscore = pygame.image.load(
            "data/images/scorescreen/newbestscore.png")
        tryagain = pygame.image.load("data/images/scorescreen/tryagain.png")
        backhome = pygame.image.load("data/images/scorescreen/back.png")
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

        press = 0
        black = (0, 0, 0)
        white = (255, 255, 255)

        ifbest = False
        clock = pygame.time.Clock()
        timer = pygame.time.Clock()

        maxscore = [0, 0, 0, 0, 0, 0]

        sound = True

        score_path = os.path.join(get_activity_root(), 'data', 'score.pkl')
        
        if os.path.getsize(score_path) == 0:

            with open(score_path, 'wb') as output:
                pickle.dump(maxscore, output, pickle.HIGHEST_PROTOCOL)

        with open(score_path, 'rb') as input:  # REading
            maxscore = pickle.load(input)

        if score > maxscore[gamenumber - 1]:
            best = score
            ifbest = True
            maxscore[gamenumber - 1] = score
            with open(score_path, 'wb') as output:  # Writiing if max
                pickle.dump(maxscore, output, pickle.HIGHEST_PROTOCOL)

        else:
            best = maxscore[gamenumber - 1]
            # print best

        # print best
        score = font2.render(str(score), 1, (255, 255, 255))
        best = font2.render(str(best), 1, white)

        while not self.crashed:
            # Gtk events
            while Gtk.events_pending():
                Gtk.main_iteration()
            event = pygame.event.poll()

            if event.type == pygame.KEYDOWN:
                return 1
            if event.type == pygame.QUIT:
                return

            mos_x, mos_y = pygame.mouse.get_pos()

            if ifbest == True:

                gameDisplay.fill(black)
                gameDisplay.blit(background, (0 + 350, 0))
                gameDisplay.blit(gameover, (350 + 60, 50 + 30))

                gameDisplay.blit(newbestscore, (450, 160))

                # tryagain
                if tryagain.get_rect(center=(450 + 80, 250 + 10)).collidepoint(mos_x, mos_y):
                    gameDisplay.blit(pygame.transform.scale(
                        tryagain, (293, 84)), (448, 250))
                    if(pygame.mouse.get_pressed())[0] == 1 and press == 0:
                        press = 1
                        return 1

                    if event.type == pygame.MOUSEBUTTONUP:
                        press = 0

                else:

                    gameDisplay.blit(tryagain, (450, 250))

                # back home
                if backhome.get_rect(center=(450 + 80, 340 + 10)).collidepoint(mos_x, mos_y):
                    gameDisplay.blit(pygame.transform.scale(
                        backhome, (291, 84)), (448, 340))
                    if (pygame.mouse.get_pressed())[0] == 1 and press == 0:
                        press = 1
                        return 0

                    if event.type == pygame.MOUSEBUTTONUP:
                        press = 0

                else:

                    gameDisplay.blit(backhome, (450, 340))

                gameDisplay.blit(best, (560, 190))

            else:

                gameDisplay.fill(black)
                gameDisplay.blit(background, (0 + 350, 0))
                gameDisplay.blit(gameover, (350 + 80, 50))
                gameDisplay.blit(scoreboard, (450 + 5, 160))

                # try again
                if tryagain.get_rect(center=(450 + 80 + 5, 250 + 10 + 150)).collidepoint(mos_x, mos_y):
                    gameDisplay.blit(pygame.transform.scale(
                        tryagain, (293, 84)), (448 + 5, 250 + 150))
                    if(pygame.mouse.get_pressed())[0] == 1 and press == 0:
                        press = 1
                        return 1

                    if event.type == pygame.MOUSEBUTTONUP:
                        press = 0

                else:

                    gameDisplay.blit(tryagain, (450 + 5, 250 + 150))

                # backhome
                if backhome.get_rect(center=(450 + 80 + 5, 340 + 10 + 150)).collidepoint(mos_x, mos_y):
                    gameDisplay.blit(pygame.transform.scale(
                        backhome, (291, 84)), (448 + 5, 340 + 150))
                    if (pygame.mouse.get_pressed())[0] == 1 and press == 0:
                        press = 1
                        return 0

                    if event.type == pygame.MOUSEBUTTONUP:
                        press = 0

                else:

                    gameDisplay.blit(backhome, (450 + 5, 340 + 150))

                gameDisplay.blit(score, (570, 210))
                gameDisplay.blit(best, (570, 320))


            pygame.display.update()
            clock.tick(60)
