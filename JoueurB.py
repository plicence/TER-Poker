import Joueur
from enum import Enum
import random
from random import randint
import numpy as np

class JoueurB(Joueur.Joueur):
    

    grid = [
        [1,0],
        [0,0],
        [0,0],
        [0,0],
        [0,0],
        [0,0],
        [0,0],
        [0,0],
        [0,0],
        [0,0],
        [0,0],
        [0,0],
        [0,0],
        [0,0],
        [0,0],
        [0,0],
        [0,0],
        [0,0],
        [0,0],
        [0,0],
        [0,0],
        [0,0],
        [0,0],
        [0,0],
        [0,0],
        [0,0],
        [0,0],
        [0,0],
        [0,0],
        [0,0],
        [0,0],
        [0,0],
        [0,0],
        [0,0],
        [0,0],
        [0,0],
        [0,0],
        [0,0],
        [0,0],
        [0,0],
    ]
    
    Action = Enum('Action', 'Passer Suivre')
    
    Ancien_Solde = None
    
    
    def init_grille(self):
        with open("ressources/grilleB.txt", "r") as f:
            lignes = f.readlines()
            for i in range(0, 39):
                lignes[i] = list(map(float, lignes[i][:-1].split(",")))
                print(lignes[i])
                self.grid[i] =  lignes[i]
                
            
                    
    def ecrit_grille(self):
        with open("ressources/grilleB.txt", "w") as f:
            for i in range(0, 40):
                for j in range(0, 2):
                    if(j < 2):
                        f.write(str(self.grid[i][j])+",")
                    else:
                        f.write(str(self.grid[i][j]))    
                f.write("\n")
    def __init__(self):
        super(JoueurB, self).__init__()
        self.init_grille()  
        
            
    def suivre(self, miseA):
        if(self.solde - miseA > 0):
            self.solde -= miseA
            return miseA
        else:
            return 0
    
    
    def passer(self):
        return 0
        
    def takeAction(self, epsilon, actionA): #Choisit l'action à effectuer
        np.matrix(self.grid)
        if (random.uniform(0, 1) < epsilon):
            action = randint(0, 1)
        else:
            indice = (self.carte - 1) * 4 + actionA
            action = np.argmax(self.grid[indice])   
        return action
        
        
    def ActionsVal(self, action, miseA): #retourne l'argent à jouer selon l'action prise
        val = None
        self.Ancien_Solde = self.solde
        if (action == 0):
            return self.passer()
        elif (action == 1):
            return self.suivre(miseA)
        return val
    
    def ActualiserSolde(self, Gain):#actualise le solde du joueur B
        self.solde += Gain
        
    def GetRecompense(self): #calcul le gain effectif après jeu
        print(self.solde)
        print(self.Ancien_Solde)
        return self.solde - self.Ancien_Solde    
        
        
                 
        
        
        