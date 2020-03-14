


class Joueur:
     
    
    
    def __init__(self):
        self.solde = 1000
        self.carte = 1
        
    def mise_depart(self):
        self.ancien_solde= self.solde
        self.solde -= 1
        return 1
    
    def recevoir_carte(self, carte):
        self.cartePrecedente = self.carte
        self.carte = carte

        
        
        

    