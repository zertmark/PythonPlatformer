from src.Platforms import Platform, Spikes, BlockTeleport
from src.Animations import ANIMATION_JUMP_LEFT, ANIMATION_JUMP_RIGHT, ANIMATION_JUMP, ANIMATION_STAY, ANIMATION_LEFT, ANIMATION_RIGHT, ANIMATION_DELAY
from src.monster import Monster
from pygame.sprite import Sprite
from pygame.constants import K_RIGHT, K_UP, K_LEFT
import pyganim
import pygame
MOVE_SPEED = 5
WIDTH = 22
HEIGHT = 32
COLOR = "#000000"
JUMP_POWER = 8.5
GRAVITY = 0.3


class Player(Sprite):
    def __init__(self, x: int = 0, y: int = 0):
        Sprite.__init__(self)
        self.xvel = 0
        self.yvel = 0
        self.startX = x
        self.startY = y
        self.image = pygame.Surface((WIDTH, HEIGHT))
        self.image.fill(pygame.Color(COLOR))
        self.image.set_colorkey(pygame.Color(COLOR))
        self.rect = pygame.Rect(x, y, WIDTH, HEIGHT)
        self.left = False
        self.right = False
        self.up = False
        self.onGround = False
        self.keys = {
            K_LEFT: False,
            K_RIGHT: False,
            K_UP: False
        }
        self.animUPLeft = pyganim.PygAnimation(ANIMATION_JUMP_LEFT)
        self.animUPRight = pyganim.PygAnimation(ANIMATION_JUMP_RIGHT)
        self.animLeft = pyganim.PygAnimation(
            self.createAnimation(ANIMATION_LEFT))
        self.animRight = pyganim.PygAnimation(
            self.createAnimation(ANIMATION_RIGHT))
        self.animUp = pyganim.PygAnimation(ANIMATION_JUMP)
        self.animStay = pyganim.PygAnimation(ANIMATION_STAY)

        self.animStay.play()
        self.animStay.blit(self.image, (0, 0))
        self.animRight.play()
        self.animLeft.play()
        self.animUp.play()
        self.animUPLeft.play()
        self.animUPRight.play()

    def createAnimation(self, sprite_list):
        return [(animation, ANIMATION_DELAY) for animation in sprite_list]

    def move(self, platforms, sprites):
        if self.keys[K_UP]:
            if self.onGround:
                self.yvel = -JUMP_POWER
            self.image.fill(pygame.Color(COLOR))
            self.animUp.blit(self.image, (0, 0))

        if self.keys[K_LEFT]:
            self.xvel = -MOVE_SPEED
            self.image.fill(pygame.Color(COLOR))
            if self.keys[K_UP] and not self.onGround:
                self.animUPLeft.blit(self.image, (0, 0))
            else:
                self.animLeft.blit(self.image, (0, 0))

        if self.keys[K_RIGHT]:
            self.xvel = MOVE_SPEED
            self.image.fill(pygame.Color(COLOR))
            if self.keys[K_UP] and not self.onGround:
                self.animUPRight.blit(self.image, (0, 0))
            else:
                self.animRight.blit(self.image, (0, 0))

        if not (self.keys[K_LEFT] or self.keys[K_RIGHT]):
            self.xvel = 0
            if not self.keys[K_UP]:
                self.image.fill(pygame.Color(COLOR))
                self.animStay.blit(self.image, (0, 0))

        if not self.onGround:
            self.yvel += GRAVITY
            # if self.keys[K_LEFT]:
            #    self.image.fill(pygame.Color(COLOR))
            #    self.animUPLeft.blit(self.image, (0,0))
            # elif self.keys[K_RIGHT]:
            #    self.image.fill(pygame.Color(COLOR))
            #    self.animUPRight.blit(self.image, (0,0))

        self.onGround = False

        self.rect.y += self.yvel
        self.collide(0, self.yvel, platforms, sprites)

        self.rect.x += self.xvel
        self.collide(self.xvel, 0, platforms, sprites)

    def draw(self, screen):
        screen.blit(self.image, (self.rect.x, self.rect.y))

    def collide(self, xvel, yvel, platforms, sprites):
        for p in platforms:
            if pygame.sprite.collide_rect(self, p):
                if xvel > 0:
                    self.rect.right = p.rect.left

                if xvel < 0:
                    self.rect.left = p.rect.right

                if yvel > 0:
                    self.rect.bottom = p.rect.top
                    self.onGround = True
                    self.yvel = 0

                if yvel < 0:

                    self.rect.top = p.rect.bottom
                    if isinstance(p, Platform):
                        platforms.remove(p)
                        if sprites.has(p):
                            sprites.remove(p)

                    self.yvel = 0
                # TO:DO Rewrite this cringe
                if (isinstance(p, Spikes) and p in platforms) or isinstance(p, Monster):
                    self.die()

                elif isinstance(p, BlockTeleport):
                    self.teleport(p.dx, p.dy)

    def setKey(self, event):
        if event.key in self.keys.keys():
            if event.type == pygame.KEYDOWN:
                self.keys[event.key] = True
            elif event.type == pygame.KEYUP:
                self.keys[event.key] = False

    def die(self):
        self.teleport(-64, 0)

    def teleport(self, dx: int = 0, dy: int = 0):
        self.rect.x += dx
        self.rect.y += dy

    def getX(self) -> int:
        return self.rect.x

    def getY(self) -> int:
        return self.rect.y
