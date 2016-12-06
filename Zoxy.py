
from ggame import App, RectangleAsset, ImageAsset, Sprite, LineStyle, Color, Frame

SCREEN_WIDTH = 1280
SCREEN_HEIGHT = 940

class Platformer(App):
    def __init__(self, width, height):
        super().__init__(width, height)
        black = Color(1, 1)
        line = LineStyle(3, black)
        grass = Color(0x229954, 1)
        hedge = Color(0x145A32, 1)
        stone = Color(0xB2BABB, 1)
        road = Color(0x515A5A, 1)
        roof = Color(0xA04000, 1)
        Grass = RectangleAsset(1279,939,line,grass)
        Hedge = RectangleAsset(25,700,line,hedge)
        Stone = RectangleAsset(50,20,line,stone)
        Road = RectangleAsset(60,940,line,road)
        Roof = RectangleAsset(300,400,line,roof)
        Sprite(Grass, (0,0))
        Sprite(Roof, (440,270))
        Sprite(Stone, (480,690))
        Sprite(Stone, (480,740))
        Sprite(Road, (320,0))
        Sprite(Hedge, (1000,500))
        

myapp = Platformer(SCREEN_WIDTH, SCREEN_HEIGHT)
myapp.run()
