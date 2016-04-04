#Assignment 5
#Class: ICS4U-02
#Name: Alex Taylor
#Date: March 2, 2016
#Description: Ball-Colour Game

import pygame, sys, os
from pygame.locals import *
from Arcade import arcade
from random import randint

pygame.init()



def game(arcade):
    while True:
        restart = False
        arcade.setWindow(1250,900)
        screen = arcade.get_screen()
        pygame.display.set_caption('Ball-Colour Game')

        #Variables
        colour1 = 254
        colour2 = 254
        colour3 = 254

        x = 625
        y = 700
        x1 = randint(100,800)
        y1 = randint(100,600)
        x2 = randint(100,1150)
        y2 = randint(100,400)
        x3 = randint(750,1150)
        y3 = randint(100,800)
        x4 = randint(100,800)
        y4 = randint(100,600)
        x5 = randint(100,1150)
        y5 = randint(100,400)
        x6 = randint(750,1150)
        y6 = randint(100,800)

        vE1 = randint(-6,-2)
        vN1 = randint(2,6)
        vE2 = randint(2,6)
        vN2 = randint(-6,-3)
        vE3 = randint(2,6)
        vN3 = randint(2,6)
        vE4 = randint(-6,-3)
        vN4 = randint(3,6)
        vE5 = randint(3,6)
        vN5 = randint(-6,-3)
        vE6 = randint(3,6)
        vN6 = randint(3,6)

        Start = 1
        Difficulty = 1
        Score = 0
        Life = 1

        #Text Variables
        Font1 = pygame.font.SysFont("monospace", 36)
        Font2 = pygame.font.SysFont("monospace", 16)
        Font3 = pygame.font.SysFont("monospace", 56)

        label1 = Font1.render("Q = Blue          W = Green          E = Red", 1, (255,255,0))
        label2 = Font1.render('Score:', 1, (255,255,0))
        label3 = Font1.render(str(Score), 1, (255,255,0))
        label4 = Font2.render('Esc = Quit', 1, (255,255,0))
        label5 = Font3.render('YOU LOST', 1, (255,255,0))
        label6 = Font3.render('Ball-Colour Game', 1, (255,255,0))
        label7 = Font1.render('Easy', 1, (0,255,0))
        label8 = Font1.render('Hard', 1, (255,0,0))
        label9 = Font2.render('R to retry', 1, (255,255,0))
        
        while True:

            arcade.getEvents()
            #Menu Display
            while Start == 1:
                arcade.getEvents()
                screen.blit (label6, (375, 450))
                screen.blit (label7, (425, 800))
                screen.blit (label8, (725, 800))
                screen.blit(label4, (0, 0))
                if Difficulty == 1:
                    pygame.draw.rect(screen,(0,255,0),(420,790,100,50),3) #Difficulty selection
                if Difficulty == 2:
                    pygame.draw.rect(screen,(255,0,0),(720,790,100,50),3)

                pressed = pygame.key.get_pressed()
                if pressed[K_RETURN]: #Start Game
                    Start = 0
                elif pressed[K_LEFT]: #Difficulty becomes Easy
                    Difficulty = 1
                elif pressed[K_RIGHT]:#Difficulty becomes Hard
                    Difficulty = 2
                elif pressed[K_ESCAPE]:#Quits game
                    arcade.returnToArcade()
                pygame.display.flip() #Updates screen
                screen.fill((0,0,0))

                for event in pygame.event.get():
                    if event.type == pygame.QUIT:
                        pygame.quit()
                        sys.exit()
                
            pygame.draw.circle(screen,(colour1,colour2,colour3),(x,y),50) #Draws player
            pygame.display.flip()
            screen.fill((0,0,0))
            screen.blit(label1, (100, 50))
            screen.blit(label2, (450, 900))
            screen.blit(label3, (600, 900))
            screen.blit(label4, (0, 0))

            pressed = pygame.key.get_pressed()
            if pressed[pygame.K_ESCAPE]:#Quits game
                pygame.quit()
            if pressed[pygame.K_DOWN]:  #Player moves down
                y += 4
            if pressed[pygame.K_UP]:    #Player moves up
                y -= 4
            if pressed[pygame.K_LEFT]:  #Player moves left
                x -= 4
            if pressed[pygame.K_RIGHT]: #Player moves right
                x += 4
            if pressed[pygame.K_q]:     #Player changes colour to blue
                colour1 = 0
                colour2 = 0
                colour3 = 255
            elif pressed[pygame.K_w]:   #Player changes colour to green
                colour1 = 0
                colour2 = 255
                colour3 = 0
            elif pressed[pygame.K_e]:   #Player changes colour to red
                colour1 = 255
                colour2 = 0
                colour3 = 0
                
            if x >= 1200:   #Player cannot pass these borders
                x = 1200
            if y >= 900:
                y = 900
            if x <= 50:
                x = 50
            if y <= 50:
                y = 50

            if Score %2 == 0:
                pygame.draw.circle(screen,(255,255,0),(50,50),15)   #Determines where next objective will be
                if x <= 100 and x >= 0 and y <= 105 and y >= 0:
                    Score += 1
            elif Score %2 == 1:
                pygame.draw.circle(screen,(255,255,0),(1200,900),15)
                if x <= 1200 and x >= 1130 and y <= 900 and y >= 820:
                    Score += 1
            label3 = Font1.render(str(Score), 1, (255,255,0))       #Updates 

            x1 += vE1   #Enemy balls movement
            y1 += vN1
            x2 += vE2
            y2 += vN2
            x3 += vE3
            y3 += vN3
                
            if x1 >= 1225:  #Enemy balls borders
                x1 = 1225
                vE1 = -vE1  #Enemy balls bounce off wall and revese direction
            if y1 >= 925:
                y1 = 925
                vN1 = -vN1
            if x1 <= 25:
                x1 = 25
                vE1 = -vE1
            if y1 <= 25:
                y1 = 25
                vN1 = -vN1

            if x2 >= 1225:
                x2 = 1225
                vE2 = -vE2
            if y2 >= 925:
                y2 = 925
                vN2 = -vN2
            if x2 <= 25:
                x2 = 25
                vE2 = -vE2
            if y2 <= 25:
                y2 = 25
                vN2 = -vN2

            if x3 >= 1225:
                x3 = 1225
                vE3 = -vE3
            if y3 >= 925:
                y3 = 925
                vN3 = -vN3
            if x3 <= 25:
                x3 = 25
                vE3 = -vE3
            if y3 <= 25:
                y3 = 25
                vN3 = -vN3
                
            pygame.draw.circle(screen,(0,0,255),(x1,y1),25) #Displays enemy balls
            pygame.draw.circle(screen,(0,255,0),(x2,y2),25)
            pygame.draw.circle(screen,(255,0,0),(x3,y3),25)

            if x - x1 <= 55 and x - x1 >= -55 and y - y1 <= 55 and y - y1 >= -55 and colour3 !=255: #Lose life upon collision if colour is not same
                Life = 0
            if x - x2 <= 55 and x - x2 >= -55 and y - y2 <= 55 and y - y2 >= -55 and colour2 !=255:
                Life = 0
            if x - x3 <= 55 and x - x3 >= -55 and y - y3 <= 55 and y - y3 >= -55 and colour1 !=255:
                Life = 0

            if Difficulty == 2: #Adds extra enemies on 'Hard' difficulty
                x4 += vE4
                y4 += vN4
                x5 += vE5
                y5 += vN5
                x6 += vE6
                y6 += vN6
                    
                if x4 >= 1225:
                    x4 = 1225
                    vE4 = -vE4
                if y4 >= 925:
                    y4 = 925
                    vN4 = -vN4
                if x4 <= 25:
                    x4 = 25
                    vE4 = -vE4
                if y4 <= 25:
                    y4 = 25
                    vN4 = -vN4
                
                if x5 >= 1225:
                    x5 = 1225
                    vE5 = -vE5
                if y5 >= 925:
                    y5 = 925
                    vN5 = -vN5
                if x5 <= 25:
                    x5 = 25
                    vE5 = -vE5
                if y5 <= 25:
                    y5 = 25
                    vN5 = -vN5

                if x6 >= 1225:
                    x6 = 1225
                    vE6 = -vE6
                if y6 >= 925:
                    y6 = 925
                    vN6 = -vN6
                if x6 <= 25:
                    x6 = 25
                    vE6 = -vE6
                if y6 <= 25:
                    y6 = 25
                    vN6 = -vN6
                    
                pygame.draw.circle(screen,(0,0,255),(x4,y4),25)
                pygame.draw.circle(screen,(0,255,0),(x5,y5),25)
                pygame.draw.circle(screen,(255,0,0),(x6,y6),25)

                if x - x4 <= 55 and x - x4 >= -55 and y - y4 <= 55 and y - y4 >= -55 and colour3 !=255:
                    Life = 0
                if x - x5 <= 55 and x - x5 >= -55 and y - y5 <= 55 and y - y5 >= -55 and colour2 !=255:
                    Life = 0
                if x - x6 <= 55 and x - x6 >= -55 and y - y6 <= 55 and y - y6 >= -55 and colour1 !=255:
                    Life = 0


            while Life == 0:        #Death Screen
                arcade.getEvents()
                screen.fill((0,0,0))
                screen.blit(label5, (470, 450))
                screen.blit(label4, (0, 0))
                screen.blit(label3, (600, 900))
                screen.blit(label2, (450, 900))
                screen.blit(label9, (1130, 0))
                pygame.display.flip()
                pressed = pygame.key.get_pressed()
                if pressed[pygame.K_ESCAPE]:    #Quits game
                    arcade.returnToArcade()
                if pressed[pygame.K_r]:         #Restarts game
                    restart = True
                    break
            if restart == True:
                break
            pygame.time.Clock().tick(240) #Set FPS


if __name__ == '__main__':
    pygame.init
    pygame.display.set_caption(os.path.basename(__file__).split(',')[0])
    game(arcade())      #Runs Game
