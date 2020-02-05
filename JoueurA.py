import Joueur


class JoueurA(Joueur.Joueur):
    

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
    
        
        