import gtk
import pickle
import pygame
import sys
from random import *




class rules:
    
    def run(self,gameDisplay,info):
        
        
        disp_width=600
        
        press=0
        crashed=False
        black=(0,0,0)
        clock=pygame.time.Clock()
        timer=pygame.time.Clock()
        
        background=pygame.image.load("data/images/rulesbackground.png")
        back=pygame.image.load("data/images/back.png")
        
        
        
        background=pygame.transform.scale(background,(disp_width-100,info.current_h-40))
        back=pygame.transform.scale(back,(80,50))
        
        sound = True
        try:
            pygame.mixer.init()
        except Exception, err:
            sound = False
            print 'error with sound', err 
        
        
        
        
        
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
            
            
            
            gameDisplay.fill(black)
            gameDisplay.blit(background,(0+350,0))
                
                
                
                
                
            if back.get_rect(center=(750+35,20+15)).collidepoint(mos_x,mos_y):
                gameDisplay.blit(pygame.transform.scale(back,(85,55)),(725,20))
                if(pygame.mouse.get_pressed())[0]==1 and press==0:
                    press=1
                    return 
                
                if event.type==pygame.MOUSEBUTTONUP:
                    press=0
            
            
            else:
                gameDisplay.blit(back,(725,20))
                
            
            #pygame.draw.circle(gameDisplay,(255,255,255), (750+35,20+15),5,2)
            
            
            
            
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
       
'''       
a=scorewindow()
a.run(gameDisplay,False)
'''
