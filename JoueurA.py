import Joueur


class JoueurA(Joueur.Joueur):
    

    
    def jouer(self):
        if (self.carte > 10):
            return "annule"
        else :
            self.solde -= 5
            return 5
        
        