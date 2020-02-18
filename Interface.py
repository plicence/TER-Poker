import pygame
import random
from time import time

class Interface:
	def __init__(self, table):
		pygame.init()
		self.screen=pygame.display.set_mode((800,500))
		self.screen.fill((255,255,255))
		self.bg=self.back=pygame.image.load("ressources/table.png")
		self.carte_alice=Carte()
		self.carte_bob=Carte()
		self.table=table
		random.seed(time())

	def charge_cartes(self):
		"""choisit les sprites en fonction des valeurs piochées"""
		coul_alice=random.randint(0,3)
		coul_bob=random.randint(0,3)
		if(coul_bob==coul_alice):
			coul_bob=(coul_bob+random.randint(1,3))%4
		self.carte_alice.charge_image(self.table.carteA,coul_alice)
		self.carte_bob.charge_image(self.table.carteB,coul_bob)

	def place_cartes(self):
		"""animation des cartes sur la table"""
		self.x_alice=self.x_bob=350
		self.y_alice=0
		self.y_bob=440
		for i in range(1,70):
			self.y_alice+=2
			self.y_bob-=2
			self.screen.fill((255,255,255))
			self.screen.blit(self.bg,(97,60))
			self.screen.blit(self.carte_alice.back,(350,self.y_alice))
			self.screen.blit(self.carte_bob.back,(350,self.y_bob))
			pygame.display.flip()
			pygame.time.wait(10)
	
	def retourne_cartes(self):
		"""animation des cartes qui se retournent"""
		for i in range(1,15):
			tmp_back_alice=pygame.transform.scale(self.carte_alice.back,(30-2*i,50))
			tmp_back_bob=pygame.transform.scale(self.carte_bob.back,(30-2*i,50))
			self.screen.fill((255,255,255))
			self.screen.blit(self.bg,(97,60))
			self.screen.blit(tmp_back_alice,(350+i,self.y_alice))
			self.screen.blit(tmp_back_bob,(350+i,self.y_bob))
			pygame.display.flip()
			pygame.time.wait(10)
			
		for i in range(0,15):
			tmp_face_alice=pygame.transform.scale(self.carte_alice.face,(2*i,50))
			tmp_face_bob=pygame.transform.scale(self.carte_bob.face,(2*i,50))
			self.screen.fill((255,255,255))
			self.screen.blit(self.bg,(97,60))
			self.screen.blit(tmp_face_alice,(350-i,self.y_alice))
			self.screen.blit(tmp_face_bob,(350-i,self.y_bob))
			pygame.display.flip()
			pygame.time.wait(10)
			
		pygame.time.wait(1500)
	
class Carte:
	def __init__(self):
		self.back=pygame.image.load("ressources/back.png")
		self.back=pygame.transform.scale(self.back,(30,50))
		self.face=self.back
	
	def charge_image(self, val, coul):
		self.face=pygame.image.load("ressources/"+str(coul)+"/"+str(val)+".png")
		self.face=pygame.transform.scale(self.face,(30,50))