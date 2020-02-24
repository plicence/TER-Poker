import matplotlib.pyplot as plt
import Poker as p


class Graph:
	def __init__(self):
		self.Jeu = p.Jeu()
		self.WinA = self.Jeu.winA
		print("hello",self.WinA)
		#self.WinB = self.Jeu.get_WinB()

	def graph(self):

		name = ['Win A', 'Win B']
		data = [self.WinA, self.WinB]

		plt.pie(data,labels=name, autopct='%1.1f%%', startangle=90, shadow=True)
		plt.axis('equal')
		plt.show()

def main():
	g=Graph()
	#g.recup()

main()