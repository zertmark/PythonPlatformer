import pygame
import pyganim
from src.Animations import ANIMATION_MONSTER



class Monster(pygame.sprite.Sprite):
    HEIGHT = 32
    WIDTH = 32
    COLOR = "#2110FF"
    def __init__(self, x: int, y: int, v_left: int = 0, v_up: int = 0, max_length: int = 0, max_height: int = 0):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.Surface((self.WIDTH, self.HEIGHT))
        self.image.fill(pygame.Color(self.COLOR))
        self.image.set_colorkey(pygame.Color(self.COLOR))
        self.rect = pygame.Rect(x, y, self.WIDTH, self.HEIGHT)

        self.start_x = x
        self.start_y = y

        self.max_length = max_length
        self.max_height = max_height

        self.xvel = v_left
        self.yvel = v_up

        self.boltAnim = pyganim.PygAnimation(ANIMATION_MONSTER)
        self.boltAnim.play()

    def update(self, platforms:list):
        self.image.fill(pygame.Color(self.COLOR))
        self.boltAnim.blit(self.image, (0, 0))

        #self.rect.x += self.xvel
        #self.rect.y += self.yvel

        #self.collide(platforms)

        #if abs(self.start_x - self.rect.x) > self.max_length:
        #    self.xvel = -self.xvel

        #if abs(self.start_y - self.rect.y) > self.max_height:
        #    self.yvel = -self.yvel

    def collide(self, platforms:list):
        for p in platforms:
            if pygame.sprite.collide_rect(self, p) and self != p:
                self.xvel = -self.xvel
                self.yvel = -self.yvel
