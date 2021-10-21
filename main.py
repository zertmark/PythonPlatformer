import pygame
from src.player import Player
from src.level import Level
from src.camera import X, Y, Title, Camera


class Main:
    SpritesGroup: object = None

    def __init__(self):
        pygame.init()

    def setTitle(self, new_title: str = ""):
        pygame.display.set_caption(new_title)

    def setDisplaySize(self, x: int = 0, y: int = 0):
        self.display = pygame.display.set_mode((x, y))

    def loadBackground(self, path_to_image: str = ""):
        self.background = pygame.image.load(path_to_image)

    def addObjectsToSpriteGroup(self, entities: list, group: object):
        for entity in entities:
            group.add(entity)

    def startLevel(self):
        self.Level = Level()
        self.Level.loadObjects()
        self.SpritesGroup = pygame.sprite.Group()
        self.addObjectsToSpriteGroup(
            self.Level.getPlatfroms(), self.SpritesGroup)
        self.addObjectsToSpriteGroup(self.Level.getMonsters(), self.SpritesGroup)

        self.Player = Player(55, 55)
        self.SpritesGroup.add(self.Player)
        self.Clock = pygame.time.Clock()
        self.Camera = Camera(self.Level.width, self.Level.height)
    def loop(self):
        #mn = monster.Monster(120, 200, 2, 3, 150, 15)

        while True:

            self.Clock.tick(60)
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    print("Exiting game...")
                    exit()

                if event.type == pygame.KEYUP or event.type == pygame.KEYDOWN:
                    self.Player.setKey(event)

            self.display.blit(self.background, (0, 0))
            self.Player.move(self.Level.getPlatfroms(), self.SpritesGroup)
            self.addObjectsToSpriteGroup(
                self.Level.getPlatfroms(), self.SpritesGroup)
            # mn.update(self.Level.getPlatfroms())

            self.Camera.update(self.Player)
            for ent in self.SpritesGroup:
                self.display.blit(
                    ent.image, self.Camera.applyCorrdinatesToObject(ent))
                ent.update(self.Level.getPlatfroms())
                

            pygame.display.update()


if __name__ == "__main__":
    main = Main()
    main.setTitle(Title)
    main.setDisplaySize(X, Y)
    main.loadBackground("./levels/bg.jpg")
    main.startLevel()
    main.loop()
