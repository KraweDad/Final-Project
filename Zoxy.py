
from ggame import App, RectangleAsset, ImageAsset, Sprite, LineStyle, Color, Frame
import random
import time

SCREEN_WIDTH = 1280
SCREEN_HEIGHT = 940
#BINGOWASTHEPLAYER
class Bingo(Sprite):
    black = Color(0,1)
    skin = Color(0x003300, 1)
    line = LineStyle(0, black)
    asset = RectangleAsset(20,20, line, skin)
    
    def __init__(self,position):
        super().__init__(Bingo.asset, position)
        self.vy = 0
        self.vx = 0
        self.vr = 0
        self.fxcenter = self.fycenter = 0
        Zoxy.listenKeyEvent("keydown", "up arrow", self.movenorth)
        Zoxy.listenKeyEvent("keyup", "up arrow", self.moveoff)
        Zoxy.listenKeyEvent("keydown", "down arrow", self.movesouth)
        Zoxy.listenKeyEvent("keyup", "down arrow", self.moveoff)
        Zoxy.listenKeyEvent("keydown", "right arrow", self.moveeast)
        Zoxy.listenKeyEvent("keyup", "right arrow", self.moveoff)
        Zoxy.listenKeyEvent("keydown", "left arrow", self.movewest)
        Zoxy.listenKeyEvent("keyup", "left arrow", self.moveoff)
    
    def step(self):
        self.x += self.vx
        self.y += self.vy
    
    def movesouth(self,event):
        self.vy = 10
        
    def movenorth(self,event):
        self.vy = -10
        
    def moveeast(self,event):
        self.vx = 10
        
    def movewest(self,event):
        self.vx = -10
        
    def moveoff(self,event):
        self.vx = self.vy = 0
#PEOPLEBEPEOPLE
class People(Sprite):
    time.time()
    Human = True
    black = Color(0,1)
    skin = Color(0xfbc02d, 1)
    line = LineStyle(1, black)
    asset = RectangleAsset(20,20, line, skin)
    
    def __init__(self,position):
        super().__init__(People.asset, position)
        self.vy = 0
        self.vx = 0
        self.vr = 0
        self.fxcenter = self.fycenter = 0
        self.waituntil = time.time() + 1
        
    def step(self):
        thetime = time.time()
        self.x += self.vx
        self.y += self.vy
        Infection = self.collidingWithSprites(Bingo)
        if len(Infection) != 0:
            self.visible = False
        if thetime > self.waituntil:
            self.waituntil = thetime + .5
            Singularity = random.randrange(10000)
            if Singularity > 0 and Singularity <= 2500:
                self.vy = -2
            elif Singularity > 2500 and Singularity <= 5000:
                self.vy = 2
            elif Singularity > 5000 and Singularity <= 7500:
                self.vx = -2
            elif Singularity > 7500 and Singularity <= 10000:
                self.vx = 2
            else:
                pass
#ZAMBIESBEZAMBIES
class ZPeople(Sprite):
    black = Color(0,1)
    skin = Color(0x003300, 1)
    line = LineStyle(1, black)
    asset = RectangleAsset(20,20, line, skin)
    
    
    def __init__(self,position):
        super().__init__(ZPeople.asset, position)
        self.vy = 0
        self.vx = 0
        self.vr = 0
        self.fxcenter = self.fycenter = 0
        self.visible = False
        
    def step(self):
        self.x = People.x
        self.y = People.y
        Infection = self.collidingWithSprites(Bingo)
        if len(Infection) != 0:
            self.visible = True
#ZOXYGAMEISBESTZOXYGAME        
class Zoxy(App):
    def __init__(self, width, height):
        super().__init__(width, height)
        black = Color(1, 1)
        line = LineStyle(2, black)
        grass = Color(0x229954, 1)
        hedge = Color(0x145A32, 1)
        stone = Color(0xB2BABB, 1)
        road = Color(0x515A5A, 1)
        roof = Color(0xA04000, 1)
        Grass = RectangleAsset(1279,939,line,grass)
        Hedge = RectangleAsset(25,700,line,hedge)
        Hedge2 = RectangleAsset(25,340,line,hedge)
        Hedge3 = RectangleAsset(25,290,line,hedge)
        Hedge4 = RectangleAsset(485,25,line,hedge)
        Stone = RectangleAsset(20,50,line,stone)
        Road = RectangleAsset(60,940,line,road)
        Roof = RectangleAsset(300,400,line,roof)
        Sprite(Grass, (0,0))
        Sprite(Roof, (440,270))
        Sprite(Stone, (420,520))
        Sprite(Stone, (380,520))
        Sprite(Road, (310,0))
        Sprite(Hedge, (840,170))
        Sprite(Hedge2, (380, 170))
        Sprite(Hedge3, (380, 580))
        Sprite(Hedge4, (380, 845))
        Sprite(Hedge4, (380, 145))
        People((500, 500))
        People((600, 600))
        People((500, 600))
        People((600, 500))
        People((500, 500))
        People((600, 600))
        People((500, 600))
        People((600, 500))
        People((500, 500))
        People((600, 600))
        People((500, 600))
        People((600, 500))
        People((500, 500))
        People((600, 600))
        People((500, 600))
        People((600, 500))

        ZPeople((500, 500))
        ZPeople((600, 600))
        ZPeople((500, 600))
        ZPeople((600, 500))
        ZPeople((500, 500))
        ZPeople((600, 600))
        ZPeople((500, 600))
        ZPeople((600, 500))
        ZPeople((500, 500))
        ZPeople((600, 600))
        ZPeople((500, 600))
        ZPeople((600, 500))
        ZPeople((500, 500))
        ZPeople((600, 600))
        ZPeople((500, 600))
        ZPeople((600, 500))
        Bingo((0,0))
        
    def step(self):
        for ship in self.getSpritesbyClass(Bingo):
            ship.step()
        for hip in self.getSpritesbyClass(People):
            hip.step()
            if hip.x >= 1280:
                hip.x = 20
                hip.y = random.randrange(940)
            if hip.x <= 0:
                hip.x = 1260
                hip.y = random.randrange(940)
            if hip.y >= 940:
                hip.x = random.randrange(1280)
                hip.y = 20
            if hip.y <= 0:
                hip.x = random.randrange(1280)
                hip.y = 920
                

myapp = Zoxy(SCREEN_WIDTH, SCREEN_HEIGHT)
myapp.run()
