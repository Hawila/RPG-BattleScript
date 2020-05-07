# blender build scripts
import random
from .skills import skill
class bcolors:
    HEADER = '\033[95m'
    OKBLUE = '\033[94m'
    OKGREEN = '\033[92m'
    WARNING = '\033[93m'
    FAIL = '\033[91m'
    ENDC = '\033[0m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'

class allColors:
    CEND = '\33[0m'
    CBOLD = '\33[1m'
    CITALIC = '\33[3m'
    CURL = '\33[4m'
    CBLINK = '\33[5m'
    CBLINK2 = '\33[6m'
    CSELECTED = '\33[7m'

    CBLACK = '\33[30m'
    CRED = '\33[31m'
    CGREEN = '\33[32m'
    CYELLOW = '\33[33m'
    CBLUE = '\33[34m'
    CVIOLET = '\33[35m'
    CBEIGE = '\33[36m'
    CWHITE = '\33[37m'

    CBLACKBG = '\33[40m'
    CREDBG = '\33[41m'
    CGREENBG = '\33[42m'
    CYELLOWBG = '\33[43m'
    CBLUEBG = '\33[44m'
    CVIOLETBG = '\33[45m'
    CBEIGEBG = '\33[46m'
    CWHITEBG = '\33[47m'

    CGREY = '\33[90m'
    CRED2 = '\33[91m'
    CGREEN2 = '\33[92m'
    CYELLOW2 = '\33[93m'
    CBLUE2 = '\33[94m'
    CVIOLET2 = '\33[95m'
    CBEIGE2 = '\33[96m'
    CWHITE2 = '\33[97m'

    CGREYBG = '\33[100m'
    CREDBG2 = '\33[101m'
    CGREENBG2 = '\33[102m'
    CYELLOWBG2 = '\33[103m'
    CBLUEBG2 = '\33[104m'
    CVIOLETBG2 = '\33[105m'
    CBEIGEBG2 = '\33[106m'
    CWHITEBG2 = '\33[107m'
'''
# passive of class types
mage -> Mana Recovery (passive) recovery mana after each level
warrior(warrior trained in the art of defensive techniques) -> defense Formation -> reduce all incoming damage by 25%
  
'''
class charClasses:
    """
    Main character class used to intilize character and enemies type (Mage,warrior,healer or archer)
    """
    def __init__(self,skills,HitPoints,manaPoints,attackPoints,defPoints,type,crticalHit):
        """
        Parameters
        -----
        list : skills
             cuurent class skills 
        int : HitPoints
             max health points
        int : manaPoints 
             max mana points
        int : attackPoints
             intial attack
        int : defPoints
             intial defense points
        str : type
             character class or type(mage.archer,etc)
        int : crticalHit
             crtical hit percent          
        """
        self.skills = skills
        self.maxhp = HitPoints
        self.currentHitPoints = HitPoints
        self.maxmp = manaPoints
        self.currentManaPoints = manaPoints
        self.lowattack = attackPoints
       # self.maxattackk = attackPoints + (random.randrange(50,100) * (attackPoints / 100) +  crticalHit)
        self.maxattackk = attackPoints + 20
        self.defpoints = defPoints
        self.type = type
        self.action = ["Action","sKills|Magic"]

    def generateRandomDamage(self):
        return random.randrange(self.lowattack,self.maxattackk)

    
    def takeDamage(self,dmg):
          self.currentHitPoints -= dmg  
          if self.currentHitPoints<0:
               self.currentHitPoints = 0
          return self.currentHitPoints
    
    def reduce_mana(self,cost):
         self.currentManaPoints -= cost 

    def get_hp(self):
         return self.currentHitPoints
    def getMaxHp(self):
         return self.maxhp 
    def get_cmana(self):
         return self.currentManaPoints     
    def getMaxMana(self): 
         return self.maxmp

  
    def Choice(self):
         i = 1
         print("Actions")
         for item in self.action:
              print(i,"-" +item)
              i += 1

    def choose_skill(self):
         i=1
         print("Skills")
         for skill in self.skills:
              print(str(i) + ":",skill.name,"Cost : ",skill.cost)
              i += 1 