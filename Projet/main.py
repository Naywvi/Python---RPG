import os
import os.path
import random
import time
from colorama import Fore#, Back, Style
import json

from game import Game


class Start():
    """
    Start the game
    """
    OS = -1

    def bind_rdn(self,rdn1,rdn2) -> int:
        return random.randint(rdn1,rdn2) 

    def __init__(self):
        Os_Choose()
        Clear(self.OS)
        Menu()
    
class Clear(Start):
    """
    Clear terminal by input os on Os_Choose
    """

    def __init__(self,OS):
        if OS == 0: os.system("cls")
        elif OS == 1:os.system("clear")
        else: print("\nWrong selection\n"); return Os_Choose()
        
class Os_Choose(Start):
    """
    Select Os to clean terminal WIN -> cls Linux -> clear
    """
    Os = ["\n0 - Windows","1 - Other"]

    def __init__(self):
        print(Fore.WHITE +"\nWhat is your OS ?\n{}".format("\n".join(self.Os)))
        self.return_os_input = input("\nSelect a field : ")
        self.OS_SELECTED(self.return_os_input)

    #Bind 0 or 1 to use "clear or cls" and use it in Clear()
    def OS_SELECTED(self,OS_RETURNED):
        if OS_RETURNED == "0":print(Fore.RED +"You selected Windows."); Start.OS = 0
        elif OS_RETURNED == "1":print(Fore.GREEN +"You selected Other."); Start.OS = 1
        else: print(Fore.RED +"\nWrong selection");return Os_Choose()

        
class Menu(Start):
    """
    Menu
    """
    Menu = ["\n0 - Create new Game","1 - Load saved game","2 - About","3 - Exit"]

    def __init__(self):
        print(Fore.CYAN + " ""\n".join(self.Menu),"\n" )
        self.select_menu = input(Fore.WHITE +"Select a field : ")
        Menu_Select(self.select_menu)

class Menu_Select(Menu):
    """
    Selection of menu
    """

    def __init__(self,return_menu_select):
        if return_menu_select == "0":New_Player()
        elif return_menu_select == "1":
            print("\nLoad\n")
            ##If have save
            if os.path.isfile("Projet/save.json"):
                fileObject = open("Projet/save.json", "r")
                jsonContent = fileObject.read()
                aList = json.loads(jsonContent)
                Clear(self.OS)
                print("You load the last save \n\n- Name :",aList[0],"\n- Type : ", aList[1],"\n- Level : ", aList[6])
                time.sleep(3)
                Game(aList)
            ##If don't have save
            else:Clear(self.OS);print("You don't have a save. Create a new character.");time.sleep(3);Clear(self.OS);return Menu()
            

        elif return_menu_select == "2":print("\nAbout\n");return self.about()
        elif return_menu_select == "3":print("\nend\n");return quit ()
        else: 
            Clear(self.OS)
            time.sleep(0.5)
            print(Fore.RED +"\nWrong selection\n" + Fore.WHITE)
            time.sleep(0.5)
            Clear(self.OS)
            return Menu()
    def about(self):
        Clear(self.OS)
        print("About : \n")
        print("https://github.com/Naywvi\n")
        print("By Nagib Lakhdari")
        time.sleep(3)
        Clear(self.OS)
        return Menu()
class New_Player(Start):
    """
    New Character
    """
    Type_character = ["\n0 - Warrior","1 - Magician","2 - Assassin","3 - Tank\n"]
    FLEMME_character = ["Warrior","Magician","Assassin","Tank"]
    strengh = 0
    resistance = 0

    def __init__(self):  
        Clear(self.OS)
        self.name_of_new_player = input(Fore.CYAN +"The name of the charactere : ")
        Clear(self.OS)
        self.select_type_of_charactere = print("\n".join(self.Type_character));self.Setup_Random_stats(input(Fore.WHITE +"Selected a field : "))

    def Setup_Random_stats(self, inp_character):
        if inp_character == "0": self.resistance = self.bind_rdn(25,35);self.strengh = self.bind_rdn(32,42);self.Print_type_selected(int(inp_character)) #Warrior stats
        elif inp_character == "1": self.resistance = self.bind_rdn(20,30);self.strengh = self.bind_rdn(28,35);self.Print_type_selected(int(inp_character))  #Magician stats
        elif inp_character == "2": self.resistance = self.bind_rdn(15,25);self.strengh = self.bind_rdn(70,80);self.Print_type_selected(int(inp_character))  #Assassin stats
        elif inp_character == "3": self.resistance = self.bind_rdn(70,100);self.strengh = self.bind_rdn(8,15);self.Print_type_selected(int(inp_character))  #Assassin stats
        else:
            Clear(self.OS)
            time.sleep(0.5)
            print(Fore.RED +"\nWrong selection\n" + Fore.WHITE)
            time.sleep(0.5)
            Clear(self.OS)
            return New_Player()

    def Print_type_selected(self, inp_character):
        Clear(self.OS)
        print("You selected a "+Fore.RED +"{}".format("".join(self.FLEMME_character[inp_character])+Fore.WHITE +", TO CLEAN THIS Shit world. \n"))
        print(Fore.CYAN+"{} ".format(self.name_of_new_player)+Fore.WHITE +"the "+Fore.RED + "{}".format("".join(self.FLEMME_character[inp_character]) + Fore.WHITE + " have {}% of resistance, and {} strengh.".format(self.resistance,self.strengh)))
        self.all_stats_players = [self.name_of_new_player,self.FLEMME_character[inp_character],self.resistance,self.strengh,100,0,0]#100 = HP / 0 = lvl 0
        while True:
            self.inp_ready = input("\nARE YOU READY ?!! [y]/[n] : ")
            if self.inp_ready == "y": Game(self.all_stats_players)
            elif self.inp_ready == "n":return New_Player()
            else:
                Clear(self.OS)
                time.sleep(0.5)
                print(Fore.RED +"\nWrong selection\n" + Fore.WHITE)
                time.sleep(0.5)
                Clear(self.OS)



#g.Game()
Start()