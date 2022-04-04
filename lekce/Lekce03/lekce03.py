#  funkce

# def pozdrav(jmeno: str):
#     print(f"Ahoj {jmeno}!")

# jmeno = input("Zadej jmeno: ")
# pozdrav(jmeno)
"""
def secti (a, b):
    return a+b

vysledek = secti(4, 5)
print(vysledek)
"""

def prevod_eur_na_czk (pocet_eur: int, kurz: float = 25):
    # funkce prevadi eura na koruny 
    return kurz * pocet_eur 

print(prevod_eur_na_czk(pocet_eur=10, kurz=24.7))