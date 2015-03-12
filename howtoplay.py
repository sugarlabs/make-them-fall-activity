
import gtk
import pickle
import pygame
import sys
from random import *

pygame.init()
sound=True
        
try:
    pygame.mixer.init()
except Exception, err:
    sound=False
    print 'error with sound', error
            
black=(0,0,0)
white=(255,255,255)
clock=pygame.time.Clock()
timer=pygame.time.Clock()
            
  
disp_width = 600
disp_height = 600
            
            

            
gameDisplay=pygame.display.get_surface()
        
if not(gameDisplay):
    info=pygame.display.Info()
    # info.current_h
    gameDisplay = pygame.display.set_mode((info.current_w,info.current_h))
            
    pygame.display.set_caption("Make Them Fall")
    gameicon=pygame.image.load('data/images/icon.png')
    pygame.display.set_icon(gameicon)



class scorewindow:
    
    def run(self,gameDisplay,score):
        
        
        
        
        
        background=pygame.image.load("data/images/scorescreen/whitebackground.png")
        gameover=pygame.image.load("data/images/scorescreen/gameover.png")
        newbestscore=pygame.image.load("data/images/scorescreen/newbestscore.png")
        tryagain=pygame.image.load("data/images/scorescreen/tryagain.png")
        backhome=pygame.image.load("data/images/scorescreen/back.png")
        scoreboard=pygame.image.load("data/images/scorescreen/scoreboard.png")
        
        
        
        background=pygame.transform.scale(background,(disp_width-100,info.current_h))
        
        
        font_path = "fonts/arial.ttf"
        font_size = 50
        font_size_large=40
        
        font1= pygame.font.Font(font_path, font_size)
        font1.set_bold(True)
        font2=pygame.font.Font(font_path, font_size_large)
        font2.set_bold(True)
        score=0
        crashed=False
        press=0
        black=(0,0,0)
        white=(255,255,255)
        
        ifbest=False
           
        score=font2.render(str(score),1,(255,255,255))
        
        
        
        
        
        while not crashed:
        #Gtk events
            
            while gtk.events_pending():
                gtk.main_iteration()
            event=pygame.event.poll()
            #totaltime+=timer.tick()
            if event.type == pygame.QUIT:
                #totaltime+=timer.tick()
                crashed=True
               
            mos_x,mos_y=pygame.mouse.get_pos()
            
            if ifbest==True:
            
                gameDisplay.fill(black)
                gameDisplay.blit(background,(0+350,0))
                gameDisplay.blit(gameover,(350+60,50+30))
                
                
                
                gameDisplay.blit(newbestscore,(450,160))
                
                if tryagain.get_rect(center=(450+80,250+10)).collidepoint(mos_x,mos_y):
                    gameDisplay.blit(pygame.transform.scale(tryagain,(293,84)),(448,250))
                    if(pygame.mouse.get_pressed())[0]==1 and press==0:
                        press=1
                        return 1
                
                    if event.type==pygame.MOUSEBUTTONUP:
                        press=0
                
                
                else:
                    
                    gameDisplay.blit(tryagain,(450,250))
                
                
                if backhome.get_rect(center=(450+80,340+10)).collidepoint(mos_x,mos_y):
                    gameDisplay.blit(pygame.transform.scale(backhome,(291,84)),(448,340))
                    if (pygame.mouse.get_pressed())[0]==1 and press==0:
                        press=1
                        return 0
                
                    if event.type==pygame.MOUSEBUTTONUP:
                        press=0
                
                
                else:
                    
                    gameDisplay.blit(backhome,(450,340))
                
                
                
                
            else:
                
                gameDisplay.fill(black)
                gameDisplay.blit(background,(0+350,0))
                gameDisplay.blit(gameover,(350+80,50))
                gameDisplay.blit(scoreboard,(450+5,160))
                
                
                if tryagain.get_rect(center=(450+80+5,250+10+150)).collidepoint(mos_x,mos_y):
                    gameDisplay.blit(pygame.transform.scale(tryagain,(293,84)),(448+5,250+150))
                    if(pygame.mouse.get_pressed())[0]==1 and press==0:
                        press=1
                        return 1
                
                    if event.type==pygame.MOUSEBUTTONUP:
                        press=0
                
                
                else:
                    
                    gameDisplay.blit(tryagain,(450+5,250+150))
                
                
                if backhome.get_rect(center=(450+80+5,340+10+150)).collidepoint(mos_x,mos_y):
                    gameDisplay.blit(pygame.transform.scale(backhome,(291,84)),(448+5,340+150))
                    if (pygame.mouse.get_pressed())[0]==1 and press==0:
                        press=1
                        return 0
                
                    if event.type==pygame.MOUSEBUTTONUP:
                        press=0
                
                
                else:
                    
                    gameDisplay.blit(backhome,(450+5,340+150))
                
                
                
                
                
                
               
            
            pygame.draw.circle(gameDisplay,(255,255,255), (450+140,250+200),5,2)
            pygame.draw.circle(gameDisplay,(255,255,255), (450+140,340+200),5,2)
            
               
                
                
            
                
           
           
            gameDisplay.blit(score,(570,210))
            
            
            
            
            pygame.display.update()
            clock.tick(60)
     
            if crashed==True:                                   # Game crash or Close check
                pygame.quit()
                sys.exit()
     
     
     
     
        # Just a window exception check condition

        event1=pygame.event.get()                                 
        if event1.type == pygame.QUIT:
            crashed=True
   
        if crashed==True:
            pygame.quit()
            sys.exit()
            
a=scorewindow()
a.run(gameDisplay,False)