
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
    gameDisplay = pygame.display.set_mode((info.current_w,info.current_h))
            
    pygame.display.set_caption("Make Them Fall")
    gameicon=pygame.image.load('data/images/icon.png')
    pygame.display.set_icon(gameicon)



class pane2:
    
    def run(self,gameDisplay):
        
        crashed=False 
        orientation1=0
        orientation2=0
        
        leftman=pygame.image.load("data/images/man.png")
        rightman=pygame.transform.flip(leftman,True,False)
        background=pygame.image.load("data/images/2pane.png")
        lspike=pygame.image.load("data/images/Spike.png")
        rspike=pygame.transform.flip(lspike,True,False) 
        background=pygame.transform.scale(background,(disp_width,info.current_h))
        y_axis1=700
        y_axis2=y_axis1+50
        
        
        while not crashed:
        #Gtk events
            
            while gtk.events_pending():
                gtk.main_iteration()
            event=pygame.event.poll()
            
            
            #for event in pygame.event.get():
                
            #totaltime+=timer.tick()
            if event.type == pygame.QUIT:
                totaltime+=timer.tick()
                
                
            #print event
            
            if event.type==pygame.KEYDOWN and event.key==276:
                print event
                
            
            '''
            gameDisplay.fill(black)
            gameDisplay.blit(background,(0+350,0))
            
            if orientation1==0:                     #orientation change
                gameDisplay.blit(lspike,(350,y_axis1))
            
            if orientation1==1:
                gameDisplay.blit(rspike,(589,y_axis1))
                
                
            if orientation2==0:
                gameDisplay.blit(lspike,(659,y_axis2))
            
            if orientation2==1:
                gameDisplay.blit(rspike,(659+238,y_axis2))
               
            
            gameDisplay.blit(leftman,(350,100))
            gameDisplay.blit(leftman,(659,100))
            
            
            
            
            y_axis1-=5
            y_axis2-=5
            
            if(y_axis1<-40):
                orientation1=randint(0,1)
                y_axis1=700
                
            
            if(y_axis2<-40):
                orientation2=randint(0,1)
                y_axis2=700
            
            '''
            
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
            
a=pane2()
a.run(gameDisplay)