import Platforms
FILE_DIR = "./levels/1.txt"
BG_DIR = "./levels/bg.jpg"


class Level:

    def __init__(self, path=FILE_DIR):
        self.pathLevel = path
        self.objects=[]
        self.platforms=[]
        self.monsters=[]

    def loadObjects(self):
        with open (self.pathLevel, 'r') as file:
            for line in file.readlines():
                self.objects.append(line.strip()[:-1])
        
        self.width = len(self.objects[0]) * Platforms.Platform.PLATFORM_WIDTH
        self.height= len(self.objects) * Platforms.Platform.PLATFORM_HEIGHT

    def loadPlatforms(self):
        for y, row in enumerate(self.objects):
            for x, value in enumerate(row):
                if value == "-":
                    self.platforms.append(Platforms.Platform(x*Platforms.Platform.PLATFORM_WIDTH,y*Platforms.Platform.PLATFORM_HEIGHT))
                elif value == "*":
                    self.platforms.append(Platforms.Spikes(x*Platforms.Platform.PLATFORM_WIDTH,y*Platforms.Platform.PLATFORM_HEIGHT))
                #TO:DO доделать создания монстра  
                elif value == "M":
                    pass
                
    def getPlatfroms(self) -> list:
        return self.platforms

    def getPathLevel(self) -> str:
        return self.pathLevel