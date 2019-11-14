import pygame as pg
from settings import *

class Wall(pg.sprite.Sprite):
	def __init__(self,game,x,y):
		self.groups = game.all_sprites, game.walls

		pg.sprite.Sprite.__init__(self,self.groups)

		self.game = game

		self.image = pg.Surface((TILESIZE,TILESIZE))
		self.image.fill(C_WHITE)
		self.rect = self.image.get_rect()

		self.x = x
		self.y = y

		self.rect.x = x*TILESIZE
		self.rect.y = y*TILESIZE

class Player(pg.sprite.Sprite):
	def __init__(self,game,x,y):
		self.groups = game.all_sprites
		pg.sprite.Sprite.__init__(self,self.groups)
		self.game = game
		self.image = pg.Surface((TILESIZE,TILESIZE))
		self.image.fill(C_WHITE)
		self.rect = self.image.get_rect()
		self.vx, self.vy = 0, 0
		self.x = x*TILESIZE
		self.y = y*TILESIZE

	def get_keys(self):
		self.vx, self.vy = 0, 0
		keys = pg.key.get_pressed()
		if keys[pg.K_LEFT]:
			self.vx = -PLAYER_SPEED
		if keys[pg.K_RIGHT]:
			self.vx = PLAYER_SPEED
		if keys[pg.K_UP]:
			self.vy = -PLAYER_SPEED
		if keys[pg.K_DOWN]:
			self.vy = PLAYER_SPEED

	def update(self):
		self.get_keys()
		self.x += self.vx*self.game.dt
		self.y += self.vy*self.game.dt
		self.rect.x = self.x
		self.rect.y = self.y