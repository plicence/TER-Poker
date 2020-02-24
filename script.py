import matplotlib.pyplot as plt
import Poker as p


class Graph:
	def __init__(self):
		self.Jeu = p.Jeu()
		self.WinA = 0
		self.WinB = 0

	def graph(self):

		self.Jeu.jeu_interface_boucle_qlearning(10000)
		plt.text(-1.5, 1, self.Jeu.winA+self.Jeu.winB+self.Jeu.equal )
		name = ['Win A', 'Win B', 'Equal']
		data = [self.Jeu.winA, self.Jeu.winB, self.Jeu.equal]
		plt.pie(data,labels=name, autopct='%1.1f%%', startangle=90)
		plt.axis('equal')
		plt.show()

def main():
	g=Graph()
	g.graph()

main()