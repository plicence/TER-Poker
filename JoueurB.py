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
		self.lire_table()
		self.affiche_table()
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
		self.solde-=mise
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
		if current_mise==4:
			current_mise=3
		current_action=self.action
		current_carte=self.carte
		
		last_q_table=self.q_table[self.last_mise][self.last_carte-1][self.last_action]
		current_q_table=self.q_table[current_mise][current_carte-1][current_action]
		self.q_table[self.last_mise][self.last_carte-1][self.last_action]=last_q_table+self.epsilon*(self.gain+self.gamma*current_q_table-last_q_table)
		
		self.last_mise=current_mise
		self.last_action=current_action
		self.last_carte=current_carte
	
	def fin_tour(self, pot, resultat):
		if(resultat==0):
			self.gain=-self.mise_tour
		elif(resultat==1):
			self.gain=self.mise_tour
			self.solde+=pot
		else:
			self.gain=0
			self.solde+=int(pot/2)
		self.q_function();
	
	def affiche_table(self):
		for i in range(0,4):
			for j in range(0,10):
				print(self.q_table[i][j])
			print(" ")
				
	def ecrire_table(self):
		fichier=open("ressources/table_bob.txt","w")
		for i in range(0,4):
			for j in range(0,10):
				for k in range(0,2):
					fichier.write(str(self.q_table[i][j][k]))
					fichier.write(" ")
		fichier.close()
		
	def lire_table(self):
		fichier=open("ressources/table_bob.txt","r")
		data=fichier.read()
		data=data.split()
		i=0
		j=0
		k=0
		for elem in data:
			self.q_table[i][j][k]=float(elem)
			i=(i+1)%4
			j=(j+1)%10
			k=(k+1)%2
		fichier.close()