import matplotlib.pyplot as plt
import Poker as p


class Graph:
	def __init__(self):
		self.Jeu = p.Jeu()
		self.WinA = 0
		self.WinB = 0

	def graphrond(self):
		plt.title("Nombres de manches gagnes par Joueur")
		self.Jeu.jeu_interface_boucle_qlearning(10000)
		plt.text(-1.5, 1, self.Jeu.winA+self.Jeu.winB+self.Jeu.equal )
		name = ['Win A', 'Win B', 'Equal']
		data = [self.Jeu.winA, self.Jeu.winB, self.Jeu.equal]
		plt.pie(data,labels=name, autopct='%1.1f%%', startangle=90)
		plt.axis('equal')
		plt.show()

	def graphhist(self):
		plt.title("Nombre de mises differentes du Joueur A")
		self.Jeu.jeu_interface_boucle_qlearning(10000)
		plt.hist(self.Jeu.list, bins = 4, color = 'yellow', edgecolor = 'red')
		plt.xlabel('Mise')
		plt.ylabel('Nombres')
		plt.show()


def main():
	g = Graph()
	g.graphrond()
	g.graphhist()

main()