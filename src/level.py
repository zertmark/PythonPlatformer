from functools import cache
import src.Platforms
from src.monster import Monster
FILE_DIR = "./levels/1.txt"
BG_DIR = "./levels/bg.jpg"


class Level:

    def __init__(self, path=FILE_DIR):
        self.pathLevel = path
        self.objects = {}
        self.platforms = []
        self.monsters = []
        self.types = {
            "-": src.Platforms.Platform,
            "*": src.Platforms.Spikes,
            "M": Monster
        }

    def loadObjects(self):
        countX: int = 0
        countY: int = 0 
        with open(self.pathLevel, 'r') as file:
            for y, row in enumerate(file.readlines()):
                countY = y
                for x, value in enumerate(row.strip()[:-1]):
                    countX = x
                    if value in list(self.types.keys())[:2]:
                        if str(self.types[value]) not in list(self.objects.keys()):
                            self.objects[str(self.types[value])]=[self.types[value](x*self.types[value].WIDTH, y*self.types[value].HEIGHT)]    
                        else:
                            self.objects[str(self.types[value])].append(self.types[value](x*self.types[value].WIDTH, y*self.types[value].HEIGHT))
            
        self.width  = (countX+1) * src.Platforms.Platform.WIDTH
        self.height = (countY+1) * src.Platforms.Platform.HEIGHT

    #def loadEntities(self):

        #for y, row in enumerate(self.objects):
        #    for x, value in enumerate(row):
                #if value in self.types.keys():
        #        if value in list(self.types.keys())[:2]:
        #            self.platforms.append(self.types[value](
        #                x*self.types[value].WIDTH, y*self.types[value].HEIGHT))
                #elif value == "*":
                #    self.platforms.append(src.Platforms.Spikes(
                #        x*src.Platforms.Platform.WIDTH, y*src.Platforms.Platform.HEIGHT))
                # TO:DO доделать создания монстра
        #        elif value == "M": 
        #            pass
    @cache
    def getEntities(self, Type:object) -> list:
        output=[]
        for lst in self.objects.values():
            for object in lst:
                if isinstance(object,Type):
                    print(f"{object} is a platform")
                    output.append(object)
        return output
        #return [object for object in self.objects if isinstance(object,Type)]
    def getPlatfroms(self) -> list:
        return self.getEntities(src.Platforms.Platform)
    
    def getPathLevel(self) -> str:
        return self.pathLevel
