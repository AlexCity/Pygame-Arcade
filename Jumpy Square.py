import pygame, os, sys, random
from pygame.locals import *
from Arcade import arcade
from colours import *

global screen_width
screen_width = 460
global screen_height
screen_height = 600

class Jumper(pygame.sprite.Sprite):

    def __init__(self, jump_velocity, g, file = None):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.Surface((20,20))
        self.image.fill(pink)
        self.rect = self.image.get_rect()
        self.rect.x = 120
        self.rect.y = 290
        self.jump_velocity = jump_velocity
        self.g = g
        self.velocity = 0

    def jump(self):
        self.velocity = self.jump_velocity * -1

    def update(self):
        self.rect.y += round(self.velocity)
        self.velocity += self.g

class BlockPair(pygame.sprite.Sprite):

    INTERVAL = 80
    WIDTH = 40
    GAP = 200
    SPEED = 4

    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.dokill = False
        r = random.randint(120,380)

        self.top = pygame.Surface((BlockPair.WIDTH, r))
        self.top.fill(maroon)
        self.top_rect = self.top.get_rect()

        self.bottom = pygame.Surface((BlockPair.WIDTH, screen_height - r - BlockPair.GAP))
        self.bottom.fill(maroon)
        self.bottom_rect = self.bottom.get_rect()
        self.bottom_rect.y = r + BlockPair.GAP


        self.image = pygame.Surface((BlockPair.WIDTH, screen_height), pygame.SRCALPHA, 32)
        self.image.blit(self.bottom, (0, r + BlockPair.GAP))
        self.image.blit(self.top, (0,0))
        self.rect = self.image.get_rect()
        self.rect.x = screen_width
        
    def update(self):
        self.rect.x -= BlockPair.SPEED
        self.top_rect.x = self.rect.x
        self.bottom_rect.x = self.rect.x
        if self.rect.x < self.rect.width * -1:
            self.dokill = True


def Game(arcade):

    clock = pygame.time.Clock()
    screen = arcade.get_screen()
    arcade.setCaption(__file__)
    arcade.setWindow(screen_width, screen_height)
    font1 = pygame.font.SysFont('Arial',24, True)

    player = Jumper(16, 0.8)
    sprites = pygame.sprite.RenderUpdates()
    sprites.add(player)

    obstacles = pygame.sprite.RenderUpdates()
    pTimer = 0

    screen_rect = screen.get_rect()
    background = arcade.getImage(__file__, 'Background.png')
    background2 = arcade.getImage(__file__, 'Background.png')
    b_scroll = 0

    hit = False
    start = False
    score = 0

    while True:
        if not start:
            start_text = font1.render('Press Space To Start', False, purple)
            screen.blit(background, (0,0))
            screen.blit(player.image, (120,290))
            screen.blit(start_text, (screen_width // 2 - start_text.get_rect()[2] // 2, screen_height // 1.5 - start_text.get_rect()[3] // 2))
            while not start:
                for event in pygame.event.get():
                    if event.type == pygame.QUIT:
                        pygame.quit()
                        sys.exit()
                    elif event.type == pygame.KEYDOWN:
                        if event.key == K_ESCAPE:
                            arcade.returnToArcade()
                        if event.key == K_SPACE:
                            start = True
                            player.jump()
                
                pygame.display.flip()
                clock.tick(60)
        if hit:
            score_str = 'Your score is: ' + str(score)
            score_text = font1.render(score_str, False, purple)
            background = pygame.Surface((screen_width, screen_height))
            background.fill(black)
            screen.blit(background, (0,0))
            screen.blit(score_text, (screen_width // 2 - score_text.get_rect()[2] // 2, screen_height // 2 - score_text.get_rect()[3] // 2))
            while True:
                for event in pygame.event.get():
                    if event.type == pygame.QUIT:
                        pygame.quit()
                        sys.exit()
                    elif event.type == pygame.KEYDOWN:
                        if event.key == K_ESCAPE:
                            arcade.returnToArcade()
                        else:
                            Game(arcade)
                
                pygame.display.flip()
                clock.tick(60)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            elif event.type == pygame.KEYDOWN:
                if event.key == K_ESCAPE:
                    arcade.returnToArcade()
                player.jump()
            elif event.type == pygame.MOUSEBUTTONDOWN:
                player.jump()

        pTimer +=1
        if pTimer >= BlockPair.INTERVAL:
            pTimer = 0
            obstacles.add(BlockPair())

        sprites.update()
        obstacles.update()
        player.rect.clamp_ip(screen_rect)
        for i in obstacles:
            if i.dokill == True:
                obstacles.remove(i)
                score += 1
            if player.rect.colliderect(i.top_rect) or player.rect.colliderect(i.bottom_rect): hit = True
        screen.blit(background, (b_scroll, 0))
        screen.blit(background2, (b_scroll + 1600, 0))
        b_scroll -= 4
        if b_scroll <= 1600 * -1: b_scroll = 0
        score_text = font1.render(str(score), False, purple)
        screen.blit(score_text, (5, 5))        
        obstacles.draw(screen)
        sprites.draw(screen)
        pygame.display.flip()
        clock.tick(60)



if __name__ == '__main__':
    pygame.init()
    pygame.mixer.init(22050,-16,2,16)
    Game(arcade())
