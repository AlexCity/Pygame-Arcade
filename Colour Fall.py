# Pygame Mini Game "Colour Catcher"
# ICS4U-02
# 2016
# Andrew Foster
# A game to test out pygame

import pygame, sys, Arcade, os
from pygame.locals import * 
from random import randint
def game(arcade): 
#Declaration of variables
    #Start Menu
    Start= True
    Life= True
    blife= True
    speed=4

    #rectangle cord 
    x=400 
    y=500 

    #ballcord 
    ballcordx = randint(0,900) 
    ballcordy= 50
    ballspeed=2

    #rectangle colour 
    colour1=255 
    colour2=1 
    colour3=1 

    #ball colour 
    ballcolour1=randint(1,3) 

    if ballcolour1==1: 
        ballcolour1=255 
        ballcolour2=1 
        ballcolour3=1 
    if ballcolour1==2: 
        ballcolour1=1 
        ballcolour2=255 
        ballcolour3=1 
    if ballcolour1 ==3: 
        ballcolour1=1 
        ballcolour2=1 
        ballcolour3=255 



    #score
    score= 0

    #Fonts on screen 
    font1=pygame.font.SysFont("monospace",30) 
    label1= font1.render("You Lose",1,(255,255,255))
    font2=pygame.font.SysFont("monospace",24)
    label3= font1.render("Welcome to Colour Catch",1,(255,255,255))
    label4= font2.render("Press Enter to Play",1,(255,255,255))
    label5= font2.render("Press Enter to Return to Menu",1,(255,255,255))
    label6= font2.render("A = Red ",1,(255,255,255))
    label7= font2.render("S = Green ",1,(255,255,255))
    label8= font2.render("D = Blue ",1,(255,255,255))

    
    rectangle = pygame.Surface((100, 10)) 
    arcade.setWindow(900, 600)
    screen= arcade.get_screen()
    while True:
        
        screen.fill((0,0,0))
        #Start Menu
        while Start == True:
            arcade.getEvents()
            pressed= pygame.key.get_pressed()
            screen.fill((0,0,0))
            screen.blit(label3,(250,75))
            screen.blit(label4,(300,350))
            screen.blit(label6,(150,400))
            screen.blit(label7,(350,400))
            screen.blit(label8,(550,400))
            #Starts the game
            if pressed[K_RETURN]:
                Start = False
            if pressed[K_ESCAPE]:
                arcade.returnToArcade()
            pygame.display.flip()
            
        #score board
        label2 = font2.render("Score: "+str(score),1,(255,255,255))
        screen.blit(label2,(350,50))
        #drawing the objects
        rectangle.fill((colour1, colour2, colour3), (0,0,100,10)) 
        screen.blit(rectangle, (x, y))
        #drawing the ball's position and colour
        if blife== True: 
            pygame.draw.circle(screen,(ballcolour1,ballcolour2,ballcolour3), (int(ballcordx),int(ballcordy)),10)      
        else:
            ballcordx = randint(0,900) 
            ballcordy= 50
            #random colour for the ball determinded
            ballcolour1=randint(1,3) 
            if ballcolour1==1: 
                ballcolour1=255 
                ballcolour2=1 
                ballcolour3=1 
            if ballcolour1==2: 
                ballcolour1=1 
                ballcolour2=255 
                ballcolour3=1 
            if ballcolour1 ==3: 
                ballcolour1=1 
                ballcolour2=1 
                ballcolour3=255
            pygame.draw.circle(screen,(ballcolour1,ballcolour2,ballcolour3), (ballcordx,ballcordy),10)
            blife=True

        #movements and controls
        pressed= pygame.key.get_pressed() 
        if pressed[K_LEFT]: 
            x-=speed
        if pressed[K_RIGHT]: 
            x+=speed
        if pressed[K_a]: 
            colour1= 255 
            colour2=1 
            colour3=1 
        if pressed[K_s]: 
            colour1= 1 
            colour2=255 
            colour3=1 
        if pressed[K_d]: 
            colour1= 1 
            colour2=1 
            colour3=255
            
        #boarders 
        if x>= 800: 
            x=800 
        if y>= 890: 
            y= 890 
        if x<=0: 
            x=0 
        if y<=0: 
            y=0
        speed += 0.0001
        ballspeed += 0.0001
        #ball related
        if ballcordy>=520:
            Life=False
        if blife== True:
            ballcordy+= ballspeed
        else:
            ballcordy== ballcordy
        
        #when the ball hits the paddle it checks the colour to see if it works and it checks to see if the position is in a correct position,
        #if it is it sets the balls life to false causing the ball to be sent back up top 
        if x-ballcordx<= 0 and x-ballcordx>= -100 and ballcordy>=500 and ballcordy<=510 and ballcolour1== colour1 and ballcolour2== colour2 and ballcolour3== colour3: 
            score =score+1
            blife= False

        #End Screen
        if Life==False:
            screen.fill((0,0,0))
            screen.blit(label1,(375,250))
            screen.blit(label5,(250,500))
            #label2= font2.render("Score: "+str(score),1,(255,255,255))
            screen.blit(label2,(395,50))
            pressed = pygame.key.get_pressed()
            if pressed[K_RETURN]:
                game(arcade)
        pygame.display.flip()
        if pressed[K_ESCAPE]:
            arcade.returnToArcade()
        arcade.getEvents()

if __name__ == '__main__':
    pygame.init()
    pygame.display.set_caption(os.path.basename(__file__).split('.')[0])
    game(Arcade.arcade())
        
