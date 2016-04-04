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
        pygame.display.set_icon(pygame.image.load(os.getcwd() + '\\resources\\window_icon.png').convert_alpha())

    def UI(arcade):
        arcade.__init__()
        arcade.setCaption(__file__)
        arcade.setWindow(1125,750)
        bg = arcade.getImage('\\','UI_bg.png')
        arcade.initBackground(bg)
        UI_font1 = pygame.font.Font(os.getcwd() + '\\resources\\UI_font1.ttf', 48)
        UI_font2 = pygame.font.Font(os.getcwd() + '\\resources\\UI_font1.ttf', 16)
        text1 = UI_font1.render('Welcome to the Pygame Aracade!', False, white)
        selections = [
            UI_font2.render('1: Air Hockey', False, white),
            UI_font2.render('2: Block Breaker', False, white),
            UI_font2.render('3: Snow Whirled', False, white),
            UI_font2.render('4: Pong', False, white),
            UI_font2.render('5: Colourful Balls', False, white),
            UI_font2.render('6: Jumpy Square', False, white)
                      ]
        selections_rects = [x.get_rect() for x in selections]
        game = 'Arcade'
        while True:
            arcade.getEvents()
            arcade.drawBackground(bg)
            arcade.draw((text1, 177, 10))
            for i in range(len(selections)):
                selections_rects[i][0], selections_rects[i][1] = 563 - selections[i].get_rect().width//2, 70*(i+2)
                arcade.draw((selections[i], selections_rects[i][0], selections_rects[i][1]))
            arcade.update()
            pressed = arcade.getKey()
            mouse_pos = pygame.mouse.get_pos()
            mouse_click = pygame.mouse.get_pressed()[0]
            if pressed[K_1] or pressed[K_KP1] or (mouse_click and selections_rects[0].collidepoint(mouse_pos)): game = 'Air Hockey'; import_module('Air Hockey').air_hockey(arcade)
            if pressed[K_2] or pressed[K_KP2] or (mouse_click and selections_rects[1].collidepoint(mouse_pos)): game = 'Block Breaker'; import_module('Block Breaker').Game(arcade)
            if pressed[K_3] or pressed[K_KP3] or (mouse_click and selections_rects[2].collidepoint(mouse_pos)): game = 'Snow Whirled'; import_module('Snow Whirled').SnowWhirled(arcade)
            if pressed[K_4] or pressed[K_KP4] or (mouse_click and selections_rects[3].collidepoint(mouse_pos)): game = 'Pong'; import_module('Pong').Game(arcade)
            if pressed[K_5] or pressed[K_KP5] or (mouse_click and selections_rects[4].collidepoint(mouse_pos)): game = 'Colourful Balls'; import_module('Colourful Balls').game(arcade)
            if pressed[K_6] or pressed[K_KP6] or (mouse_click and selections_rects[5].collidepoint(mouse_pos)): game = 'Jumpy Square'; import_module('Jumpy Square').Game(arcade)
            if pressed[K_ESCAPE]:
                pygame.quit()
                sys.exit()
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
            area[0], area[1] = arg[1] - 20, arg[2] - 20
            area[2], area[3] = area[2] + 40, area[3] + 40
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
        
    def get_screen(self):
        return self.screen



if __name__ == '__main__':
    #If arcade.py is executed, open game selector UI
    #All games are executable as a standalone game.
    #All games are contained in a single .py file + resources (sprites, fonts, etc.)
    pygame.mixer.init(22050,-16,2,16)
    pygame.init()
    arcade.UI(arcade())


