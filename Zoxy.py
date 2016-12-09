
from ggame import App, RectangleAsset, ImageAsset, Sprite, LineStyle, Color, Frame

SCREEN_WIDTH = 1280
SCREEN_HEIGHT = 940

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
        
    def movenorth(self,event):
        self.vy = -2
        
    def movesouth(self,event):
        self.vy = 2
    
    def moveeast(self,event):
        self.vx = 2
    
    def movewest(self,event):
        self.vx = -2
    
    def moveoff(self,event):
        self.vx = self.vy = 0
    
        

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
        Bingo((350, 900))
        
    def step(self):
        for ship in self.getSpritesbyClass(Bingo):
            ship.step()

myapp = Zoxy(SCREEN_WIDTH, SCREEN_HEIGHT)
myapp.run()
