# blender build scripts
import random
from Classes.skills import skill
from Classes.inventory import item
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
    def __init__(self,name,skills,HitPoints,manaPoints,attackPoints,defPoints,type,crticalHit,items):
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
        self.name = name
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
        self.items=items
        self.action = ["Normal Attack","sKills|Magic","Items"]

    def generateRandomDamage(self):
        return random.randrange(self.lowattack,self.maxattackk)

    
    def takeDamage(self,dmg):
          self.currentHitPoints -= dmg  
          if self.currentHitPoints<0:
               self.currentHitPoints = 0
          return self.currentHitPoints

    def addMana(self,value):
         self.currentManaPoints+=value
         if self.currentManaPoints > self.maxmp:
              self.currentManaPoints = self.maxmp

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

    def addattack(self,attp):
         self.lowattack += (attp/2)
         self.maxattackk+=attp 

    def heal(self,hp):
         self.currentHitPoints+=hp
         if self.currentHitPoints>self.maxhp:
              self.currentHitPoints = self.maxhp 
  
    def Choice(self):
         i = 1
         print(bcolors.OKGREEN+self.name+bcolors.ENDC)
         print(bcolors.OKGREEN +"Actions"+bcolors.ENDC)
         for item in self.action:
              print(i,"-" +item)
              i += 1

    def choose_skill(self):
         i=1
         print(bcolors.OKGREEN +"Skills"+bcolors.ENDC)
         for skill in self.skills:
              print(str(i) + "-",skill.name,"Cost : ",skill.cost)
              i += 1
    
    def choose_item(self):
         i=1
         print(bcolors.OKGREEN +"ITEMS"+bcolors.ENDC)
         for item in self.items:
              print(str(i)+ "-",item["item"].name,": ",item["item"].description,"(x" +str(item["quantity"])+")")
              i += 1
    def get_enemy_bar(self):
         health_bar = "" #initial hp bar
         bar_chunks = (self.currentHitPoints/self.maxhp) * 100 / 2
         while bar_chunks > 0:
              health_bar += "█"
              bar_chunks -= 1 
         while len(health_bar) < 50:  #length of hp bar below in print (-)counts
              health_bar += " "
         health_string =  str(self.currentHitPoints)+"/"+str(self.maxhp) # 4 digit + / + 4 digit = 9 
         hp=""
         if len(health_string) < 9:
              needed_space = 9 -len(health_string)

              while needed_space > 0:
                   hp += " "
                   needed_space -= 1
              hp += health_string     
         else:
              hp = health_string
         print("                     __________________________________________________ ")
         print(bcolors.BOLD+self.name+"     "+hp+bcolors.FAIL+"|" 
         +health_bar+"|"+bcolors.ENDC)           
    
    def get_stat_bar(self):
         health_bar = "" #initial hp bar
         bar_chunks = (self.currentHitPoints/self.maxhp) * 100 / 4 # he ASCII block elements come in chunks of 8
                                                                   
         mana_bar = ""
         mana_chunks = (self.currentHitPoints/self.maxhp) * 100 / 10

         while bar_chunks > 0:
              health_bar += "█"
              bar_chunks -= 1 

         while mana_chunks > 0:
              mana_bar += "█"
              mana_chunks -= 1

         while len(health_bar) < 25:  #length of hp bar below in print (-)counts
              health_bar += " " 

         while len(mana_bar) < 10:
              mana_bar += " " 

         health_string =  str(self.currentHitPoints)+"/"+str(self.maxhp) # 4 digit + / + 4 digit = 9 
         hp=""
         if len(health_string) < 9:
              needed_space = 9 -len(health_string)

              while needed_space > 0:
                   hp += " "
                   needed_space -= 1
              hp += health_string     
         else:
              hp = health_string

         mana_string =  str(self.currentManaPoints)+"/"+str(self.maxmp)
         mp=""
         if len(mana_string) < 7:
              needed_mspace = 7 -len(mana_string)

              while needed_mspace > 0:
                   mp += " "
                   needed_mspace -= 1
              mp += mana_string     
         else:
              mp = mana_string 

         print("                     _________________________             __________ ")
         print(bcolors.BOLD+self.name+"     "+bcolors.OKGREEN+hp+"|" 
         +health_bar+"|    "+bcolors.BOLD+mp+"|"+bcolors.OKBLUE+mana_bar+"|"+bcolors.ENDC)          
