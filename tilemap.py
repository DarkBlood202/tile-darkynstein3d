import pygame as pg
from settings import *

class Map:
	def __init__(self,filename):
		self.data = []
		with open(filename,"rt") as f:
			for line in f:
				self.data.append(line.strip())

		self.tile_width = len(self.data[0])
		self.tile_height = len(self.data)
		self.width = self.tile_width*TILESIZE
		self.height = self.tile_height*TILESIZE

class Camera:
	def __init__(self,width,height):
		self.camera = pg.Rect(0,0,width,height)
		self.width = width
		self.height = height

	def apply_to(self,entity):
		return entity.rect.move(self.camera.topleft)

	def update(self,target):
		x = -target.rect.x + SCENE_W//2
		y = -target.rect.y + SCENE_H//2

		x = min(0,x)
		y = min(0,y)

		x = max(-(self.width - SCENE_W),x)
		y = max(-(self.height - SCENE_H),y)

		self.camera = pg.Rect(x,y,self.width,self.height)