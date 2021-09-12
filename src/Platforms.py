import pygame
import pyganim


class Platform(pygame.sprite.Sprite):
    WIDTH = 32
    HEIGHT = 32
    PLATFORM_COLOR = "#006262"

    def __init__(self, x: int = 0, y: int = 0):
        super().__init__()
        self.image = pygame.Surface(
            (self.WIDTH, self.HEIGHT))
        self.image = pygame.image.load("levels/platform.png")
        self.rect = pygame.Rect(
            x, y, self.WIDTH, self.HEIGHT)

    def getX(self) -> int:
        return self.rect.x

    def getY(self) -> int:
        return self.rect.y


class Spikes(Platform):
    def __init__(self, x: int, y: int):
        super().__init__(x=x, y=y)
        self.image = pygame.image.load("levels/dieBlock.png")


class BlockTeleport(Platform):

    def __init__(self, x: int, y: int, dx: int, dy: int):
        from Animations import ANIMATION_BLOCK_TELEPORT
        super().__init__(x, y)
        self.dx = dx
        self.dy = dy

        self.image.set_colorkey(pygame.Color("#7686FF"))
        self.boltAnim = pyganim.PygAnimation(ANIMATION_BLOCK_TELEPORT)
        self.boltAnim.play()

    def update(self):
        self.image.fill(pygame.Color("#7686FF"))
        self.boltAnim.blit(self.image, (0, 0))
