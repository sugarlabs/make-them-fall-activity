
import gtk
import pickle
import pygame
import sys
from random import *


class pane4window:

    def run(self, gameDisplay, info):

        crashed = False
        orientation1 = 0
        orientation2 = 0
        orientation3 = 0
        orientation4 = 0
        orientation5 = 0
        orientation6 = 0

        leftmove = leftdownmove = 350
        rightmove = rightdownmove = 659
        limit1 = limit2 = 0

        leftman = pygame.image.load("data/images/man.png")
        rightman = pygame.transform.flip(leftman, True, False)
        background = pygame.image.load("data/images/up4.png")
        background1 = pygame.image.load("data/images/down4.png")

        lspike = pygame.image.load("data/images/Spike.png")
        rspike = pygame.transform.flip(lspike, True, False)
        background = pygame.transform.scale(
            background, (600, info.current_h / 2))
        background1 = pygame.transform.scale(
            background1, (600, info.current_h / 2))
        y_axis1 = 400 + 100
        y_axis2 = 750 + 100

        y_axisa = 430 + 100
        y_axisb = 800 + 100

        leftquad = leftdown = leftman
        rightquad = rightdown = leftman
        f1 = f2 = f3 = f4 = 0
        m1 = m2 = m3 = m4 = 0
        time1 = time2 = 0

        font_path = "fonts/arial.ttf"
        font_size = 50
        font1 = pygame.font.Font(font_path, font_size)
        score = 0

        x_axis1 = x_axis2 = 350
        x_axisa = x_axisb = 659
        speed = 5
        flag = 1

        black = (0, 0, 0)
        white = (255, 255, 255)
        clock = pygame.time.Clock()
        timer = pygame.time.Clock()

        sound = True
        try:
            pygame.mixer.init()
        except Exception, err:
            sound = False
            print 'error with sound', err

        jump = pygame.mixer.Sound("data/sound/jump.wav")
        scoremusic = pygame.mixer.Sound("data/sound/score.wav")
        collide = pygame.mixer.Sound("data/sound/fall.wav")

        while not crashed:
            # Gtk events

            while gtk.events_pending():
                gtk.main_iteration()
            event = pygame.event.poll()
            # totaltime+=timer.tick()
            if event.type == pygame.QUIT:
                # totaltime+=timer.tick()
                crashed = True

            # print event

            gameDisplay.fill(black)
            gameDisplay.blit(background, (0 + 350, 0))

            # Keypress orientation change

            if event.type == pygame.KEYDOWN and event.key == 97 and f1 == 0:
                jump.play(0)
                f1 = 1
                m1 = 1  # start moving

            if event.type == pygame.KEYDOWN and event.key == 100 and f2 == 0:
                jump.play(0)
                f2 = 1
                m2 = 1  # start moving

            if event.type == pygame.KEYDOWN and event.key == 276 and f3 == 0:
                jump.play(0)
                f3 = 1
                m3 = 1  # start moving

            if event.type == pygame.KEYDOWN and event.key == 275 and f4 == 0:
                jump.play(0)
                f4 = 1
                m4 = 1

            # Check for when to stop

            if leftmove > 608:
                leftquad = rightman
                m1 = f1 = 0
                leftmove = 608
                time1 = 0

            if leftmove < 350:
                leftquad = leftman
                m1 = f1 = 0
                leftmove = 350
                time1 = 0

            if rightmove < 659:
                rightquad = leftman
                m2 = f2 = 0
                rightmove = 659
                time2 = 0

            if rightmove > 916:
                rightquad = rightman
                m2 = f2 = 0
                rightmove = 916
                time2 = 0

            # down orintation change and stop moves

            if leftdownmove > 608:
                leftdown = rightman
                m3 = f3 = 0
                leftdownmove = 608
                time1 = 0

            if leftdownmove < 350:
                leftdown = leftman
                m3 = f3 = 0
                leftdownmove = 350
                time1 = 0

            if rightdownmove < 659:
                rightdown = leftman
                m4 = f4 = 0
                rightdownmove = 659
                time2 = 0

            if rightdownmove > 916:
                rightdown = rightman
                m4 = f4 = 0
                rightdownmove = 916
                time2 = 0

            if m1 == 1:

                if leftquad == leftman:
                    leftmove += 30
                if leftquad == rightman:
                    leftmove -= 30
                time1 += 1

            if m2 == 1:

                if rightquad == leftman:
                    rightmove += 30
                if rightquad == rightman:
                    rightmove -= 30
                time2 += 1

            if m3 == 1:

                if leftdown == leftman:
                    leftdownmove += 30
                if leftdown == rightman:
                    leftdownmove -= 30
                time2 += 1

            if m4 == 1:

                if rightdown == leftman:
                    rightdownmove += 30
                if rightdown == rightman:
                    rightdownmove -= 30
                time2 += 1

            #[350,608]   [659, 916]

            # upper Guys Display

            if leftquad == leftman or leftquad == rightman:
                gameDisplay.blit(leftquad, (leftmove, 30))

            if rightquad == leftman or rightquad == rightman:
                gameDisplay.blit(rightquad, (rightmove, 30))

            ######### SPIKE PART###########

            if orientation1 == 0 and y_axis1 < 400:  # orientation change
                x_axis1 = 350
                gameDisplay.blit(lspike, (x_axis1, y_axis1))

            if orientation1 == 1 and y_axis1 < 400:
                x_axis1 = 589
                gameDisplay.blit(rspike, (x_axis1, y_axis1))

            # right side spikes
            if orientation4 == 0 and y_axisa < 400:
                x_axisa = 659
                gameDisplay.blit(lspike, (x_axisa, y_axisa))

            if orientation4 == 1 and y_axisa < 400:
                x_axisa = 659 + 238
                gameDisplay.blit(rspike, (x_axisa, y_axisa))

            gameDisplay.blit(background1, (0 + 350, 380)
                             )  # bottom part display

            # bottom guys display

            if leftdown == leftman or leftdown == rightman:
                gameDisplay.blit(leftdown, (leftdownmove, 400))

            if rightdown == leftman or rightdown == rightman:
                gameDisplay.blit(rightdown, (rightdownmove, 400))

            # bottom spikes

            if orientation2 == 0 and y_axis2 > 380:
                x_axis2 = 350
                gameDisplay.blit(lspike, (x_axis2, y_axis2))

            if orientation2 == 1 and y_axis2 > 380:
                x_axis2 = 589
                gameDisplay.blit(rspike, (x_axis2, y_axis2))

            if orientation5 == 0 and y_axisb > 380:
                x_axisb = 659
                gameDisplay.blit(lspike, (x_axisb, y_axisb))

            if orientation5 == 1 and y_axisb > 380:
                x_axisb = 659 + 238
                gameDisplay.blit(rspike, (x_axisb, y_axisb))

            y_axis1 -= speed
            y_axis2 -= speed

            y_axisa -= speed
            y_axisb -= speed
            '''
            if score==25 or score==55 or score==70:
                flag=1
            
            if score==60 and flag==1 :
                flag=0
                speed+=0.1
            '''

            # score count

            if y_axis1 < -40 or y_axis2 < 380 or y_axisa < -40 or y_axisb < 380:
                scoremusic.play(0)
                score += 1

            if(y_axis1 < -40):
                orientation1 = randint(0, 1)

                y_axis1 = 400

            if(y_axis2 < 380):
                orientation2 = randint(0, 1)

                y_axis2 = 700

            if(y_axisa < -40):
                orientation4 = randint(0, 1)

                y_axisa = 400

            if(y_axisb < 380):
                orientation5 = randint(0, 1)

                y_axisb = 700

            scores = font1.render(str(score), 1, (0, 0, 0))
            gameDisplay.blit(scores, (200 + 650, 30))

            # Collision detection

            if leftquad.get_rect(center=(leftmove + 5, 30 + 10)).collidepoint(x_axis1 + 8, y_axis1):
                collide.play(0)
                return score

            if rightquad.get_rect(center=(rightmove + 5, 30 + 10)).collidepoint(x_axisa + 8, y_axisa):
                collide.play(0)
                return score

            if leftdown.get_rect(center=(leftdownmove + 5, 400 + 10)).collidepoint(x_axis2 + 8, y_axis2):
                collide.play(0)
                return score

            if rightdown.get_rect(center=(rightdownmove + 5, 400 + 10)).collidepoint(x_axisb + 8, y_axisb):
                collide.play(0)
                return score

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
