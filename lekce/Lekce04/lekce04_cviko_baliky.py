class Balik:
    def __init__(self, adress, weight, delivered = False):
        self.adress = adress
        self.weight = weight
        self.delivered = delivered
    
    def deliver(self):
        self.delivered = True
    
    def __str__(self):
        if self.delivered:
            return f"Balik byl dorucen na adresu: {self.adress}. Ma hmotnost {self.weight} kg."
        else:
            return f"Balik nebyl dorucen a ma byt dorucen na adresu: {self.adress}. Ma hmotnost {self.weight} kg."
        # "ano" if self.delivered else "Ne"

prvni_balik = Balik("Dlouha ulice", 15)
print(prvni_balik)
prvni_balik.deliver()
print(prvni_balik)

druhy_balik = Balik ("Narodni trida", 16, True)