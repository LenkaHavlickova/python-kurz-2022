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

class CennyBalik (Balik):

    def __init__(self, adress, weight, value, delivered = False):
        super().__init__(adress, weight, delivered)
        self.value = value

    def __str__(self):
        return super().__str__() + f" Balik ma hodnotu {self.value} Kc."

muj_Balik = CennyBalik("KOnecna 1, Praha 1", 15, 455, True)
print(muj_Balik)
levny_Balik = Balik("Dlouha 5, Praha 5", 20)
print(levny_Balik)
             