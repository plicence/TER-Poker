import JoueurA
import JoueurB
import Interface
import random
from time import time

import pygame # a supprimer
	
class Jeu:
	def __init__(self):
		self.joueurA=JoueurA.JoueurA()
		self.joueurB=JoueurB.JoueurB()
		random.seed(time())
		self.carteA=0
		self.carteB=0
		self.pot=0
		#aff=-1
		
	def charge_interface(self):
		"""initialise la fenetre"""
		#####Toujours appeler pygame.quit() avant la fin du programme si cette fonction est utilisée#####
		self.aff=Interface.Interface(self)
	
	def tirer(self):
		"""prends la mise de départ et distribue les cartes"""
		self.pot = self.joueurA.mise_depart() + self.joueurB.mise_depart() # Les joueurs A et B font leurs mises de départ		
		self.carteA = random.randint(1, 10) #La carte du joueur A est tirée
		self.carteB = random.randint(1, 10)#La carte du joueur B est tirée
		self.joueurA.recevoir_carte(self.carteA) #Le joueur A reçoit sa carte
		self.joueurB.recevoir_carte(self.carteB) #Le joueur B reçoit sa carte
	
	def tirer_Sans_Mise(self):
		"""prends la mise de départ et distribue les cartes"""	
		self.carteA = random.randint(1, 10) #La carte du joueur A est tirée
		self.carteB = random.randint(1, 10)#La carte du joueur B est tirée
		self.joueurA.recevoir_carte(self.carteA) #Le joueur A reçoit sa carte
		self.joueurB.recevoir_carte(self.carteB) #Le joueur B reçoit sa carte
	
	
	def jeu_simple(self):
		"""jeu avec affichage en console"""
		self.tirer()
		print("carteA : " + str(self.carteA))
		print("carteB : " + str(self.carteB))

		actionA = self.joueurA.jouer() #Le joueur A joue

		if(actionA > 0): # S'il mise on ajoute au pot
			self.pot += actionA
			print("A mise" + str(actionA) )
			actionB = self.joueurB.jouer(actionA) # Le joueur B joue
    
			if(actionB == 0):
				print("B passe")
				self.joueurA.solde += self.pot # S'il passe le joueur A gagne 
        
			else: # S'il mise on vérifie qui a la plus grande valeur de carte
        
				self.pot += actionB
				print("B mise" + str(actionB))
 
				if (self.carteA > self.carteB):
					self.joueurA.solde += self.pot #Le joueur A gagne
				elif (self.carteB > self.carteA):
					self.joueurB.solde += self.pot #Le joueur B gagne
				else: #Si les joueurs ont une égalité, chacun reprend son argent
					self.joueurA.solde += (actionA + 1)
					self.joueurB.solde += (actionB + 1)    
            
		else:
			self.joueurB.solde += self.pot #Si le joueur A passe, le joueur B gagne

		print("Pot: " + str(self.pot))
		print("Solde A: " + str(self.joueurA.solde))
		print("Solde B: " + str(self.joueurB.solde))
	
	def jeu_interface(self):
		"""Jeu avec interface graphique"""
		self.tirer()
		self.aff.charge_cartes()
		self.aff.place_cartes()
		actionA = self.joueurA.jouer() #Le joueur A joue

		if(actionA > 0): # S'il mise on ajoute au pot
			self.pot += actionA
			print("A mise" + str(actionA) )
			actionB = self.joueurB.jouer(actionA) # Le joueur B joue
    
			if(actionB == 0):
				print("B passe")
				self.joueurA.solde += self.pot # S'il passe le joueur A gagne 
        
			else: # S'il mise on vérifie qui a la plus grande valeur de carte
        
				self.pot += actionB
				print("B mise " + str(actionB))
 
				if (self.carteA > self.carteB):
					self.joueurA.solde += self.pot #Le joueur A gagne
				elif (self.carteB > self.carteA):
					self.joueurB.solde += self.pot #Le joueur B gagne
				else: #Si les joueurs ont une égalité, chacun reprend son argent
					self.joueurA.solde += (actionA + 1)
					self.joueurB.solde += (actionB + 1)    
            
		else:
			self.joueurB.solde += self.pot #Si le joueur A passe, le joueur B gagne

		print("Pot: " + str(self.pot))
		print("Solde A: " + str(self.joueurA.solde))
		print("Solde B: " + str(self.joueurB.solde))

		self.aff.retourne_cartes()
		
	def jeu_simple_boucle(self, n):
		"""jeu en console répété n fois sans réinitialisation des joueurs (les soldes sont conservés après chaque tour de boucle)"""
		for i in range(1,n):
			self.jeu_simple()
			
	def jeu_interface_boucle(self, n):
		"""jeu avec interface répété n fois sans réinitialisation des joueurs"""
		self.charge_interface()
		for i in range(1,n):
			self.jeu_interface()
		pygame.quit()
	
	def verif_solde(self):
		"""retourne 1 si A a perdu, 2 si b a perdu, 0 si les deux joueurs peuvent continuer"""
		if (self.joueurA.solde == 0):
			return 1
		elif(self.joueurB.solde == 0):
			return 2
		else:
			return 0
			
			
			
	def jeu_interface_qlearning(self):
		"""Jeu avec interface graphique"""
		self.tirer()
		#self.aff.charge_cartes()
		#self.aff.place_cartes()
		ac = self.joueurA.takeAction(0) #Le joueur A joue
		actionA = self.joueurA.ActionsVal(ac) # Le joueurA mise une somme(0, 1, 2, 4) par rapport à l'action effectuée
		if(actionA > 0): # S'il mise on ajoute au pot
			self.pot += actionA
			#print("A mise" + str(actionA) )
			actionB = self.joueurB.jouer(actionA) # Le joueur B joue
    
			if(actionB == 0):
				#print("B passe")
				self.joueurA.ActualiserSolde(self.pot) # S'il passe le joueur A gagne 
        
			else: # S'il mise on vérifie qui a la plus grande valeur de carte
        
				self.pot += actionB
				#print("B mise " + str(actionB))
 
				if (self.carteA > self.carteB):
					self.joueurA.ActualiserSolde(self.pot) #Le joueur A gagne
				elif (self.carteB > self.carteA):
					self.joueurB.solde += self.pot #Le joueur B gagne
				else: #Si les joueurs ont une égalité, chacun reprend son argent
					self.joueurA.ActualiserSolde(actionA + 1)
					self.joueurB.solde += (actionB + 1)    
            
		else:
			#print("Joueur A passe")
			self.joueurB.solde += self.pot #Si le joueur A passe, le joueur B gagne

		"""print("Pot: " + str(self.pot))
		print("Carte A : " + str(self.joueurA.carte))
		print("Carte B : " + str(self.joueurB.carte))
		print("Solde A: " + str(self.joueurA.solde))
		print("Solde B: " + str(self.joueurB.solde))"""
		
		carteATour1 = self.joueurA.carte
		carteBTour1 = self.joueurB.carte
		
		recompenseA = self.joueurA.GetRecompense()
		#self.aff.retourne_cartes()

		#TOUR T+1: on définit quelle serait l'action suivante
		
		self.tirer_Sans_Mise()
		ac1 = self.joueurA.takeAction(0) #Le joueur A joue
		
		#Q-Function
		self.joueurA.grid[carteATour1 - 1][ac] = self.joueurA.grid[carteATour1 - 1][ac] + 0.000085 * (recompenseA + 0.0001 * self.joueurA.grid[self.joueurA.carte - 1][ac1] - self.joueurA.grid[carteATour1 - 1][ac])
		
		#Affichage la QGrid
		
		"""for s in range(0, 10):
			print(self.joueurA.grid[s])"""
		
	def jeu_interface_boucle_qlearning(self, n):
		"""jeu avec interface répété n fois sans réinitialisation des joueurs"""
		#self.charge_interface()
		i = 0
		while(self.joueurA.solde > 0 and self.joueurB.solde >0):
			self.jeu_interface_qlearning()
			i = i +1
		if(self.joueurA.solde > 0):
			print("JoueurA gagne")
		print(i)
		return i
		"""if(self.joueurA.solde > 0):
			return 1
		else: 
			return 0"""
				
		
		#pygame.quit()
			
def main():
	res = 3001
	for i in range(0, 50):	#while(res > 3000):
		j=Jeu()
		res = j.jeu_interface_boucle_qlearning(10000)
		j.joueurA.ecrit_grille()
	#j.jeu_interface_boucle(5)
	print(str(res))
main()