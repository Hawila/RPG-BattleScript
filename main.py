from Classes.game import charClasses,allColors,bcolors
import  random

MageSpells = [{"name": "FireBall","cost":15,"Damage":45},
              {"name" : "LightningBolt","cost":25,"Damage":random.randrange(50,99)},
              {"name": "ThunderStorm","cost":50,"Damage":150}]

EnemySpells = [{"name": "Cursing","cost":15,"Damage":45},
              {"name" : "Torment","cost":25,"Damage":random.randrange(50,99)},
              {"name": "Jinx","cost":50,"Damage":150}]

Slime = charClasses(EnemySpells,150,90,60,10,"Slime",0)
Goblin = charClasses(EnemySpells,300,110,80,20,"Goblin",0)
Zombie = charClasses(EnemySpells,500,150,100,30,"Zombie",0)
Demon = charClasses(EnemySpells,750,190,110,40,"Demon Soul",0)
Cyclops = charClasses(EnemySpells,5000,500,130,90,"Boss-Cyclops",0)
Phoenix = charClasses(EnemySpells,3000,1000,150,120,"Boss-Phoenix",0)

Monsters = [Slime,Goblin,Zombie,Demon]
Bosses = [Cyclops,Phoenix]

Player = charClasses(MageSpells,360,80,90,30,"Mage",0)
Slime = charClasses(EnemySpells,150,90,60,10,"Slime",0)




one= True
while one:
    print("===================")
    Player.Choice()
    choice= input("Please Select:")
    index = int(choice)-1
    print("You Selected ",Player.action[int(choice)-1])
    if index == 0 :
        dmg= Player.generateRandomDamage()
        Slime.takeDamage(dmg)
        print("successful attack of ", dmg ,Slime.type, "HP",Slime.currentHitPoints)

    enemy_choice=1
    enemy_dmg = Slime.generateRandomDamage()
    Player.takeDamage(enemy_dmg)
    print(bcolors.FAIL + bcolors.BOLD +"Enemy Strike For:",enemy_dmg,"Your Hp is :",Player.get_hp(),bcolors.ENDC)


  