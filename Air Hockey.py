#Air Hockey
#Michael Olson
#Feb 24th

import pygame,math,sys,os #imports
from pygame.locals import * 
from Arcade import arcade #import the engine

global arcade #makes a global arcade variable
arcade = arcade() #makes an easy reference to the engine


class Paddle():     #Class for the player paddle
    def __init__(self): #When the class is initialized
        self.coor = (0,0)   #State the variable
        
        self.surface = arcade.makeSurface(40,40, 1)#Makes the surface for drawing

        pygame.draw.circle(self.surface,(255,0,0) ,(20,20),20)
        #Draws the filled in circle on top of the surface that is then updated
        #by the engine
        
    def move(self):#Function for moving the paddle, called every loop
        
        last_pos = self.coor    #records the last position
        self.coor = pygame.mouse.get_pos() #sets the current position equal to
                                            #the mouse, in the form (x,y)
        #speed calculations
        self.move_x = self.coor[0]-last_pos[0]#records the amount the x changes
        self.move_y = self.coor[1]-last_pos[1]#records the amount the y changes

#Class for the puck object
class Puck():   
    def __init__(self):
        self.coor = [200,200]   #Sets the initial position

        #Same as in the paddle object, makes the suface to be passed to the engine
        self.surface = arcade.makeSurface(30,30, 1)
        #Then draws a circle on it
        pygame.draw.circle(self.surface,(0,0,0) ,(15,15),15)

        #Makes the initial speed 0
        self.move_x = 0 
        self.move_y = 0
        
    def move(self):

        #move the puck by the speed
        self.coor[0] += self.move_x
        self.coor[1] += self.move_y
        
        #Collision with the sides
        if self.coor[0]>= 600 or self.coor[0]<=0:
            self.move_x = -1*self.move_x
        if self.coor[1]>= 800 or self.coor[1]<=0:
            self.move_y = -1*self.move_y

        #Slowly slows down the puck over time
        self.move_x -=self.move_x /100
        self.move_y -=self.move_y /100
        
    def changeDirection(self,x,y):# When the object is hit, change the speed/direction
        self.move_x = x
        self.move_y = y

#function for when the puck and paddle collied   
def collision(paddle, puck,paddle_x,paddle_y):
    
    #the speed of the x and y paddle movement are divided by two
    puck_x = paddle_x/2 #By doing the x and y individually the direction stays the same
    puck_y = paddle_y/2 #It works the same way as rise/run

    #Calls the puck to change it's speed, and passes it the new speeds
    puck.changeDirection(puck_x,puck_y)
    

# Main game, to be called by the Arcade
def air_hockey(arcade):

    arcade.setWindow(600,800) #Changes the window to my size instead of the default 600,600
    rink = arcade.getImage(__file__, "rink.png")  #refrences the background image
    
    paddle = Paddle() #initializes a Paddle() class object, to be called by "paddle"
    puck = Puck()   #Makes a Puck object refrenceable by puck
    
    arcade.initBackground(rink)#Calls the engine to initialize the background
    
    hit = False #states the hit variable at the start
    
    pygame.mouse.set_visible(False)#Makes the mouse invisible

    #MAIN GAME LOOP                
    while True:
    
        paddle.move()#Calls the paddle to update it's position and speed
        
        #Finds if the paddle and the puck are colliding for the first time
        if hit == False and arcade.isColliding((puck.surface, puck.coor[0], puck.coor[1]), (paddle.surface, paddle.coor[0], paddle.coor[1]))== True:
            hit = True
            collision(paddle, puck,paddle.move_x,paddle.move_y)#calls the collision function
        elif arcade.isColliding((puck.surface, puck.coor[0], puck.coor[1]), (paddle.surface, paddle.coor[0], paddle.coor[1]))==False:
            hit = False
            
        puck.move()# Calls the puck to move itself

        arcade.getEvents() #Need this to close game properly, put in main loop.

        if arcade.getKey()[K_ESCAPE]: arcade.returnToArcade()
                
        arcade.drawBackground(rink)#Has the engine draw the background

        #Has the engine draw the moving peices
        arcade.draw ((paddle.surface,paddle.coor[0],paddle.coor[1]),
                     (puck.surface,puck.coor[0],puck.coor[1]))
        arcade.update()

#Runs game if executed from file instead of arcade
if __name__ == '__main__':
    pygame.init()
    pygame.mixer.init(22050,-16,2,1024)
    pygame.display.set_caption(os.path.basename(__file__).split('.')[0])


    air_hockey(arcade)                      
