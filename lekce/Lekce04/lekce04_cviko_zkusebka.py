class Zamestnanec:
    def __init__(self, jmeno, zkusebni_doba: bool, pozice = "uklizecka"):
        self.jmeeeno = jmeno
        self.pozice = pozice
        self.pocet_dni_dovolene = 30
        self.zkusebni_doba = zkusebni_doba
 
    def cerpani_dovolene(self, pocet_dni_cerpani):
        if self.pocet_dni_dovolene >= pocet_dni_cerpani:
            self.pocet_dni_dovolene -= pocet_dni_cerpani
            print(f"Prejeme peknou dovolenou. Zbyva vam {self.pocet_dni_dovolene} dni dovolene")
        else:
            print(f"Nemate dost dovolene, maximalne muzete cerpat {self.pocet_dni_dovolene}")

    def __str__(self):
        return f'Zamestnanec se jmenuje {self.jmeeeno} a pracuje jako {self.pozice} a ma {self.pocet_dni_dovolene} pocet dni dovolene. {"Zamestnanec je ve zkusebni dobe." if self.zkusebni_doba else "Neni ve zkusebni dobe"}'

eda = Zamestnanec("Eduard Maly", True, "udrzbar")
print(eda)
lota = Zamestnanec("Lota Surova", False )
print(lota)
