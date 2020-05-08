from Classes.game import charClasses,allColors,bcolors
from Classes.skills import skill
from Classes.inventory import item
import  random

#warrior skills
MightyBlow = skill("Mighty Blow",15,45,"skill")
SoldierStrike = skill("Soldier Strike",25,random.randrange(50,90),"skill")
TripleChop = skill("Triple Chop",50,150,"ultimate")
# Mage Skills 
Fireball = skill("FireBall",15,45,"spell")
LightningBolt = skill("LightningBolt",25,random.randrange(50,90),"spell")
ThunderStorm = skill("ThunderStorm",50,150,"ultimate")
# Archer Skills 
arcingShot = skill("Arcing Shot",15,45,"skill")
FocusedShot = skill("Focused Shot",25,random.randrange(50,90),"skill")
#Healer Skill
cure = skill("cure",20,70,"Heal") #heal one party member
cura = skill("cura",50,120,"Heal") #heal 1 party member
Divine = skill("Divine",100,250,"Heal") # heal all party member
#Enemy Skill
Cursing = skill("Cursing",15,45,"spell")
Torment = skill("Torment",2,90,"spell")
Jinx = skill("Jinx",50,150,"spell")

MageSpells = [Fireball,LightningBolt,ThunderStorm]
HealerSpell = [cure,cura,Divine]
EnemySpells = [Cursing,Torment,Jinx]

#Consumables Items
sPotion = item("Small Hp Potion","hpotion","Heals player for 50 hp",50)
sMPotion = item("Small Mp Potion","mpotion","Restore player Mana by 50 Points",50)
attPotion = item("Attack potion","apotion","increase AttackPoints  40 Points",40)
lPotion = item("Large Hp Potion","hpotion","Heals player for 100 hp",100)
elixer = item("Elixer","hpotion","Fully Restore HP/MP",999)

#attack items 
gernade = item("Gernade","attack","Deals 500 Damage",500)

Slime = charClasses(EnemySpells,150,90,40,10,"Slime",0,[])
Goblin = charClasses(EnemySpells,300,110,60,20,"Goblin",0,[])
Zombie = charClasses(EnemySpells,1500,150,80,30,"Zombie",0,[])
Demon = charClasses(EnemySpells,750,190,110,40,"Demon Soul",0,[])
Cyclops = charClasses(EnemySpells,5000,500,130,90,"Boss-Cyclops",0,[])
Phoenix = charClasses(EnemySpells,3000,1000,150,120,"Boss-Phoenix",0,[])

Monsters = [Slime,Goblin,Zombie,Demon]
Bosses = [Cyclops,Phoenix]

PLayer_items =[{"item" : sPotion,"quantity":10},{"item" : lPotion,"quantity":5},
{"item" : sMPotion,"quantity":10},{"item" : attPotion,"quantity":3},{"item" : elixer,"quantity":5},
{"item" : gernade,"quantity":1}]

Player = charClasses(MageSpells,360,80,90,30,"Mage",0,PLayer_items)





one= True
while one:
    print("===================")
    Player.Choice()
    choice= input(" Select An option:")
    if choice:
        index = int(choice)-1
    else:
        continue
    if not index in(0,1,2):
        print(bcolors.OKBLUE+"please choose a valid option :"+bcolors.ENDC)
        continue
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

        magic_dmg = Player.skills[skill_index].generateRandomDamage()
        Player_mana = Player.get_cmana()
        if Player.skills[skill_index].cost > Player_mana:
            print(bcolors.FAIL + bcolors.BOLD +"You Dont Have Mana"+bcolors.ENDC)
            continue

        Player.reduce_mana(Player.skills[skill_index].cost)
        if Player.skills[skill_index].type == "Heal":
            Player.heal(magic_dmg)
            print(bcolors.OKGREEN+"You healed For:",magic_dmg)
        else:
            Zombie.takeDamage(magic_dmg)
            print("You Delt",magic_dmg," Damage To",Zombie.type,"with",Player.skills[int(choice)-1].name,"And it cost: ",Player.skills[skill_index].cost,"Your Current Mana: ",Player.get_cmana())

    elif index == 2:
        Player.choose_item()
        item_choice=int(input("Choose item")) - 1 

        if item_choice == -1:
            continue 
        item = Player.items[item_choice]
        if item["quantity"] > 0:
            item["quantity"] -= 1
        else:
            print(bcolors.FAIL+"You dont have more of this item")
            continue
        
        if item["item"].type == "hpotion":
            Player.heal(item["item"].value)
            if item.name == "Elixer":
                print(bcolors.OKGREEN+"Your HP/MP have been restored")
            else:
                print(bcolors.OKGREEN+"You healed For:",item["item"].value,"Your HP:",Player.get_hp())       
        elif item["item"].type == "apotion":
            Player.addattack(item["item"].value)
            print(bcolors.OKGREEN+"in/Max Attack increased By:",item["item"].value/2,item["item"].value)
        elif item["item"].type == "mpotion":
            Player.addMana(item["item"].value)  
            print(bcolors.OKGREEN+"Mana increased By:",item["item"].value)
        elif item["item"].type =="attack":
            Zombie.takeDamage(item["item"].value)
            print("You Delt",item["item"].value," Damage To",Zombie.type)
    
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