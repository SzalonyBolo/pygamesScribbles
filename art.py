from select import select
from turtle import left, pos
import pygame
from pygame.locals import *
import sys

pygame.init()
vec = pygame.math.Vector2  # 2 for two dimensional
 
WIDTH = 800
HEIGHT = 600

FPS = 60
 
FramePerSec = pygame.time.Clock()
 
displaysurface = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Game")

class platform(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.surf = pygame.Surface((WIDTH, 20))
        self.surf.fill((255,0,0))
        self.rect = self.surf.get_rect(center = (WIDTH/2, HEIGHT - 10))

class Player(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__() 
        self.posx = 10
        self.posy = 420
        self.speed = 5
        self.width = 30
        self.height = 30
        self.update()

    def update(self):
        self.surf = pygame.Surface((self.width, self.height))
        self.surf.fill((128,255,40))
        self.rect = self.surf.get_rect(center = (self.posx, self.posy))

    def keyInput(self, keys):
      if keys[pygame.K_w] or keys[pygame.K_UP]:
         self.posy -= self.speed
      if keys[pygame.K_s] or keys[pygame.K_DOWN]:
          self.posy += self.speed
      if keys[pygame.K_d] or keys[pygame.K_RIGHT]:
          self.posx += self.speed
      if keys[pygame.K_a] or keys[pygame.K_LEFT]:
          self.posx -= self.speed
      self.update()

    def get_pos(self):
      return (self.posx, self.posy)

class GenericSprite(pygame.sprite.Sprite):
  def __init__(self, surf, rect):
      super().__init__()
      self.surf = surf
      self.rect = rect


def shortenLineSegment(a, b, c, d, length):
  short_x = a + (length * (c - a))
  short_y = b + (length * (d - b))
  return (short_x, short_y)

PT1 = platform()
P1 = Player()

all_sprites = pygame.sprite.Group()
all_sprites.add(PT1)
all_sprites.add(P1)

all_circles = []
 
while True:
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()

    displaysurface.fill((0,0,0))
    m_left, m_middle, m_right = pygame.mouse.get_pressed()

    if m_left:
      #circ = pygame.Surface((10,10))
      #circ.fill((0,255,0))
      #r = circ.get_rect(center = (pygame.mouse.get_pos()))
      #all_sprites.add(GenericSprite(circ, r))
      #circle_surface = pygame.draw.circle(surface=displaysurface, color=(0,0,255), radius=15, width=0, center=pygame.mouse.get_pos())
      all_circles.append(pygame.mouse.get_pos())

    circ = pygame.Surface((10,10))
    circ.fill((0,255,0))
    r = circ.get_rect(center = (pygame.mouse.get_pos()))
    
    keys = pygame.key.get_pressed()
    P1.keyInput(keys=keys)

    P1.update()
    for entity in all_sprites:
      displaysurface.blit(entity.surf, entity.rect)
    for circle in all_circles:
      pygame.draw.circle(displaysurface, (0,0,255), circle, 15, 0)
      p_pos = P1.get_pos()
      shorten_line = shortenLineSegment(circle[0], circle[1], p_pos[0], p_pos[1], 0.9)
      pygame.draw.line(displaysurface, (0,0,255), shorten_line, circle)

      floor_colilide = pygame.sprite.spritecollide()

    #displaysurface.blit(circ, r)
    pygame.display.update()
    FramePerSec.tick(FPS)