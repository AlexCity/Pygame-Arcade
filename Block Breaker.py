import pygame, os, sys
from pygame.locals import *
from Arcade import arcade
from colours import *    

class Paddle(pygame.sprite.Sprite):
    def __init__(self, colour, width, height):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.Surface([width,height])
        self.image.fill(colour)
        self.rect = self.image.get_rect()
    def set_speed(self, speed):     self.speed = speed
    def move_right(self):           self.rect.x += self.speed
    def move_left(self):            self.rect.x -= self.speed
    def move_up(self):              self.rect.y -= self.speed
    def move_down(self):            self.rect.y += self.speed

class Circle(pygame.sprite.Sprite):
    def __init__(self, colour, radius):
        pygame.sprite.Sprite.__init__(self)
        self.radius = radius
        self.image = pygame.Surface([radius*2,radius*2], pygame.SRCALPHA, 32)
        self.circle = pygame.draw.circle(self.image, colour, (radius,radius), radius)
        self.rect = self.image.get_rect()
        self.dx = 3
        self.dy = 3
    def bounce_x(self):
        self.dx *= -1
    def bounce_y(self):
        self.dy *= -1

class Brick(pygame.sprite.Sprite):
    def __init__(self, colour):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.Surface((40,25))
        self.image.fill(colour)
        self.rect = self.image.get_rect()
    
def exit_game():
    pygame.quit()
    sys.exit()

def intersects(rect, r, center):
    circle_distance_x = abs(center[0]-rect.centerx)
    circle_distance_y = abs(center[1]-rect.centery)
    if circle_distance_x > rect.w/2.0+r or circle_distance_y > rect.h/2.0+r:
        return False
    if circle_distance_x <= rect.w/2.0 or circle_distance_y <= rect.h/2.0:
        return True
    corner_x = circle_distance_x-rect.w/2.0
    corner_y = circle_distance_y-rect.h/2.0
    corner_distance_sq = corner_x**2.0 +corner_y**2.0
    return corner_distance_sq <= r**2.0

def end(state):
    if state == True: #win
        pass
    elif state == False: #lose
        pass

def Game(arcade):
    arcade.setWindow(600,600)
    screen = arcade.get_screen()
    font1 = pygame.font.SysFont('Arial',24, True)
    arcade.setCaption(__file__)
    blip = arcade.getSound(__file__, 'blip.wav')
    player = Paddle(teal, 100, 10)
    player.rect.x, player.rect.y = 250, 550
    player.set_speed(5)
    ball = Circle(pink, 10)
    ball.rect.x, ball.rect.y = 290, 500
    sprites = pygame.sprite.RenderUpdates()
    sprites.add(player, ball)
    bricks = pygame.sprite.RenderUpdates()
    state = None
    for i in range(5):
        for j in range(15):
            brick = Brick(red)
            brick.rect.x, brick.rect.y = 40*j,25*(i+2)
            bricks.add(brick)
    background = pygame.Surface((600,600))
    background.fill(black,(0,0,600,600))
    screen.blit(background, (0,0))
    score = 0
    pygame.display.flip()
    screen_rect = screen.get_rect()
    while True:
        arcade.getEvents()
        pressed = pygame.key.get_pressed()
        if pressed[K_RIGHT]:    player.move_right()
        if pressed[K_LEFT]:     player.move_left()
        if pressed[K_ESCAPE]:   arcade.returnToArcade()
        if pressed[K_r]:        Game(arcade)
        if intersects(player.rect, ball.radius, (ball.rect.x + ball.radius, ball.rect.y + ball.radius)):
            ball.dy = abs(ball.dy)
            if ball.rect[0] > player.rect[0] + 25 and ball.rect[0] + ball.rect[2] < player.rect[0] + player.rect[2] - 25: #center zone
                if ball.dx > 0:
                    ball.dx = 3
                else:
                    ball.dx = -3
            elif ball.rect[0] < player.rect[0] + 25: #left zone
                ball.dx = 4
            elif ball.rect[0] + ball.rect[2] > player.rect[0] + player.rect[2] - 25: #right zone
                ball.dx = -4   
        if ball.rect.x <= 0 or ball.rect.x >= 600 - ball.radius*2: ball.bounce_x()
        if ball.rect.y <= 0: ball.bounce_y()
        if ball.rect.y >= 590 - ball.radius*2: end(False)
        ball.rect.x -= ball.dx
        ball.rect.y -= ball.dy
        kill_list = []
        for brick in bricks:            
            if intersects(brick.rect, ball.radius, (ball.rect.x + ball.radius, ball.rect.y + ball.radius)):
                kill_list.append(brick)
                ball.bounce_y()
                blip.play()
                score += 1
        if len(bricks) == 0: end(True)
        score_text = font1.render(str(score), False, maroon)
        bricks.clear(screen, background)
        bricks.remove(kill_list)
        player.rect.clamp_ip(screen_rect) # Restricts player from going off-screen
        ball.rect.clamp_ip(screen_rect)
        screen.blit(background, (0,0))
        screen.blit(score_text, (5,5))
        pygame.display.update([pygame.Rect(r[0]-10, r[1]-10, r[2]+20, r[3]+20) for r in sprites.draw(screen)] + bricks.draw(screen) + [pygame.Rect(5,5,30,30)])
        pygame.time.Clock().tick(120) # Set FPS


if __name__ == '__main__':
    pygame.mixer.init(22050,-16,2,16)
    pygame.init()
    Game(arcade())
