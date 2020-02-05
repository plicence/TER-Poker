import JoueurA
import JoueurB
import random
from time import time


joueurA = JoueurA.JoueurA()
joueurB = JoueurB.JoueurB()

pot = joueurA.mise_depart() + joueurB.mise_depart() # Les joueurs A et B font leurs mises de départ
random.seed(time())
carteA = random.randint(1, 10) #La carte du joueur A est tirée
random.seed(time())
carteB = random.randint(1, 10)#La carte du joueur B est tirée
print("carteA : " + str(carteA))
print("carteB : " + str(carteB))
joueurA.recevoir_carte(carteA) #Le joueur A reçoit sa carte
joueurB.recevoir_carte(carteB) #Le joueur B reçoit sa carte

actionA = joueurA.jouer() #Le joueur A joue

if(actionA > 0): # S'il mise on ajoute au pot
    
    pot += actionA
    print("A:" + str(actionA) )
    actionB = joueurB.jouer(actionA) # Le joueur B joue
    
    if(actionB == 0):
        joueurA.solde += pot # S'il passe le joueur A gagne 
        
    else: # S'il mise on vérifie qui a la plus grande valeur de carte
        
        pot += actionB
        print("B:" + str(actionB))
 
        if (carteA > carteB):
            joueurA.solde += pot #Le joueur A gagne
        elif (carteB > carteA):
            joueurB.solde += pot #Le joueur B gagne
        else: #Si les joueurs ont une égalité, chacun reprend son argent
            joueurA.solde += (actionA + 1)
            joueurB.solde += (actionB + 1)    
            
else:
    joueurB.solde += pot #Si le joueur A passe, le joueur B gagne




print("Pot: " + str(pot))
print("Solde A: " + str(joueurA.solde))
print("Solde B: " + str(joueurB.solde))

if (joueurA.solde == 0 or joueurB == 0):
    exit()
