import pygame
import gtk
import sys
import os



class rule:
    
    

    def make(self,gameDisplay,sound):
        
        
        check=0
        background=pygame.image.load("images/ruless.jpg").convert()
        background=pygame.transform.scale(background,(900,715))
        crashed=False
        
        clock=pygame.time.Clock()
        back=pygame.image.load("buts/welcomescreen/back.png")
        back=pygame.transform.scale(back,(100,50))
        if sound:
            s2=pygame.mixer.Sound("sound/success.ogg")
            s2.play(0)
            s1=pygame.mixer.Sound("sound/button.ogg")
        
        
        while not crashed:
            # Gtk events
            while gtk.events_pending():
                gtk.main_iteration()
            event=pygame.event.poll()
        
            if event.type == pygame.QUIT:
                crashed = True
            
            mos_x,mos_y=pygame.mouse.get_pos()
            
            
            gameDisplay.blit(background,(0+280-50,0))
            
            
            if back.get_rect(center=(455-30+280,535+60+15)).collidepoint(mos_x,mos_y):                                #BACK
                gameDisplay.blit(pygame.transform.scale(back,(110,55)),(440-30+280,520+60+15))
                
                if (pygame.mouse.get_pressed())[0]==1 and check==0:
                    if sound:
                        s1.play()
                    check=1
                    
                    return
                  
                if event.type==pygame.MOUSEBUTTONUP:
                    check=0
            
            else:
                gameDisplay.blit(back,(440-30+280,520+60+15))
                
                

            
            
            
            pygame.display.update()
            clock.tick(50)
     
            if crashed==True:                                   # Game crash or Close check
                pygame.quit()
                sys.exit()
            
        
        event1=pygame.event.poll()                                 
        if event1.type == pygame.QUIT:
            crashed=True
   
        if crashed==True:
            pygame.quit()
            sys.exit()


