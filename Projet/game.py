from ast import Return
import json
import random
import time
from colorama import Fore, Back, Style


import monsters as mo
import boss  as bo
import items  as it

    
class Game():
    """
    The game
    """
    def __init__(self,stats_p): 
        self.stats = stats_p
        #RP - Story
        Map(self.stats)
        

class Map(Game):
    """
    Random Map
    """
    human = "웃"
    def __init__(self,stats_p):

        self.inventory = []#[7:len(aList)]
        self.stat = stats_p#[0:7]

        #If have inventory -> for load
        if len(self.stat) != 7:
            #index / index
            
            for i in stats_p[7:len(stats_p)]:
                self.inventory.append(i)
                
            del stats_p[7:len(stats_p)] #Clean len(self.stat) != 7:
            stats_p[0:7] = self.stat
            
            

        self.map = self.Create_Map()
        self.printing(self.Random_Import_On_The_map(self.map))

    #create Map

    def Create_Map(self):
        map = []
        for i in range(0,16,1):
            map.append([i])
            for j in range(1,16,1):
                map[i].append("_")
        return map

    #Print random point in map
    def Random_Import_On_The_map(self,map_vierge):
        index_boss = 1
        
        for i in range(16):
            for j in map_vierge[i]:
                indx = map_vierge[j]

                rdn = random.randint(0,6)#Difficulty spawn
                rdn_indx = random.randint(0,15)

                if index_boss == 1: indx[rdn_indx] = "B";index_boss = 2
                elif rdn == 1: indx[rdn_indx] = "c"
                elif rdn == 2: indx[rdn_indx] = "m"
                break#One per line

        #initialise out of loop = cause > bug 
        for i in range(16):
            map_vierge[i][0] = "_"

        self.spawn(map_vierge)#spawn

        return map_vierge

    #spawn
    def spawn(self, map_spawn):
        map_spawn[len(map_spawn)-1][0] = "웃"


    #Print The map
    def printing(self, map_end):

        print("")
        for i in range(16):
            print(' '.join(str(e) for e in map_end[i]))
        self.Movement(map_end)
        
    def Where_Is_Human_In_The_Map(self,map_mov):
        index = -1
        index2 = 0
        for i in range(16):
            index += 1
            for j in map_mov[i]:

                if j == "웃":
                    for k in map_mov[i]:

                        if k == "웃":break

                        index2 += 1
                    return index,index2 ,map_mov#Define index of human
                

    #Select input
    def Movement(self,map_reset):
        
        inp = input("\n           {}\n           {} \n\n     Use this keys to moove\n\n               ".format("    z   ","  q s d \n\npress 'm' to return on the menu"))
        pos1, pos2, map_reset_end = self.Where_Is_Human_In_The_Map(map_reset)

        if inp == "z":
            self.Index_Entity_On_Map(map_reset_end[pos1-1][pos2])

            map_reset_end[pos1-1][pos2] = "웃";map_reset_end[pos1][pos2] = Fore.MAGENTA+"_"+Fore.WHITE
            return self.printing(map_reset_end)#return to printMap

        elif inp == "q":
            if map_reset_end[pos1][0] == "웃":
                self.Index_Entity_On_Map(map_reset_end[pos1][0])
                map_reset_end[pos1][0] = "웃"
            else:
                self.Index_Entity_On_Map(map_reset_end[pos1][pos2-1])

                map_reset_end[pos1][pos2-1] = "웃";map_reset_end[pos1][pos2] = Fore.MAGENTA+"_"+Fore.WHITE
            return self.printing(map_reset_end)#return to printMap

        elif inp == "s":

            self.Index_Entity_On_Map(map_reset_end[pos1+1][pos2])

            map_reset_end[pos1+1][pos2] = "웃";map_reset_end[pos1][pos2] = Fore.MAGENTA+"_"+Fore.WHITE
            return self.printing(map_reset_end)#return to printMap

        elif inp == "d":
            
            if map_reset_end[pos1][-1] == "웃":
                self.Index_Entity_On_Map(map_reset_end[pos1][0])
                map_reset_end[pos1][-1] = "웃"

            else:
                self.Index_Entity_On_Map(map_reset_end[pos1][pos2+1])
                map_reset_end[pos1][pos2+1] = "웃";map_reset_end[pos1][pos2] = Fore.MAGENTA+"_"+Fore.WHITE

            return self.printing(map_reset_end)#return to printMap

        elif inp == "m":
            index = 0
            print("Name : ",self.stat[0],"Your are a : ",self.stat[1],"Resistance ->",self.stat[2],"Strengh ->",self.stat[3],"HP ->",self.stat[-3],"LEVEL ->",self.stat[-1])#Todo
            if len(self.inventory) != 0:
                print("\n#=============================#\nYour inventory")
                while True:
                    print(Fore.GREEN + " \n",index ,"-", self.inventory[index][0])
                    if index == len(self.inventory)-1:
                        #index = 0
                        break

                    index += 1
                print(Fore.WHITE + "\n#=============================#\n")
            else: print(Fore.RED+"\nInventory is empty ... Try to loot a chest."+Fore.WHITE)
            print("0 - Save & quit\n1 - End\n2 - return to game")
            while True:
                inpSave =  input("\nSelect a field : ")
                if inpSave == "0":
#SAVE
                    with open('Projet/save.json', 'w') as outfile:
                        outfile.write(json.dumps(self.stat + self.inventory, indent=4))
                        
                    time.sleep(1)
                    print("saved")#SAVVEEEEE & return game
                    return quit()
                elif inpSave == "1":return quit()
                elif inpSave == "2":return self.printing(map_reset_end)
                else: print("Wrong selection")
            
        else: print("        Wrong selection");return self.printing(map_reset_end)

    def Index_Entity_On_Map(self,end_pos):
        if end_pos == "c":
            drop = Entity.Chest()
            self.inventory.append(drop)
        elif end_pos == "m":Entity.Mob(self.stat,self.inventory)
        elif end_pos == "B":
            Entity.Boss(self.stat,self.inventory)

            #add inventaire to recreate Map
            list_inv = []
            for i in self.inventory:
                list_inv.append(i)
            Map(self.stat+list_inv)

        if self.stat[-2] > 100:#Give +1 lvl if self.stat[-2] > 100
            print(Fore.GREEN+"LEVEL UP"+Fore.WHITE)
            print(Fore.GREEN+"You are Level {}.".format(self.stat[-1])+Fore.WHITE)
            self.stat[-2] -= 100
            self.stat[-1] += 1
            time.sleep(1.5)
        

class Entity(Game):
    """
    Manages entities
    """
    
    def __init__(self):
        print("")


#[Type Object str, Stats, Type int]
    def Chest():
        i = it.Random_Item()
        print(Fore.GREEN+"You drop a {} he was placed in your inventory.".format(i.Items[0])+Fore.WHITE)
        time.sleep(1.5)
        return i.Items
        
#[Name_monster, Strengh_Monster, Defense_Monster, PV_Monster]    
    def Mob(stat_p,inventory):
        m = mo.Random_Monster()
        Entity.fight(m.Monster,stat_p,inventory)

#[Name_Boss, Strengh_Boss, Defense_Boss, PV_Boss]       
    def Boss(stat_p,inventory):
        b = bo.Random_Boss()
        Entity.fight(b.Boss,stat_p,inventory)

#[name_of_new_player, Type, resistance, strengh, HP, LVL]
    def fight(mob_stats,Player_stats,inventory):

        #Difficulty up with lvl
        if Player_stats[-1] > 0:

            multiplicateur = Player_stats[-1]
            multiplicateur /= 10

            if multiplicateur < 1:
                multiplicateur += 1
            mob_stats[1] *= multiplicateur
        
        print(Fore.RED + "\n{} attaque !!".format(mob_stats[0]))
        time.sleep(1)
        print("\n{} have {} strengh and {} HP !!\n".format(mob_stats[0],mob_stats[1],mob_stats[-1]))
        time.sleep(2)
        print(Fore.GREEN + "{} you have {} HP and you have {} of strengh now.".format(Player_stats[0],Player_stats[-3],Player_stats[-4]))
        time.sleep(2)
        inp = input(Fore.WHITE +"\nDo you want :\n\n1 - Attaque ?\n2 - Use a object of your inventory ?\n\nSelect a field : ")
        
        while inp:
            #dead
            if Player_stats[-3] < 0:
                print(Fore.RED + "YOU ARE DEAD")
                return quit()
            if inp == "1":

                mob_stats[-1] -= Player_stats[-4]
                print(Fore.GREEN + "\nYou took {} HP away from him".format(Player_stats[-4]))
                time.sleep(1)

                #dead Mob/Boss
                if mob_stats[-1] <= 0:
                    print(Fore.GREEN +"\nYou kill {}.".format(mob_stats[0]))
                    print(Back.RED + Fore.WHITE +"\nWarning you have {} HP left.".format(Player_stats[-3])+Style.RESET_ALL)
                    xp = mob_stats[1] *  mob_stats[2]
                    Player_stats[-2] += xp
                    break

                print(Fore.RED +"\n{} attaque to!!".format(mob_stats[0]))
                time.sleep(2)
                Player_stats[-3] -= mob_stats[1]
                print("\nHe takes {} HP away from you. "+ Fore.GREEN +"You have {} HP left".format(mob_stats[1],Player_stats[-3]))
                time.sleep(1)


                print(Fore.RED + "\nHe has {} HP left".format(mob_stats[-1]))
                inp = input(Fore.WHITE+"\n#=============================#\n\nDo you want :\n\n1 - Attaque ?\n2 - Use a object of your inventory ?\n\nSelect a field : ")
            
            elif inp == "2":#Open inventory

                index = 0
                if len(inventory) != 0:
                    while True:
                        print(Fore.GREEN + " \n",index ,"-", inventory[index][0])
                        if index == len(inventory)-1:
                            break

                        index += 1

                    inpI = input(Fore.WHITE + "\nSelect a Item : ")
                    field = inventory[int(inpI)][2]

                    if field == 1: Player_stats[-3] += inventory[int(inpI)][1]
                    elif field == 2: Player_stats[-2] += inventory[int(inpI)][1]
                    elif field == 3:
                        Player_stats[-3] *= inventory[int(inpI)][1]
                        Player_stats[-3] = int(Player_stats[-3])
                    del inventory[int(inpI)]
                else: print(Fore.RED+"\nInventory is empty ... Try to loot a chest."+Fore.WHITE)
                inp = "1"
            else: inp = input(Fore.RED + "\n/!\WRONG SELECTION/!\ "+Fore.WHITE+ "\n\nDo you want :\n1 - Attaque with (attaqueList)\n2 - Use a object of your inventory ?\nSelect a field : ")

        