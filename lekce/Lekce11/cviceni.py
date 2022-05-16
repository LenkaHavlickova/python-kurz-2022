import requests

r = requests.get("https://kodim.cz/czechitas/progr2-python/python-pro-data-1/agregace-a-spojovani/excs/studenti/assets/jmena.csv")
open("jmena.csv", "wb").write(r.content)
r = requests.get("https://kodim.cz/czechitas/progr2-python/python-pro-data-1/agregace-a-spojovani/excs/studenti/assets/studenti1.csv")
open("studenti1.csv", "wb").write(r.content)
r = requests.get("https://kodim.cz/czechitas/progr2-python/python-pro-data-1/agregace-a-spojovani/excs/studenti/assets/studenti2.csv")
open("studenti2.csv", "wb").write(r.content)

# Načti dva datové sety studentů do oddělených pandas DataFrame a pomocí funkce concat je spoj do jednoho setu.
import pandas
studenti1 =pandas.read_csv("lekce/Lekce11/studenti1.csv") 
studenti2 =pandas.read_csv("lekce/Lekce11/studenti2.csv")



studenti = pandas.concat([studenti1, studenti2], ignore_index=True)


# Pokud studentovi chybí ročník, znamená to, že již nestuduje. Pokud mu chybí číslo skupiny, znamená to, že jde o dálkového studenta. Kolik studentů v datovém setu již nestuduje a kolik jsou dálkoví studenti?
print(studenti[studenti["ročník"].isnull()].shape)


print(studenti[studenti["kruh"].isnull()].shape)


# Vyčisti data od studentů, kteří nestudují nebo studují jen dálkově. Nadále budeme pracovat pouze s prezenčními studenty.
studenti = studenti.dropna()
# print(studenti)


# Zjisti, kolik prezenčních studentů je v každém z oborů.
# print(studenti.groupby("obor")["příjmení"].count())
print(studenti.groupby("obor").agg({"příjmení": "count", "prospěch": "mean"}))

# Zjisti průměrný prospěch studentů v každém oboru.
print(studenti.groupby("obor")["prospěch"].mean())

# Načti datový set s křestními jmény. Proveď join s tabulkou studentů tak, abychom věděli pohlaví jednotlivých studentů.
jmena = pandas.read_csv("lekce/Lekce11/jmena.csv")
studenti_jmena = pandas.merge(studenti, jmena[["jméno", "pohlaví"]], on = ["jméno"])
print(studenti_jmena)



# Zjisti, zda na naší fakultě studují IT spíše ženy nebo spíše muži.
print(studenti_jmena.groupby("pohlaví").agg({"příjmení": "count"}))


