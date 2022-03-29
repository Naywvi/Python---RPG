
import random

class Random_Item:
    """
    Random Items
    """

    Name_Item = ["Common healing potion","Common strengh potion","Common defense potion","Classic healing potion","Classic strengh potion","Classic defense potion","Rare healing potion","Rare strengh potion","Rare defense potion","Legendary healing potion","Legendary strengh potion","Legendary defense potion"]
    
    def __init__(self):

        rdn = random.randint(0,11)
        self.rdn_stat_po = 0
        Pot = self.Name_Item[rdn]
        self.type = 0
        if rdn+1 <= 3: 
            if Pot == "Common healing potion": self.rdn_stat_po = self.loop(15,20);self.type = 1
            elif Pot == "Common strengh potion": self.rdn_stat_po = self.loop(5,10);self.type = 2
            elif Pot == "Common defense potion": self.rdn_stat_po = round(random.uniform(1.1,1.3),1);self.type = 3
            
        elif rdn+1 <= 6:
            if Pot == "Classic healing potion": self.rdn_stat_po = self.loop(20,25);self.type = 1
            elif Pot == "Classic strengh potion": self.rdn_stat_po = self.loop(10,15);self.type = 2
            elif Pot == "Classic defense potion": self.rdn_stat_po = round(random.uniform(1.2,1.4),1);self.type = 3

        elif rdn+1 <= 9:
            if Pot == "Rare healing potion": self.rdn_stat_po = self.loop(30,35);self.type = 1
            elif Pot == "Rare strengh potion": self.rdn_stat_po = self.loop(20,25);self.type = 2
            elif Pot == "Rare defense potion": self.rdn_stat_po = round(random.uniform(1.5,1.7),1);self.type = 3

        elif rdn+1 <=12 :
            if Pot == "Legendary healing potion": self.rdn_stat_po = self.loop(100,130);self.type = 1
            elif Pot == "Legendary strengh potion": self.rdn_stat_po = self.loop(40,45);self.type = 2
            elif Pot == "Legendary defense potion": self.rdn_stat_po = round(random.uniform(1.8,2.0),1);self.type = 3

        self.Items = [Pot,self.rdn_stat_po,self.type]

    def loop(self, rdn1, rdn2):
        return random.randint(rdn1,rdn2)

Random_Item()


