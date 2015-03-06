
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
    print info.current_h
    gameDisplay = pygame.display.set_mode((info.current_w,info.current_h))
            
    pygame.display.set_caption("Make Them Fall")
    gameicon=pygame.image.load('data/images/icon.png')
    pygame.display.set_icon(gameicon)



class pane2:
    
    def run(self,gameDisplay):
        
        crashed=False 
        orientation1=0
        orientation2=0
        orientation3=0
        orientation4=0
        orientation5=0
        orientation6=0
        
        leftmove=350
        rightmove=659
        limit1=limit2=0
        
        
        leftman=pygame.image.load("data/images/man.png")
        rightman=pygame.transform.flip(leftman,True,False)
        background=pygame.image.load("data/images/2pane.png")
        lspike=pygame.image.load("data/images/Spike.png")
        rspike=pygame.transform.flip(lspike,True,False) 
        background=pygame.transform.scale(background,(disp_width,info.current_h))
        y_axis1=700
        y_axis2=y_axis1+230
        y_axis3=y_axis2+230
        
        y_axisa=750
        y_axisb=y_axisa+230
        y_axisc=y_axisb+230
        
        
        leftquad=leftman
        rightquad=leftman
        f1=f2=0
        m1=m2=0
        time1=time2=0
        
        font_path = "fonts/comicsans.ttf"
        font_size = 50
        font1= pygame.font.Font(font_path, font_size)
        score=0
           
        
        
        while not crashed:
        #Gtk events
            
            while gtk.events_pending():
                gtk.main_iteration()
            event=pygame.event.poll()
            #totaltime+=timer.tick()
            if event.type == pygame.QUIT:
                totaltime+=timer.tick()
                
               
            
            
            gameDisplay.fill(black)
            gameDisplay.blit(background,(0+350,0))
            
            
               
            
            
            # Keypress orientation change
            
            if event.type==pygame.KEYDOWN and event.key==276 and f1==0:
                
                f1=1
                m1=1        #start moving
                
                
                    
                    
            if event.type==pygame.KEYDOWN and event.key==275 and f2==0:
                f2=1
                m2=1        #start moving
                
               
                
                
            # Check for when to stop
            
            if leftmove>608:
                leftquad=rightman
                m1=f1=0
                leftmove=608
                time1=0
                
            if leftmove<350:
                leftquad=leftman
                m1=f1=0
                leftmove=350
                time1=0
                
            if rightmove<659:
                rightquad=leftman
                m2=f2=0
                rightmove=659
                time2=0
                
            if rightmove>916:
                rightquad=rightman
                m2=f2=0
                rightmove=916
                time2=0 
                
           
           
               
            if m1==1:
                
                if leftquad==leftman:
                    leftmove+=30
                if leftquad==rightman:
                    leftmove-=30
                time1+=1
            
            if m2==1:
                
                
                if rightquad==leftman:
                    rightmove+=30
                if rightquad==rightman:
                    rightmove-=30
                time2+=1
               
                
                
            #[350,608]   [659, 916]
            
                
                
                
                
           
            # Guy Display
            
            if leftquad==leftman or leftquad==rightman:
                gameDisplay.blit(leftquad,(leftmove,100))
                
             
            if rightquad==leftman or rightquad==rightman:
                gameDisplay.blit(rightquad,(rightmove,100))
            
            
            ######### SPIKE PART###########
            
            
            if orientation1==0:                     #orientation change
                gameDisplay.blit(lspike,(350,y_axis1))
            
            if orientation1==1:
                gameDisplay.blit(rspike,(589,y_axis1))
                
                
            if orientation2==0:
                gameDisplay.blit(lspike,(350,y_axis2))
            
            if orientation2==1:
                gameDisplay.blit(rspike,(589,y_axis2))
                
                
            if orientation3==0:
                gameDisplay.blit(lspike,(350,y_axis3))
            
            if orientation3==1:
                gameDisplay.blit(rspike,(589,y_axis3))
                
            
            # right side spikes
            if orientation4==0:
                gameDisplay.blit(lspike,(659,y_axisa))
            
            if orientation4==1:
                gameDisplay.blit(rspike,(659+238,y_axisa))
                
            if orientation5==0:
                gameDisplay.blit(lspike,(659,y_axisb))
            
            if orientation5==1:
                gameDisplay.blit(rspike,(659+238,y_axisb))
                
            if orientation6==0:
                gameDisplay.blit(lspike,(659,y_axisc))
            
            if orientation6==1:
                gameDisplay.blit(rspike,(659+238,y_axisc))
                
            
            
                
            
            y_axis1-=6
            y_axis2-=6
            y_axis3-=6
            
            y_axisa-=6
            y_axisb-=6
            y_axisc-=6
            
            if y_axis1==102  or y_axis2==102 or y_axisa==102 or y_axisb==102 or \
                y_axis3==102 or y_axisc==102:
                score+=1
            
            if(y_axis1<-40):
                orientation1=randint(0,10)
                if orientation1>5:
                    orientation1=1
                else:
                    orientation1=0 
                y_axis1=700
                
            
            if(y_axis2<-40):
                orientation2=randint(0,10)
                if orientation2>5:
                    orientation2=1
                else:
                    orientation2=0
                    
                y_axis2=700
                
            if(y_axis3<-40):
                orientation3=randint(0,10)
                if orientation3>5:
                    orientation3=1
                else:
                    orientation3=0
                y_axis3=700
                
                
            
            if(y_axisa<-40):
                orientation4=randint(0,10)
                if orientation4>5:
                    orientation4=1
                else:
                    orientation4=0
                y_axisa=700
                
            
            if(y_axisb<-40):
                orientation5=randint(0,10)
                if orientation5>5:
                    orientation5=1
                else:
                    orientation5=0
                y_axisb=700
                
            
            if(y_axisc<-40):
                orientation6=randint(0,10)
                if orientation6>5:
                    orientation6=1
                else:
                    orientation6=0
                y_axisc=700
                
                
            
            
            
            scores=font1.render(str(score),1,(0,0,0)) 
            gameDisplay.blit(scores,(200+650+20,30))
            
            
            
            if 
            
            
            
            
            
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