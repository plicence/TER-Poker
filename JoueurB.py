import Joueur


class JoueurB(Joueur.Joueur):
    
    
    def passer(self):
            return 0 
    
    def suivre(self, mise):
        if(mise <= self.solde):
            self.solde -= mise
            return mise
        else:
            return 0
    
    
    def jouer(self, mise):
        if(self.carte < 5 or mise >self.solde):
            return self.passer()
        else:
            return self.suivre(mise)
           
        
        