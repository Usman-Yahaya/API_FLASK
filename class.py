class voiture: 
    def __init__(self,x,y):
        self.x = x 
        self.y = y

    def avancer(self):
        self.x += 1
    def reculer(self):
        self.x -= 1

voitture = voiture(3,4)
print(voitture)

        

class cour :
    def __init__(self,lieu,horaire):
        self.lieu = lieu
        self.horaire = horaire 
    def add_cour()