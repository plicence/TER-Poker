import JoueurA
import JoueurB
import Interface
import random
from time import time
import matplotlib.pyplot as plt
import numpy as np

import pygame # a supprimer
	
class Jeu:
	def __init__(self):
		self.joueurA=JoueurA.JoueurA()
		self.joueurB=JoueurB.JoueurB()
		random.seed(time())
		self.carteA = 0
		self.carteB = 0
		self.pot = 0
		self.listeA = []
		self.listeB = []
		self.countBluff = 0
		self.totalPlay = 0
		#aff=-1
		
	def reset_partie(self):
		self.joueurA.solde = 1000
		self.joueurB.solde = 1000
		self.carteA = 0
		self.carteB = 0
		self.pot = 0

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
			
	def jeu_simple_qlearning(self):
		"""Jeu qlearning sans interface graphique"""
		alpha = 0.0001
		gamma = 0.001
		epsilon = 0
	### Distribution des cartes ###
		acb = 2
		self.tirer()
		
	### A Joue ###
		ac = self.joueurA.takeAction(epsilon) #Le joueur A joue
		actionA = self.joueurA.ActionsVal(ac) # Le joueurA mise une somme(0, 1, 2, 4) par rapport à l'action effectuée
		#Ce nest pas action mais cest la mise
		if(actionA > 0): # S'il mise on ajoute au pot
			self.pot += actionA
    
		### B joue ###
			acb = self.joueurB.takeAction(epsilon, ac)
			miseB = self.joueurB.ActionsVal(acb, actionA)
			if(miseB == 0):### B Passe ###
				self.joueurA.ActualiserSolde(self.pot)
        
			else:### B suis ###
				self.pot += miseB
 
			### On retourne les cartes ###
				if (self.carteA > self.carteB):
					self.joueurA.ActualiserSolde(self.pot)
				elif (self.carteB > self.carteA):
					self.joueurB.ActualiserSolde(self.pot)
				else:
					self.joueurA.ActualiserSolde(actionA + 1)
					self.joueurB.ActualiserSolde(miseB + 1)
            
		else:
			miseB=0
			self.joueurB.ActualiserSolde(self.pot)
			
		"""print("Pot: " + str(self.pot))		print("Carte A : " + str(self.joueurA.carte))		print("Carte B : " + str(self.joueurB.carte))		print("Mise A : " + str(actionA)) print("Mise B : " + str(actionB))print("Solde A: " + str(self.joueurA.solde))print("Solde B: " + str(self.joueurB.solde))print(" ")"""
		
		###trucs de qlearning pour le joueur a###
		if(self.joueurA.carte <= 4 and ac >= 2):
			self.countBluff += 1 
		self.totalPlay += 1
		self.listeA.append(ac)
		self.listeB.append(acb)
		carteATour1 = self.joueurA.carte
		carteBTour1 = self.joueurB.carte

		recompenseA = self.joueurA.GetRecompense()
		recompenseB = self.joueurB.GetRecompense()

		#TOUR T+1: on définit quelle serait l'action suivante
		
		self.tirer_Sans_Mise()
		ac1 = self.joueurA.takeAction(0) #Le joueur A joue
		acb1 = self.joueurB.takeAction(0, self.joueurA.ActionsValFake(ac1)) #Le joueur B joue en fonction de la mise de A 
		
		#Q-Function
		self.joueurA.grid[carteATour1 - 1][ac] = self.joueurA.grid[carteATour1 - 1][ac] + alpha * (recompenseA + gamma * self.joueurA.grid[self.joueurA.carte - 1][ac1] - self.joueurA.grid[carteATour1 - 1][ac])
		#self.joueurA.grid[carteATour1 - 1][ac] = self.joueurA.grid[carteATour1 - 1][ac] + alpha * (recompenseA - self.joueurA.grid[carteATour1 - 1][ac])
		if (actionA > 0) :
			self.joueurB.grid[(carteBTour1 - 1) * 4 + ac][acb] = self.joueurB.grid[(carteBTour1 - 1) * 4 + ac][acb] + alpha * (recompenseB + gamma * self.joueurB.grid[(self.joueurB.carte - 1) * 4 +ac1][acb1] - self.joueurB.grid[(carteBTour1 - 1) * 4 + ac][acb]) 
			#self.joueurB.grid[(carteBTour1 - 1) * 4 + ac][acb] = self.joueurB.grid[(carteBTour1 - 1) * 4 + ac][acb] + alpha * (recompenseB - self.joueurB.grid[(carteBTour1 - 1) * 4 + ac][acb]) 

	def jeu_simple_boucle_qlearning(self, partie):
		""""L'affichage des résltats se fait hors de la fonction de jeu car il n'y a que le resultat final qui nous interesse"""
		iteration = 0
		while (self.joueurA.solde > 0 and self.joueurB.solde > 0) :
			self.jeu_simple_qlearning()
			#if((iteration%100) == 0):
				#self.joueurA.Analyse(partie, iteration)
			iteration += 1
		if(self.joueurA.solde <= 0):
			print("A perd à l'itération:"+ str(iteration))
			print("")
			return 0
		if(self.joueurB.solde <= 0):
			print("B perd à l'iteration:"+ str(iteration))
			print("")
			return 0
			#print("Solde A: " + str(self.joueurA.solde))
			#print("Solde B: " + str(self.joueurB.solde))
			
	def jeu_interface_qlearning(self):
		"""Jeu avec interface graphique"""
		#initialisation
		alpha = 0.0001
		gamma = 0.001
		epsilon = 0
		self.tirer()
		self.aff.charge_cartes()
		self.aff.place_cartes()
		acb = 2
		
		#Déroulement du tour
		ac = self.joueurA.takeAction(0.1) 
		miseA = self.joueurA.ActionsVal(ac)
		
		####Si Alice mise####
		if(miseA > 0): 
			self.pot += miseA
			print("A mise " + str(miseA) )
			acb = self.joueurB.takeAction(epsilon, ac)
			miseB = self.joueurB.ActionsVal(acb, miseA)
			
			####Si Bob passe####
			if(miseB == 0):
				print("B passe")
				self.joueurA.ActualiserSolde(self.pot)
			
			####Si Bob mise####
			else:        
				self.pot += miseB
				print("B suis")
 
				####Vérification des cartes####
				if (self.carteA > self.carteB):
					self.joueurA.ActualiserSolde(self.pot)
				elif (self.carteB > self.carteA):
					self.joueurB.solde += self.pot
				else:
					self.joueurA.ActualiserSolde(miseA + 1)
					self.joueurB.solde += (miseB + 1)    
        
		####Si A passe####
		else:
			print("Joueur A passe")
			self.joueurB.solde += self.pot #Si le joueur A passe, le joueur B gagne

		####Affichage du résultat####
		self.aff.retourne_cartes()
		print("Pot: " + str(self.pot))
		print("Solde A: " + str(self.joueurA.solde))
		print("Solde B: " + str(self.joueurB.solde))
		
		####Calculs pour le Qlearning####
		
		#Enregistrement des variables
		if(self.joueurA.carte <= 4 and ac >= 2):
			self.countBluff += 1 
		self.totalPlay += 1
		self.listeA.append(ac)
		self.listeB.append(acb)
		carteATour1 = self.joueurA.carte
		carteBTour1 = self.joueurB.carte
		recompenseB = self.joueurB.GetRecompense()
		recompenseA = self.joueurA.GetRecompense()
		
		#Simulation du tour suivant
		self.tirer_Sans_Mise()
		action_a_suiv = self.joueurA.takeAction(0) #Le joueur A joue
		action_b_suiv = self.joueurB.takeAction(0, self.joueurA.ActionsValFake(action_a_suiv))
		
		#Q-Function
		self.joueurA.grid[carteATour1 - 1][ac] = self.joueurA.grid[carteATour1 - 1][ac] + 0.001 * (recompenseA + 0.001 * self.joueurA.grid[self.joueurA.carte - 1][action_a_suiv] - self.joueurA.grid[carteATour1 - 1][ac])
		if (miseA > 0) :
			self.joueurB.grid[(carteBTour1 - 1) * 4 + ac][acb] = self.joueurB.grid[(carteBTour1 - 1) * 4 + ac][acb] + alpha * (recompenseB + gamma * self.joueurB.grid[(self.joueurB.carte - 1) * 4 +action_a_suiv][action_b_suiv] - self.joueurB.grid[(carteBTour1 - 1) * 4 + ac][acb]) 

	def jeu_interface_boucle_qlearning(self, n):
		"""jeu avec interface répété n fois sans réinitialisation des joueurs"""
		self.charge_interface()
		for i in range(0,n):
			self.jeu_interface_qlearning()
			if(self.joueurA.solde <= 0):
				print("A perd à l'itération:"+ str(i))
				break
			if(self.joueurA.solde <= 0):
				print("A perd à l'itération:"+ str(i))
				break
		pygame.quit()	
		
	def graphhistA(self):
		plt.title("Diagramme des actions de A")
		plt.hist(self.listeA, bins = 10,color = 'yellow', edgecolor = 'red')
		plt.xlabel('Action')
		plt.ylabel('Nombres')
		plt.xticks([0, 1, 2, 3], ["Passer", "Miser 1", "Miser 2", "Miser 3"])
		plt.savefig("ressources/Analyse/JoueurA")
		plt.show()
	
	def graphhistB(self):
		plt.title("Diagramme des actions de B")
		plt.hist(self.listeB, bins = 10,color = 'yellow', edgecolor = 'red')
		plt.xlabel('Action')
		plt.ylabel('Nombres')
		plt.xticks([2, 0, 1], ["A passe", "Passer", "Suivre"])
		plt.savefig("ressources/Analyse/JoueurB")
		plt.show()
		
	def graphlineA(self):
		plt.title("Diagramme des actions de A au cours du temps")
		plt.plot(self.listeA)
		plt.ylabel('Action')
		plt.yticks([0, 1, 2, 3], ["Passer", "Miser 1", "Miser 2", "Miser 3"])
		plt.savefig("ressources/Analyse/JoueurALigne")
		plt.show()	
		
		
			
def main():
	
	j=Jeu()
	j.joueurA.init_grille()
	j.joueurB.init_grille()
	for i in range (0, 3) : 
		print("Partie: " + str(i))
		j.jeu_interface_boucle_qlearning(5)
		j.reset_partie()
	
	j.joueurA.grid = np.around(j.joueurA.grid, 5)	
	j.joueurB.grid = np.around(j.joueurB.grid, 5)
	j.joueurA.ecrit_grille()
	j.joueurB.ecrit_grille()
	j.graphhistA()
	j.graphhistB()
	print("Bluff"+ str(j.countBluff)+ " sur " + str(j.totalPlay) )
	
	#j.graphlineA()
	
	
	
main()