# Pygame Arcade
# ICS4U-02
# 2016
# A collection of games built using pygame by the ICS4U-02 class, all running in a virtual arcade.

import pygame, sys, os
from pygame.locals import *
from colours import *
from importlib import import_module

class arcade:
    global previous_areas; previous_areas = []
    global act_rects; act_rects = []

    def __init__(self): # This is automatically run
        flags = HWSURFACE | DOUBLEBUF #| NOFRAME
        screen_x, screen_y = 600, 600
        self.screen = pygame.display.set_mode((screen_x,screen_y),flags)
        pygame.display.set_icon(pygame.image.load(os.getcwd() + '\\resources\window_icon.png').convert_alpha())

    def UI(arcade):
        arcade.setCaption(__file__)
        arcade.setWindow(600,600)
        bg = arcade.getImage('\\','window_icon.png', 1)
        arcade.initBackground(bg)
        Arial32 = pygame.font.SysFont('Arial',32)
        text1 = Arial32.render('Welcome to the Pygame Arcade!',False, white)

        while True:

            arcade.getEvents()
            arcade.drawBackground(bg)
            arcade.draw((text1, 50, 50))
            mouse = arcade.getMousePos()
            mouseClicked = arcade.getMouseButton()
            if mouse[0] > 100 and mouse[1] > 100 and mouse[0] < 500 and mouse[1] < 500 and mouseClicked[0] == True:
                #import_module('Test Game').Game(arcade)
                import_module('Air Hockey').air_hockey(arcade)

    #Framework
    def getEvents(self): # You NEED this to be called in your main loop
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
        pygame.event.pump()

    def setWindow(self, width, height): # Change your games window size
        flags = HWSURFACE | DOUBLEBUF
        screen_x, screen_y = width, height
        self.screen = pygame.display.set_mode((screen_x,screen_y),flags)
        pygame.display.set_icon(pygame.image.load(os.getcwd() + '\\resources\window_icon.png').convert_alpha())

    def getKey(self): #returns any pressed keys
        return pygame.key.get_pressed()

    def getMousePos(self): # returns (x,y) position of mouse
        return pygame.mouse.get_pos()

    def getMouseButton(self): # returns what mouse buttons are pressed
        return pygame.mouse.get_pressed()

    def getImage(self, path, file, alpha = 0): # returns loaded pygame image from folder
        if alpha:
            return pygame.image.load(os.getcwd() + '\\resources\\' + os.path.basename(path).split('.')[0] + '\\' + file).convert_alpha()
        return pygame.image.load(os.getcwd() + '\\resources\\' + os.path.basename(path).split('.')[0] + '\\' + file).convert()

    def getSound(self, path, file): # returns loaded sound file from folder
        return pygame.mixer.Sound(os.getcwd() + '\\resources\\' + os.path.basename(path).split('.')[0] + '\\' + file)

    def isColliding(self, obj1, obj2): # checks if two surfaces are collliding
        rect1 = pygame.Rect(obj1[1], obj1[2], pygame.Surface.get_bounding_rect(obj1[0])[2], pygame.Surface.get_bounding_rect(obj1[0])[3])
        rect2 = pygame.Rect(obj2[1], obj2[2], pygame.Surface.get_bounding_rect(obj2[0])[2], pygame.Surface.get_bounding_rect(obj2[0])[3])
        return rect1.colliderect(rect2)

    def drawBackground(self, background): # draws background but doesnt update
        self.screen.blit(background, (0, 0))

    def initBackground(self, background): # call this once outside of the main loop to initialize and update background
        self.screen.blit(background, (0, 0))
        pygame.display.update()

    def draw(self, *args): #arg is (surface, x, y)
        global previous_areas
        global act_rects
        update_areas = []
        for arg in args:
            self.screen.blit(arg[0],(arg[1],arg[2]))
            area = pygame.Surface.get_bounding_rect(arg[0])
            area[0], area[1] = arg[1] - 10, arg[2] - 10
            area[2], area[3] = area[2] + 20, area[3] + 20
            update_areas.append(area)
        act_rects.append(update_areas[:])
        act_rects.append(previous_areas[:])
        previous_areas = update_areas[:]

    def update(self):
        global act_rects
        for i in act_rects:
            pygame.display.update(i)
        act_rects = []
            
    def makeSurface(self, width, height, alpha = 0): # creates a surface with transparency
        if alpha:
            return pygame.Surface((width,height), pygame.SRCALPHA, 32).convert_alpha()
        return pygame.Surface((width,height))

    def setCaption(self, file): # sets window title
        pygame.display.set_caption(os.path.basename(file).split('.')[0])

    def returnToArcade(self): # when you end your game call this in final product
        pygame.mouse.set_visible(True)
        self.setWindow(600,600)
        self.UI()



if __name__ == '__main__':
    #If arcade.py is executed, open game selector UI
    #All games are executable as a standalone game.
    #All games are contained in a single .py file + resources (sprites, fonts, etc.)
    pygame.init()
    pygame.mixer.init(22050,-16,2,1024)
    arcade.UI(arcade())


