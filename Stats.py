#import Poker
import matplotlib.pyplot as pyplot

class table:
	def __init__(self):
		self.carte_alice=list()
		self.carte_bob=list()
		self.action_alice=list()
		self.action_bob=list()
		self.resultat=list()
		self.nb_tours=0
		self.nb_bluff=0
	
	def update(self, j, action_a, action_b, res):
		self.nb_tours+=1
		self.carte_alice.append(j.joueurA.carte)
		self.carte_alice.append(j.joueurA.carte)
		
		if action_a==0:
			action_b=-1
		self.action_alice.append(action_a)
		self.action_bob.append(action_b)
		self.resultat.append(res)
	
	def fin_partie(self, bluff):
		self.nb_bluff=bluff

class tables:
	def __init__(self,n):
		self.nb_parties=n
		self.parties=list()
		self.nb_tours=list()
		self.current_table=table()
		self.bluff=list()
		self.cadrage=list()
		self.current=0
		
		self.init_cadrage()
		
	def update(self, j, action_a, action_b, res):
		self.current_table.update(j, action_a, action_b, res)
		
	def fin_partie(self, bluff):
		self.current_table.fin_partie(bluff)
		self.parties.append(self.current_table)
		self.current_table=table()
	
	def liste_simple(self, liste):
		"""Transforme une liste de listes en liste simple"""
		res=liste
		while len(res)>1:
			tmp=res[0]
			del res[0]
			res[0]=tmp+res[0]
		return res[0]
		
	def init_cadrage(self):
		for i in range(0,self.nb_parties):
			self.cadrage.append(i)
	
	def calcul_nb_tours(self):
		for i in range(0,self.nb_parties):
			self.nb_tours.append(self.parties[i].nb_tours)
	
	def calcul_bluff(self):
		for i in range(0,self.nb_parties):
			self.bluff.append(float(self.parties[i].nb_bluff)/float(self.parties[i].nb_tours))
	
	def show_nb_tours(self):
		self.calcul_nb_tours()
		pyplot.scatter(self.cadrage, self.nb_tours)
		pyplot.title("Tours nécessaires à l'élimination de Alice")
		pyplot.xlabel('Parties jouées')
		pyplot.ylabel('Nombre de tours')
		pyplot.xticks([0, self.nb_parties/2, self.nb_parties])
		pyplot.savefig("ressources/stats/durée_jeu.png")
		pyplot.show()
	
	def show_nb_bluffs(self):
		self.calcul_bluff()
		pyplot.plot(self.bluff)
		pyplot.title("Evolution du nombre de bluffs")
		pyplot.xlabel('Parties jouées')
		pyplot.ylabel('Nombre de bluffs')
		pyplot.xticks([0, self.nb_parties/2, self.nb_parties])
		pyplot.savefig("ressources/stats/nombre_bluffs.png")
		pyplot.show()
		
	def show_actions_alice(self, i):
		pyplot.hist(self.parties[i].action_alice)
		pyplot.title("Actions de Alice")
		pyplot.xlabel('Action')
		pyplot.ylabel('Nombres')
		pyplot.xticks([0, 1, 2, 3], ["Passer", "Miser 1", "Miser 2", "Miser 3"])
		pyplot.savefig("ressources/stats/alice_"+str(i+1)+".png")
		pyplot.show()
		
	def show_actions_bob(self, i):
		pyplot.hist(self.parties[i].action_bob)
		pyplot.title("Actions de Bob")
		pyplot.xlabel('Action')
		pyplot.ylabel('Nombres')
		pyplot.xticks([0, 1, 2], ["Alice Passe", "Passer", "Suivre"])
		pyplot.savefig("ressources/stats/bob_"+str(i+1)+".png")
		pyplot.show()
			
def main():
	t=table()
	t.update(Poker.Jeu(),1,1,1)
	print("ok")
