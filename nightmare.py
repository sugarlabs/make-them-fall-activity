
import gtk
import pickle
import pygame
import sys
from random import *


class pane3window:

    def run(self, gameDisplay, info):

        crashed = False
        orientation1 = 0
        orientation2 = 0
        orientation3 = 0
        orientation4 = 0
        orientation5 = 0
        orientation6 = 0

        leftmove = 350
        midmove = 555
        rightmove = 761

        limit1 = limit2 = 0

        leftman = pygame.image.load("data/images/man.png")
        rightman = pygame.transform.flip(leftman, True, False)
        background = pygame.image.load("data/images/3pane.png")
        lspike = pygame.image.load("data/images/Spike.png")
        rspike = pygame.transform.flip(lspike, True, False)
        background = pygame.transform.scale(background, (600, info.current_h))
        y_axis1 = 700
        y_axis2 = y_axis1 + 370

        y_axisa = 750
        y_axisb = y_axisa + 370

        y_axisx = 761
        y_axisy = y_axisx + 370

        leftquad = leftman
        midquad = leftman
        rightquad = leftman

        f1 = f2 = f3 = 0
        m1 = m2 = m3 = 0
        time1 = time2 = 0

        font_path = "fonts/arial.ttf"
        font_size = 50
        font1 = pygame.font.Font(font_path, font_size)
        score = 0

        x_axis1 = x_axis2 = 350
        x_axisa = x_axisb = 659
        x_axisx = x_axisy = 761
        speed = 7
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

            gameDisplay.fill(black)
            gameDisplay.blit(background, (0 + 350, 0))

            # Keypress orientation change

            if event.type == pygame.KEYDOWN and event.key == 276 and f1 == 0:
                jump.play(0)
                f1 = 1
                m1 = 1  # start moving

            if event.type == pygame.KEYDOWN and event.key == 274 and f2 == 0:
                jump.play(0)
                f2 = 1
                m2 = 1  # start moving

            if event.type == pygame.KEYDOWN and event.key == 275 and f3 == 0:
                jump.play(0)
                f3 = 1
                m3 = 1  # start moving

            # Check for when to stop

            if leftmove > 484 + 20:  # left move
                leftquad = rightman
                m1 = f1 = 0
                leftmove = 484 + 20
                time1 = 0

            if leftmove < 350:
                leftquad = leftman
                m1 = f1 = 0
                leftmove = 350
                time1 = 0

            if midmove < 555:  # mid move
                midquad = leftman
                m2 = f2 = 0
                midmove = 555
                time2 = 0

            if midmove > 690 + 20:
                midquad = rightman
                m2 = f2 = 0
                midmove = 690 + 20
                time2 = 0

            if rightmove < 761:  # right move move
                rightquad = leftman
                m3 = f3 = 0
                rightmove = 761
                time2 = 0

            if rightmove > 761 + 156:
                rightquad = rightman
                m3 = f3 = 0
                rightmove = 761 + 156
                time2 = 0

            if m1 == 1:

                if leftquad == leftman:
                    leftmove += 30
                if leftquad == rightman:
                    leftmove -= 30
                time1 += 1

            if m2 == 1:

                if midquad == leftman:
                    midmove += 30
                if midquad == rightman:
                    midmove -= 30
                time2 += 1

            if m3 == 1:

                if rightquad == leftman:
                    rightmove += 30
                if rightquad == rightman:
                    rightmove -= 30
                time2 += 1

            #[350,608]   [659, 916]

            # Guy Display

            if leftquad == leftman or leftquad == rightman:
                gameDisplay.blit(leftquad, (leftmove, 100))

            if midquad == leftman or midquad == rightman:
                gameDisplay.blit(midquad, (midmove, 100))

            if rightquad == leftman or rightquad == rightman:
                gameDisplay.blit(rightquad, (rightmove, 100))

            ######### SPIKE PART###########

            if orientation1 == 0:  # orientation change
                x_axis1 = 350
                gameDisplay.blit(lspike, (x_axis1, y_axis1))

            if orientation1 == 1:
                x_axis1 = 485
                gameDisplay.blit(rspike, (x_axis1, y_axis1))

            if orientation2 == 0:
                x_axis2 = 350
                gameDisplay.blit(lspike, (x_axis2, y_axis2))

            if orientation2 == 1:
                x_axis2 = 485
                gameDisplay.blit(rspike, (x_axis2, y_axis2))

            # mid side spikes
            if orientation3 == 0:
                x_axisa = 555
                gameDisplay.blit(lspike, (x_axisa, y_axisa))

            if orientation3 == 1:
                x_axisa = 691
                gameDisplay.blit(rspike, (x_axisa, y_axisa))

            if orientation4 == 0:
                x_axisb = 555
                gameDisplay.blit(lspike, (x_axisb, y_axisb))

            if orientation4 == 1:
                x_axisb = 691
                gameDisplay.blit(rspike, (x_axisb, y_axisb))

            # right side spikes

            if orientation5 == 0:
                x_axisx = 761
                gameDisplay.blit(lspike, (x_axisx, y_axisx))

            if orientation5 == 1:
                x_axisx = 761 + 136
                gameDisplay.blit(rspike, (x_axisx, y_axisx))

            if orientation6 == 0:
                x_axisy = 761
                gameDisplay.blit(lspike, (x_axisy, y_axisy))

            if orientation6 == 1:
                x_axisy = 761 + 136
                gameDisplay.blit(rspike, (x_axisy, y_axisy))

            y_axis1 -= speed
            y_axis2 -= speed

            y_axisa -= speed
            y_axisb -= speed

            y_axisx -= speed
            y_axisy -= speed

            '''
            
            if score==15 or score==45 or score==70:
                flag=1
            
            if score==15 and flag==1 :
                flag=0
                speed+=0.1
              
            if score==45 and flag==1:
                flag=0
                speed+=0.1
              
            if score==70 and flag==1:
                flag=0
                speed+=0.1
            '''

            if y_axis1 <= -40 or y_axis2 <= -40 or y_axisa <= -40 or y_axisb <= -40 or \
               y_axisx <= -40 or y_axisy <= -40:
                scoremusic.play(0)
                score += 1

            if(y_axis1 < -40):
                orientation1 = randint(0, 1)

                y_axis1 = 700

            if(y_axis2 < -40):
                orientation2 = randint(0, 1)

                y_axis2 = 700

            if(y_axisa < -40):
                orientation3 = randint(0, 1)

                y_axisa = 700

            if(y_axisb < -40):
                orientation4 = randint(0, 1)

                y_axisb = 700

            if(y_axisx < -40):
                orientation5 = randint(0, 1)

                y_axisx = 700

            if(y_axisy < -40):
                orientation6 = randint(0, 1)

                y_axisy = 700

            scores = font1.render(str(score), 1, (0, 0, 0))
            gameDisplay.blit(scores, (200 + 650, 30))

            if leftquad.get_rect(center=(leftmove + 5, 100 + 10)).collidepoint(x_axis1 + 8, y_axis1) \
                    or leftquad.get_rect(center=(leftmove + 5, 100 + 10)).collidepoint(x_axis2 + 8, y_axis2):
                pygame.mixer.music.load("data/sound/fall.wav")
                pygame.mixer.music.play(0)
                # collide.play(0)
                return score

            if midquad.get_rect(center=(midmove + 5, 100 + 10)).collidepoint(x_axisa + 8, y_axisa) \
                    or midquad.get_rect(center=(midmove + 5, 100 + 10)).collidepoint(x_axisb + 8, y_axisb):
                pygame.mixer.music.load("data/sound/fall.wav")
                pygame.mixer.music.play(0)
                # collide.play(0)
                return score

            if rightquad.get_rect(center=(rightmove + 5, 100 + 10)).collidepoint(x_axisx + 8, y_axisx) \
                    or rightquad.get_rect(center=(rightmove + 5, 100 + 10)).collidepoint(x_axisy + 8, y_axisy):
                pygame.mixer.music.load("data/sound/fall.wav")
                pygame.mixer.music.play(0)
                # collide.play(0)
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
