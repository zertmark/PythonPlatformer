import pygame
import pyganim
from Animations import ANIMATION_MONSTER
MONSTER_HEIGHT = 32
MONSTER_WIDTH = 32
MONSTER_COLOR = "#2110FF"




class Monster(pygame.sprite.Sprite):
    def __init__(self, x, y, v_left, v_up, max_length, max_height):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.Surface((MONSTER_WIDTH, MONSTER_HEIGHT))
        self.image.fill(pygame.Color(MONSTER_COLOR))
        self.image.set_colorkey(pygame.Color(MONSTER_COLOR))
        self.rect = pygame.Rect(x, y, MONSTER_WIDTH, MONSTER_HEIGHT)

        self.start_x = x
        self.start_y = y

        self.max_length = max_length
        self.max_height = max_height

        self.xvel = v_left
        self.yvel = v_up
        
        self.boltAnim = pyganim.PygAnimation(ANIMATION_MONSTER)
        self.boltAnim.play()

    def update(self, platforms):
        self.image.fill(pygame.Color(MONSTER_COLOR))
        self.boltAnim.blit(self.image, (0, 0))

        self.rect.x += self.xvel
        self.rect.y += self.yvel

        self.collide(platforms)

        if abs(self.start_x - self.rect.x) > self.max_length:
            self.xvel = -self.xvel

        if abs(self.start_y - self.rect.y) > self.max_height:
            self.yvel = -self.yvel

    def collide(self, platforms):
        for p in platforms:
            if pygame.sprite.collide_rect(self, p) and self != p:
                self.xvel = -self.xvel
                self.yvel = -self.yvel
