import Joueur
import random

class JoueurB(Joueur.Joueur):
	def __init__(self):
		super(JoueurB, self).__init__()
		self.q_table=[[0,0],[0,0],[0,0],[0,0]]
		self.action=1
		self.gain=0
		self.epsilon=0.1
		self.gamma=0.85
		self.precision=100 #nombre de chiffres significatifs pour epsilon
		self.mise_tour=0
	
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
			
	def get_indice_max(self, ligne):
		"""max=0
		for i in range(0,2):
			if(self.q_table[ligne][i]>self.q_table[ligne][max]):
				max=i
		return max"""
		if(self.q_table[ligne][0]>self.q_table[ligne][1]):
			return self.q_table[ligne][0]
		else:
			return self.q_table[ligne][1]
	
	def choisir(self, mise):
		if(random.randint(0,self.precision)/self.precision<self.epsilon):
			self.action=random.randint(0,1)
		else:
			self.action=self.get_indice_max(mise-1)
	
	def q_function(self):
		last_mise=self.mise_tour
		last_action=self.action
		suiv_mise=random.randint(0,3)
		suiv_action=random.randint(0,1)
		self.q_table[last_mise-1][last_action]=self.q_table[last_mise-1][last_action]+self.epsilon*(self.gain+self.gamma*self.q_table[suiv_mise-1][suiv_action]-self.q_table[last_mise-1][last_action])
	
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
			print(self.q_table[i])