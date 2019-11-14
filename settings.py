from os import path

TITLE = "Darkynstein3D"

TILESIZE = 16

HOR_TILES = 32
VER_TILES = 32

WIDTH = 1024
HEIGHT = 512

SCENE_W = WIDTH//2
SCENE_H = HEIGHT

FPS = 60

C_WHITE = (255,255,255)
C_DARKGREY = (40,40,40)
C_LIGHTGREY = (100,100,100)
C_BLACK = (0,0,0)

DATA_FOLDER = path.join(path.dirname(__file__),"data")
MAPS = path.join(DATA_FOLDER,"maps")

PLAYER_SPEED = 150