import pygame as pg
import sys
from os import path
from settings import *
from entities import *
from tilemap import *

class Game:
	def __init__(self):
		pg.init()
		pg.display.set_caption(TITLE)
		self.screen = pg.display.set_mode((WIDTH,HEIGHT))
		self.clock = pg.time.Clock()

	def load_map(self):
		self.map = Map(path.join(MAPS,"map.txt"))

	def new_game(self):
		self.all_sprites = pg.sprite.Group()
		self.walls = pg.sprite.Group()

		self.load_map()

		for row,tiles in enumerate(self.map.data):
			for col,tile in enumerate(tiles):
				if tile == "1":
					Wall(self,col,row)
				elif tile == "P":
					self.player = Player(self,col,row)

		self.camera = Camera(self.map.width,self.map.height)

		print("Map dimensions: ", self.map.width, self.map.height)
		print("Map tile dimensions: ", self.map.tile_width, self.map.tile_height)

		print("Camera dimensions", self.camera.width, self.camera.height)

	def run(self):
		self.playing = True
		while self.playing:
			self.dt = self.clock.tick(FPS)/1000
			self.events()
			self.update()
			self.draw()

	def quit(self):
		pg.quit()
		sys.exit()

	def update(self):
		self.all_sprites.update()
		self.camera.update(self.player)

	def draw_grid(self):
		for x in range(0,SCENE_W,TILESIZE):
			pg.draw.line(self.screen,C_LIGHTGREY,(x,0),(x,SCENE_H))
		for y in range(0,SCENE_H,TILESIZE):
			pg.draw.line(self.screen,C_LIGHTGREY,(0,y),(SCENE_W,y))

	def draw(self):
		self.screen.fill(C_BLACK)
		self.draw_grid()

		for sprite in self.all_sprites:
			if self.camera.apply_to(sprite).right <= SCENE_W:
				self.screen.blit(sprite.image,self.camera.apply_to(sprite))

		pg.display.flip()

	def events(self):
		for ev in pg.event.get():
			if ev.type == pg.QUIT:
				self.quit()

if __name__ == "__main__":
	g = Game()
	while True:
		g.new_game()
		g.run()