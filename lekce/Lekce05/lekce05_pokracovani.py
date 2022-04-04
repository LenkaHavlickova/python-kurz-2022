class Zamestnanec:
    def __init__(self, jmenicko, pozice = "uklizecka"):
        self.jmeeeno = jmenicko
        self.pozice = pozice
        self.pocet_dni_dovolene = 30
      
    def __str__(self):
        return f"Zamestnanec se jmenuje {self.jmeeeno} a pracuje jako {self.pozice} a ma {self.pocet_dni_dovolene} pocet dni dovolene. "

class Manazer (Zamestnanec):
    def __init__(self, jmenicko, pozice = "manazer", pocet_podrizenych = 1):
       super().__init__(jmenicko, pozice)
       self.pocet_podrizenych = pocet_podrizenych
       self.podrizeni = []
    
    def pridej_podrizeneho(self, podrizeny):
        self.podrizeni.append(podrizeny)

    def vypis_podrizene(self):
        podrizeni = ""
        for item in self.podrizeni:
            podrizeni += item.jmeeeno + ", "
        return podrizeni


    def __str__(self):
        return super().__str__() + f"Ma {self.pocet_podrizenych} podrizenych. A to: {self.vypis_podrizene()}"

franta = Zamestnanec("Franta Novak", "SW Architect")
klara = Zamestnanec("Klara Mala", "Scrum Master")
jana = Manazer("Jana Stuhlikova", "Vedouci", 2)
jana.pridej_podrizeneho(klara)
jana.pridej_podrizeneho(franta)
# print(jana.vypis_podrizene())
print(jana)