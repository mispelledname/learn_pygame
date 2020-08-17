import pygame
from pygame.locals import *
import sys

pygame.init()
vec = pygame.math.Vector2 

# game constants 
HEIGHT = 840        # window height
WIDTH  = 1120       # window width
ACC    = 0.5        # acceleration
FRIC   = -0.12      # friction
FPS    = 60         # frames per second 

# initialize clock
FramePerSec = pygame.time.Clock()

# display screen
displaysurface = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Game")

class Player(pygame.sprite.Sprite):
    def __init__(self):
        ''' initialize player '''
        super().__init__()
        # player display
        self.surf = pygame.Surface((80, 80))
        self.surf.fill((255,255,0))
        self.rect = self.surf.get_rect()
        # player movement
        self.pos = vec((10, HEIGHT-10))
        self.vel = vec(0,0)
        self.acc = vec(0,0)

    def move(self):
        ''' move player upon key presses'''
        self.acc = vec(0,0)
        # left and right movement from key press 
        pressed_keys = pygame.key.get_pressed()
        if pressed_keys[K_LEFT]:
            self.acc.x = -ACC
        if pressed_keys[K_RIGHT]:
            self.acc.x = ACC
        # update position from velocity equations 
        self.acc.x += self.vel.x * FRIC
        self.vel += self.acc
        self.pos += self.vel + 0.5 * self.acc
        # screen wrapping 
        if self.pos.x > WIDTH:
            self.pos.x = 0
        if self.pos.x < 0:
            self.pos.x = WIDTH
        self.rect.midbottom = self.pos

class Platform(pygame.sprite.Sprite):
    def __init__(self):
        ''' initialize new platform '''
        super().__init__()
        self.surf = pygame.Surface((WIDTH, 20))
        self.surf.fill((255,0,0))
        self.rect = self.surf.get_rect(center = (WIDTH/2, HEIGHT - 10))

    def move(self):
        pass

class Level:
    def __init__(self):
        self.all_sprites = pygame.sprite.Group()
        self.all_sprites.add(Platform())
        self.all_sprites.add(Player())
        
level = Level()
PT1 = Platform()
P1 = Player()
all_sprites = pygame.sprite.Group()
all_sprites.add(PT1)
all_sprites.add(P1)

# game loop
while True:
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()

    displaysurface.fill((0,0,0))

    # for entity in level.all_sprites:
    for entity in all_sprites:
        displaysurface.blit(entity.surf, entity.rect)
        entity.move()

    pygame.display.update()
    FramePerSec.tick(FPS)