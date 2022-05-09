import pandas

names = pandas.read_csv("lekce/Lekce10/jmena.csv")

# Vypiš všechny řádky se jmény, jejichž nositelé mají průměrný věk vyšší než 60.
print(names[names["věk"]>60])


# Vypiš pouze jména z těch řádků, kde četnost je mezi 80 000 a 100 000.

mene_cetna = names["četnost"]<100000
vice_cetna = names["četnost"]>80000
print(names[mene_cetna & vice_cetna])


# Vypiš jména a četnost pro jména se slovanským nebo hebrejským původem. Kolik takových jmen je?
slov_hebr_names = names["původ"].isin(["slovanský", "hebrejský"])
print(names[slov_hebr_names][["jméno", "četnost", "původ"]])
print(len(names[slov_hebr_names]))


# Vypiš všechna jména, která mají svátek první 3 dny v prosinci.
december = names["svátek"].isin(["1.12", "2.12", "3.12"])
print(names[december])


