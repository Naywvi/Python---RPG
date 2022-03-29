import random

class Random_Boss:
    """
    Randomise Boss Type/Name/HP/Strengh/Defense
    """
    
    Name_Boss =["The Deadly Keeper","The Quick Child","The Wretched Freak","The Chaotic Bane Pig","The Lone Razorback Critter","The Sapphire Dawn Cobra","The Undead Anomaly","The Bold Shrieker","The Wretched Ooze","The Rabid Nightmare Swine","The Wild Phantom Hippo","The Black-Striped Grieve Deer","The Disgusting Creature","The Empty Mongrel","The Outlandish Hybrid","The Black-Eyed Killer Boar","The Ebon Nightmare Freak","The Primitive Cavern Fiend"]
    
    def __init__(self):
        self.Name_Boss = self.Name_Boss[random.randint(0,17)]
        self.Strengh_Boss = random.randint(5,35)
        self.Defense_Boss = round(random.uniform(2.2,3.2),1)
        self.PV_Boss = int(100 * self.Defense_Boss)

        self.Boss = [self.Name_Boss,self.Strengh_Boss,self.Defense_Boss,self.PV_Boss]


Random_Boss()


