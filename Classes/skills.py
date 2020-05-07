import random

class skill:
    def __init__(self,name,cost,damage,type):
        self.name = name
        self.cost = cost
        self.damage = damage
        self.type = type
        

   
    def generateRandomDamage(self):
        return random.randrange(self.damage-10,self.damage+10)
             