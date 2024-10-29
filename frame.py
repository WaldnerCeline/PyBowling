from typing import List, Optional


class Frame:
    def __init__(self, frame_index: int):
        self.frame_index = frame_index
        self.lancer1 = None
        self.lancer2 = None
        self.score = 0
        self.isStrike = False
        self.isSpare = False

    def readLance1(self):
        valeur1 = int(input("Lancé 1 : "))
        while valeur1 < 0 or valeur1 > 10:
            print("Erreur sur le nombre de quilles, indiquez un nouveau nombre : ")
            valeur1 = int(input("Lancé 1 : "))
        self.lancer1 = valeur1
        return valeur1

    def readLance2(self):
        valeur2 = int(input("Lancé 2 : "))
        while valeur2 < 0 or valeur2 > 10 - self.lancer1:
            print("Erreur sur le nombre de quilles, indiquez un nouveau nombre : ")
            valeur2 = int(input("Lancé 2 : "))

        self.lancer2 = valeur2
        return valeur2
    
    def roll(self, only_one_lancer: bool = False):
        valeur1 = self.readLance1()
        if valeur1 == 10:
            self.isStrike = True
            self.lancer2 = 0
            self.calculate_score()
            return
        
        if only_one_lancer:
            self.lancer2 = 0
            self.calculate_score()
            return

        valeur2 = self.readLance2()
        if valeur1 + valeur2 == 10:
            self.isSpare = True

        self.calculate_score()
        #print("Frame " + str(self.frame_index) + " | Lancer 1 : " + str(self.lancer1) + " | Lancer 2 : " + str(self.lancer2))
        
        
    def calculate_score(self):
        self.score = self.lancer1 + self.lancer2

