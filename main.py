from Classes.game import charClasses,allColors,bcolors
import  random

MageSpells = [{"name": "FireBall","cost":15,"Damage":45},
              {"name" : "LightningBolt","cost":25,"Damage":random.randrange(50,99)},
              {"name": "ThunderStorm","cost":50,"Damage":150}]

Player = charClasses(MageSpells,360,80,90,30,"Mage",0)


