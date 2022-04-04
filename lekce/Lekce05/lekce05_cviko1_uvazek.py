class Zamestnanec:
    def __init__(self, jmenicko, pozice = "uklizecka"):
        self.jmeeeno = jmenicko
        self.pozice = pozice
        self.pocet_dni_dovolene = 30
        
    def cerpani_dovolene(self, pocet_dni_cerpani):
        if self.pocet_dni_dovolene >= pocet_dni_cerpani:
            self.pocet_dni_dovolene -= pocet_dni_cerpani
            print(f"Prejeme peknou dovolenou. Zbyva vam {self.pocet_dni_dovolene} dni dovolene")
        else:
            print(f"Nemate dost dovolene, maximalne muzete cerpat {self.pocet_dni_dovolene}")

    def __str__(self):
        return f"Zamestnanec se jmenuje {self.jmeeeno} a pracuje jako {self.pozice} a ma {self.pocet_dni_dovolene} pocet dni dovolene. "


class Manazer (Zamestnanec):

    def __init__(self, jmenicko, pozice = "manazer", pocet_podrizenych = 1):
       super().__init__(jmenicko, pozice)
       self.pocet_podrizenych = pocet_podrizenych
    
    def __str__(self):
        return super().__str__() + f"Ma {self.pocet_podrizenych} podrizenych."

class Brigadnik (Zamestnanec):

    def __init__(self, jmenicko, pozice, uvazek):
        super().__init__(jmenicko, pozice)
        self.uvazek = uvazek
    
    def __str__(self):
        return super().__str__() + f"Ma uvazek ve vysi {self.uvazek} %."

roman = Brigadnik("Roman Kamenik", "HR specialist", 50)
print(roman)