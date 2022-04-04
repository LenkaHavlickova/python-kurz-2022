class Zamestnanec:
    def __init__(self, jmenicko, pozice = "uklizecka"):
        self.jmeeeno = jmenicko
        self.pozice = pozice
        self.pocet_dni_dovolene = 30
        # if pozice is None:
        #     self.pozice = "uklizecka"
        # else:
        #     self.pozice = pozice
    def cerpani_dovolene(self, pocet_dni_cerpani):
        if self.pocet_dni_dovolene >= pocet_dni_cerpani:
            self.pocet_dni_dovolene -= pocet_dni_cerpani
            print(f"Prejeme peknou dovolenou. Zbyva vam {self.pocet_dni_dovolene} dni dovolene")
        else:
            print(f"Nemate dost dovolene, maximalne muzete cerpat {self.pocet_dni_dovolene}")

    def __str__(self):
        return f"Zamestnanec se jmenuje {self.jmeeeno} a pracuje jako {self.pozice} a ma {self.pocet_dni_dovolene} pocet dni dovolene."

frantisek = Zamestnanec("Frantisek Novak", "udrzbar" )
print(frantisek)
# frantisek.cerpani_dovolene(10)
# frantisek.cerpani_dovolene(10)
# frantisek.cerpani_dovolene(30)
# frantisek.cerpani_dovolene(10)


# klara = Zamestnanec("Klara Nova", "vedouci")
# print(klara.vypis_jmeno())

# debora = Zamestnanec("Debora Ticha")
# print(debora.vypis_jmeno())