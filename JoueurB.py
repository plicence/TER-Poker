import Joueur
import random

class JoueurB(Joueur.Joueur):
	def __init__(self):
		super(JoueurB, self).__init__()
		self.q_table=[
		[[0,0],[0,0],[0,0],[0,0],[0,0],[0,0],[0,0],[0,0],[0,0],[0,0]],
		[[0,0],[0,0],[0,0],[0,0],[0,0],[0,0],[0,0],[0,0],[0,0],[0,0]],
		[[0,0],[0,0],[0,0],[0,0],[0,0],[0,0],[0,0],[0,0],[0,0],[0,0]],
		[[0,0],[0,0],[0,0],[0,0],[0,0],[0,0],[0,0],[0,0],[0,0],[0,0]]]
		self.action=1
		self.gain=0
		self.epsilon=0.1
		self.gamma=0.85
		self.precision=100 #nombre de chiffres significatifs pour epsilon
		self.mise_tour=0
		self.last_mise=random.randint(0,3)
		self.last_action=random.randint(0,1)
		self.last_carte=random.randint(1,10)
	
	def passer(self):
			return 0 
    
	def suivre(self, mise):
		return mise
	
	def jouer(self, mise):
		self.mise_tour=mise
		if(self.action):
			return self.suivre(mise)
		else:
			return self.passer()	
			
	def get_indice_max(self, mise, carte):
		if(self.q_table[mise][carte][0]>self.q_table[mise][carte][1]):
			return 0
		else:
			return 1

	
	def choisir(self, mise):
		if(random.randint(0,self.precision)/self.precision<self.epsilon):
			self.action=random.randint(0,1)
		else:
			if(mise==4):
				mise=3;
			self.action=self.get_indice_max(mise,self.carte-1)
	
	def q_function(self):
		current_mise=self.mise_tour
		current_action=self.action
		current_carte=self.carte
		
		last_q_table=self.q_table[self.last_mise-1][self.last_carte-1][self.last_action]
		current_q_table=self.q_table[current_mise-1][current_carte-1][current_action]
		self.q_table[self.last_mise-1][self.last_carte-1][self.last_action]=last_q_table+self.epsilon*(self.gain+self.gamma*current_q_table-last_q_table)
		
		self.last_mise=current_mise
		self.last_action=current_action
		self.last_carte=current_carte
	
	def fin_tour(self, resultat):
		if(resultat==0):
			self.gain=-self.mise_tour
		elif(resultat==1):
			self.gain=self.mise_tour
			self.solde+=2*self.mise_tour
		else:
			self.gain=0
			self.solde+=self.mise_tour
		self.q_function();
	
	def affiche_table(self):
		for i in range(0,4):
			for i in range(0,10):
				print(self.q_table[i])