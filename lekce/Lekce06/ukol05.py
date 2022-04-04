class Film:
    nazev: str

    def __str__(self):
        return f"... {self.nazev}"

class Uzivatel:
    def __init__(self):
        self.filmy = []
    
    def pridej_film(self, film):
        self.filmy.append(film)
    
    def vypis_filmy(self):
        for f in self.filmy:
            print(f.nazev)


uzivatel = Uzivatel()

uzivatel.filmy[0].nazev