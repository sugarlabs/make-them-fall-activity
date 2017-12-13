
import gtk
import pickle
import pygame
import sys
from random import *


class pane2heartwindow:

    def run(self, gameDisplay, info):

        crashed = False
        orientation1 = 0
        orientation2 = 0
        orientation3 = 0
        orientation4 = 0
        orientation5 = 0
        orientation6 = 0

        leftmove = 350
        rightmove = 659
        limit1 = limit2 = 0

        leftman = pygame.image.load("data/images/man.png")
        rightman = pygame.transform.flip(leftman, True, False)
        background = pygame.image.load("data/images/2pane.png")
        blackheart = pygame.image.load("data/images/blackheart.png")
        whiteheart = pygame.image.load("data/images/whiteheart.png")

        lspike = pygame.image.load("data/images/heart.png")
        rspike = pygame.transform.flip(lspike, True, False)
        background = pygame.transform.scale(background, (600, info.current_h))
        y_axis1 = 700
        y_axis2 = y_axis1 + 370

        y_axisa = 750
        y_axisb = y_axisa + 370

        leftquad = leftman
        rightquad = leftman
        f1 = f2 = 0
        m1 = m2 = 0
        time1 = time2 = 0

        font_path = "fonts/arial.ttf"
        font_size = 50
        font1 = pygame.font.Font(font_path, font_size)
        score = 0

        x_axis1 = x_axis2 = 350
        x_axisa = x_axisb = 659
        speed = 7
        flag = 1

        flag1 = flag2 = flag3 = flag4 = 0

        numberofhearts = 0

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

            gameDisplay.fill(black)
            gameDisplay.blit(background, (0 + 350, 0))

            # Keypress orientation change

            if event.type == pygame.KEYDOWN and event.key == 276 and f1 == 0:
                jump.play(0)
                f1 = 1
                m1 = 1  # start moving

            if event.type == pygame.KEYDOWN and event.key == 275 and f2 == 0:
                jump.play(0)
                f2 = 1
                m2 = 1  # start moving

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

            if m1 == 1:

                if leftquad == leftman:
                    leftmove += 34
                if leftquad == rightman:
                    leftmove -= 34
                time1 += 1

            if m2 == 1:

                if rightquad == leftman:
                    rightmove += 34
                if rightquad == rightman:
                    rightmove -= 34
                time2 += 1

            #[350,608]   [659, 916]

            # Guy Display

            if leftquad == leftman or leftquad == rightman:
                gameDisplay.blit(leftquad, (leftmove, 100))

            if rightquad == leftman or rightquad == rightman:
                gameDisplay.blit(rightquad, (rightmove, 100))

            ######### SPIKE PART###########

            if orientation1 == 0 and flag1 == 0:  # orientation change
                x_axis1 = 350
                gameDisplay.blit(lspike, (x_axis1, y_axis1))

            if orientation1 == 1 and flag1 == 0:
                x_axis1 = 589
                gameDisplay.blit(rspike, (x_axis1, y_axis1))

            if orientation2 == 0 and flag2 == 0:
                x_axis2 = 350
                gameDisplay.blit(lspike, (x_axis2, y_axis2))

            if orientation2 == 1 and flag2 == 0:
                x_axis2 = 589
                gameDisplay.blit(rspike, (x_axis2, y_axis2))

            # right side spikes
            if orientation4 == 0 and flag3 == 0:
                x_axisa = 659
                gameDisplay.blit(lspike, (x_axisa, y_axisa))

            if orientation4 == 1 and flag3 == 0:
                x_axisa = 659 + 238
                gameDisplay.blit(rspike, (x_axisa, y_axisa))

            if orientation5 == 0 and flag4 == 0:
                x_axisb = 659
                gameDisplay.blit(lspike, (x_axisb, y_axisb))

            if orientation5 == 1 and flag4 == 0:
                x_axisb = 659 + 238
                gameDisplay.blit(rspike, (x_axisb, y_axisb))

            y_axis1 -= speed
            y_axis2 -= speed

            y_axisa -= speed
            y_axisb -= speed

            if score == 15 or score == 35 or score == 50 or score == 75:
                flag = 1

            if score == 15 and flag == 1:
                flag = 0
                speed += 0.1

            if score == 35 and flag == 1:
                flag = 0
                speed += 0.1

            if score == 50 and flag == 1:
                flag = 0
                speed += 0.1

            if score == 75 and flag == 1:
                flag = 0
                speed += 0.1

            if (y_axis1 <= -40 and flag1 != 1) or (y_axis2 <= -40 and flag2 != 1) or (y_axisa <= -40 and flag3 != 1)or (y_axisb <= -40 and flag4 != 1):
                collide.play(0)
                numberofhearts += 1

            if(y_axis1 < -40):
                orientation1 = randint(0, 1)
                flag1 = 0
                y_axis1 = 700

            if(y_axis2 < -40):
                orientation2 = randint(0, 1)
                flag2 = 0
                y_axis2 = 700

            if(y_axisa < -40):
                orientation4 = randint(0, 1)
                flag3 = 0
                y_axisa = 700

            if(y_axisb < -40):
                orientation5 = randint(0, 1)
                flag4 = 0
                y_axisb = 700

            scores = font1.render(str(score), 1, (0, 0, 0))
            gameDisplay.blit(scores, (200 + 650, 30))

            # Heart Blit

            if numberofhearts >= 1:
                gameDisplay.blit(blackheart, (550, 20))

            else:
                gameDisplay.blit(whiteheart, (550, 20))

            if numberofhearts >= 2:
                gameDisplay.blit(blackheart, (620, 20))

            else:
                gameDisplay.blit(whiteheart, (620, 20))

            if numberofhearts == 3:
                gameDisplay.blit(blackheart, (690, 20))

            else:
                gameDisplay.blit(whiteheart, (690, 20))

            # Heart collection check

            if leftquad.get_rect(center=(leftmove + 5, 100 + 10)).collidepoint(x_axis1 + 8, y_axis1) and flag1 == 0:
                scoremusic.play(0)
                score += 1
                # orientation2=randint(0,1)
                flag1 = 1

            if leftquad.get_rect(center=(leftmove + 5, 100 + 10)).collidepoint(x_axis2 + 8, y_axis2) and flag2 == 0:
                scoremusic.play(0)
                score += 1
                # orientation2=randint(0,1)
                flag2 = 1

            if rightquad.get_rect(center=(rightmove + 5, 100 + 10)).collidepoint(x_axisa + 8, y_axisa) and flag3 == 0:
                scoremusic.play(0)
                score += 1
                flag3 = 1

            if rightquad.get_rect(center=(rightmove + 5, 100 + 10)).collidepoint(x_axisb + 8, y_axisb) and flag4 == 0:
                scoremusic.play(0)
                score += 1
                flag4 = 1

                # collide.play(0)
                # return score

            pygame.display.update()
            clock.tick(60)

            if numberofhearts == 3:
                return score

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
