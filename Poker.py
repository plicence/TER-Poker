import JoueurA
import JoueurB
import random



joueurA = JoueurA.JoueurA()
joueurB = JoueurB.JoueurB()

pot = joueurA.mise_depart() + joueurB.mise_depart()
carteA = random.randint(1, 10)
carteB = random.randint(1, 10)

joueurA.recevoir_carte(carteA)
joueurB.recevoir_carte(carteB)

actionA = joueurA.jouer()
actionB = joueurB.jouer()

if(actionA != "annule"):
    pot += actionA
    print("A:" + str(actionA) )

pot+= actionB
print("B:" + str(actionB))
 
if (carteA > carteB):
    joueurA.solde += pot
else:
    joueurB.solde += pot 


print(pot)
print("Solde A:" + str(joueurA.solde))
print("Solde B:" + str(joueurB.solde))