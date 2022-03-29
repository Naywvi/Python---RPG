
import random

class Random_Monster:
    """
    Randomise Monster Type/Name/HP/Strengh/Defense
    """
    Name_Monster = ["Gnome","Tarantula","Gremlins","Rock golem","Spider","Ice Spider","Red Spider","Anaconda","snake","Zombie","Dreamsnare","Spectraltalon","Nethersnare","Bonevine","The Dirty Blob","Foultooth","Duskmonster","Bladesword","Cryptfoot","Terrorcat","Vexchild","Venombrood"]
    
    def __init__(self):
        self.Name_monster = self.Name_Monster[random.randint(0,21)]
        self.Strengh_Monster = random.randint(15,25)
        self.Defense_Monster = round(random.uniform(1.2,2.2),1)
        self.PV_Monster = int(50 * self.Defense_Monster)
        
        self.Monster = [self.Name_monster,self.Strengh_Monster,self.Defense_Monster,self.PV_Monster]
        

Random_Monster()

