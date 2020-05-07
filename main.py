from Classes.game import charClasses,allColors,bcolors
from Classes.skills import skill
import  random
# Mage Skills 
Fireball = skill("FireBall",15,45,"spell")
LightningBolt = skill("LightningBolt",25,random.randrange(50,90),"spell")
ThunderStorm = skill("ThunderStorm",50,150,"spell")
#Healer Skill
cure = skill("cure",20,70,"spell")
cura = skill("cura",50,120,"spell")
Divine = skill("Divine",100,250,"spell")
#Enemy Skill
Cursing = skill("Cursing",15,45,"spell")
Torment = skill("Torment",2,90,"spell")
Jinx = skill("Jinx",50,150,"spell")

MageSpells = [Fireball,LightningBolt,ThunderStorm]
HealerSpell = [cure,cura,Divine]
EnemySpells = [Cursing,Torment,Jinx]

Slime = charClasses(EnemySpells,150,90,40,10,"Slime",0)
Goblin = charClasses(EnemySpells,300,110,60,20,"Goblin",0)
Zombie = charClasses(EnemySpells,500,150,80,30,"Zombie",0)
Demon = charClasses(EnemySpells,750,190,110,40,"Demon Soul",0)
Cyclops = charClasses(EnemySpells,5000,500,130,90,"Boss-Cyclops",0)
Phoenix = charClasses(EnemySpells,3000,1000,150,120,"Boss-Phoenix",0)

Monsters = [Slime,Goblin,Zombie,Demon]
Bosses = [Cyclops,Phoenix]

Player = charClasses(MageSpells,360,80,90,30,"Mage",0)





one= True
while one:
    print("===================")
    Player.Choice()
    choice= input("Please Select:")
    index = int(choice)-1
    print("You Selected ",Player.action[int(choice)-1])

    if index == 0:
        dmg= Player.generateRandomDamage()
        Zombie.takeDamage(dmg)
        print("successful attack of ", dmg ,Zombie.type, "HP",Zombie.currentHitPoints)  
    elif index == 1:
        Player.choose_skill()
        skill_choose = input("Choose Skill:")
        skill_index = int(skill_choose)-1
        if skill_index > 2 :
            print(bcolors.FAIL + bcolors.BOLD+"Invaild Choice"+bcolors.ENDC)
            continue

        Player_mana = Player.get_cmana()
        if Player.skills[skill_index].cost > Player_mana:
            print(bcolors.FAIL + bcolors.BOLD +"You Dont Have Mana"+bcolors.ENDC)
            continue

        Player.reduce_mana(Player.skills[skill_index].cost)
        magic_dmg = Player.skills[skill_index].generateRandomDamage()
        Zombie.takeDamage(magic_dmg)
        print("You Delt",magic_dmg," Damage To",Zombie.type,"with",Player.skills[int(choice)-1].name,"And it cost: ",Player.skills[skill_index].cost,"Your Current Mana: ",Player.get_cmana())

    
    enemy_choice=1
    enemy_dmg = Zombie.generateRandomDamage()
    Player.takeDamage(enemy_dmg)
    print(bcolors.FAIL + bcolors.BOLD +"Enemy Strike For:",enemy_dmg,"Your Hp is :",Player.get_hp(),bcolors.ENDC)
    
    print("--------------")
    print(bcolors.FAIL + "Enemy Health Points : " + str(Zombie.get_hp())+"/"+str(Zombie.getMaxHp())+bcolors.ENDC)

    print(bcolors.OKGREEN + "Player Health Points : " + str(Player.get_hp())+"/"+str(Player.getMaxHp())+bcolors.ENDC)
    print(bcolors.OKGREEN + "Player Mana Points : " + str(Player.get_cmana())+"/"+str(Player.getMaxMana())+bcolors.ENDC)

    if Zombie.get_hp() == 0:
        print(bcolors.OKGREEN + "You Won" + bcolors.ENDC)
        one=False
    elif Player.get_hp() == 0:
        print(bcolors.FAIL+"You Lose"+bcolors.ENDC) 
        one=False    