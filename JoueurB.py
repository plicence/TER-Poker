import Joueur


class JoueurB(Joueur.Joueur):
    
    def jouer(self):
        if(self.carte > 5):
            return 0
        else:
            self.solde -= 1
            return 1
           
        
        