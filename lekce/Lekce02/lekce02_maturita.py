vysledky = [
  {"Jméno": "Mirek Dušín", "Český jazyk": 1, "Anglický jazyk": 2, "Matematika": 1, "Biologie": 1, "Zeměpis": 1},
  {"Jméno": "Jarka Metelka", "Český jazyk": 3, "Anglický jazyk": 1, "Matematika": 3, "Dějepis": 2, "Ekonomika": 5},
  {"Jméno": "Jindra Hojer", "Český jazyk": 2, "Anglický jazyk": 2, "Matematika": 1, "Biologie": 3, "Chemie": 3},
  {"Jméno": "Červenáček", "Český jazyk": 1, "Anglický jazyk": 1, "Matematika": 1, "Fyzika": 2, "Informatika": 4},
  {"Jméno": "Rychlonožka", "Český jazyk": 4, "Anglický jazyk": 3, "Matematika": 2, "Chemie": 1, "Biologie": 4},
]

# for student in vysledky:
#     jmeno = student.pop("Jméno")
#     znamky = student.values()
#     prumer = sum(znamky) / len(znamky)
#     print(f'{jmeno} ma prumer znamek {prumer}')

for student in vysledky:
    soucet_znamek = 0
    pocet_znamek = 0
    for key, value in student.items():
        if isinstance(value, int):
            soucet_znamek += value
            pocet_znamek += 1
        else:
            jmeno = value
    prumer = soucet_znamek / pocet_znamek
    print(f"{jmeno} ma prumer znamek {prumer} ")