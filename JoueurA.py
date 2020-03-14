import Joueur
from enum import Enum
import random
from random import randint
import numpy as np

class JoueurA(Joueur.Joueur):
    
    
    grid = [
        [1,0,0,0],
        [0,0,0,0],
        [0,0,0,0],
        [0,0,0,0],
        [0,0,0,0],
        [0,0,0,0],
        [0,0,0,0],
        [0,0,0,0],
        [0,0,0,0],
        [0,0,0,0]  
    ]
    
    Action = Enum('Action', 'Passer Miser1 Miser2 Miser4')
    
    
    def init_grille(self):
        with open("ressources/grilleA.txt", "r") as f:
            lignes = f.readlines()
            for i in range(0, 10):
                lignes[i] = list(map(float, lignes[i][:-1].split(",")))
                #print(lignes[i])
                self.grid[i] =  lignes[i]
                
            
                    
    def ecrit_grille(self):
        with open("ressources/grilleA.txt", "w") as f:
            for i in range(0, 10):
                for j in range(0, 4):
                    if(j <3):
                        f.write(str(self.grid[i][j])+",")
                    else:
                        f.write(str(self.grid[i][j]))    
                f.write("\n")
    def __init__(self):
        super(JoueurA, self).__init__()
        self.init_grille()  
        
            
    def miser1(self):
        if(self.solde - 1 > 0):
            self.solde -= 1
            return 1
        else:
            return 0
    
    def miser2(self):
        if(self.solde - 2 > 0):
            self.solde -= 2
            return 2
        else:
            return 0
    
    def miser4(self):
        if(self.solde - 4 > 0):
            self.solde -= 4
            return 4
        else:
            return 0
    
    def passer(self):
        return 0
    
    def jouer(self):
        if (self.carte == 1):
            return self.passer()
        elif (self.carte >= 2 and self.carte <= 3 ) :
            return self.miser1()
        elif (self.carte >= 4 and self.carte <= 6 ) :
            return self.miser2()
        elif (self.carte >= 7 and self.carte <= 10 ) :
            return self.miser4()
    
      
        
        
    def takeAction(self, epsilon): #Choisit l'action à effectuer
        np.matrix(self.grid)
        if (random.uniform(0, 1) < epsilon):
            action = randint(0, 3)
        else:
            action = np.argmax(self.grid[self.carte-1])   
        return action
        
        
    def ActionsVal(self, action): #retourne l'argent à jouer selon l'action prise
        val = None
        if (action == 0):
            return self.passer()
        elif (action == 1):
            return self.miser1()
        elif (action == 2):
            return self.miser2()
        elif (action == 3):
            return self.miser4()     
        return val

    def ActionsValFake(self, action): #retourne l'argent à jouer selon l'action prise
        val = None
        if (action == 0):
            return 0
        elif (action == 1):
            return 1
        elif (action == 2):
            return 2
        elif (action == 3):
            return 3     
        return val    
    
    def ActualiserSolde(self, Gain):#actualise le solde du joueur A
        self.solde += Gain
        
    def GetRecompense(self): #calcul le gain effectif après jeu
        return self.solde - self.ancien_solde   
        
        
                 
        
        
        