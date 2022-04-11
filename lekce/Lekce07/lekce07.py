import re

# znacka1 = "1A 25364"
# znacka2 = "4A6 8244"
# znacka3 = "4A6 8244 ABC"

# reg_vyraz_spz = re.compile("\d[A-Z][A-Z0-9] \d{4}")

# print(reg_vyraz_spz.match(znacka2))
# print(reg_vyraz_spz.match(znacka1))
# print(reg_vyraz_spz.match(znacka3))
# print(reg_vyraz_spz.fullmatch(znacka3))

# znacka_input = input("Zadej znacku: ")
# if reg_vyraz_spz.fullmatch(znacka_input):
#     print("Znacka je ok")
# else:
#     print("Neni ok")

zapis = """
Zápisy o provedených vyšetřeních:
Pacient 6407156800 trpěl bolestí zad a byl poslán na vyšetření. 
Pacientka 8655057477 přišla na kontrolu po zranění kotníku.
Do ordinace telefonovala pacientka 7752126712, které byl elektronicky vydán recept na Paralen. 
"""

reg_vyraz_rc = re.compile("\d{10}")
rodna_cisla = reg_vyraz_rc.findall(zapis)

for rodne_cislo in rodna_cisla:
    print(rodne_cislo)