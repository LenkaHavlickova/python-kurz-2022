# https://stage.kodim.cz/kurzy/python-data-1/python-pro-data-1/agregace-a-spojovani

import requests

r = requests.get("https://kodim.cz/czechitas/progr2-python/python-pro-data-1/agregace-a-spojovani/assets/u202.csv")
open("u202.csv", "wb").write(r.content)
r = requests.get("https://kodim.cz/czechitas/progr2-python/python-pro-data-1/agregace-a-spojovani/assets/u203.csv")
open("u203.csv", "wb").write(r.content)
r = requests.get("https://kodim.cz/czechitas/progr2-python/python-pro-data-1/agregace-a-spojovani/assets/u302.csv")
open("u302.csv", "wb").write(r.content)

import pandas
u202 = pandas.read_csv("lekce/Lekce11/u202.csv")
u203 = pandas.read_csv("lekce/Lekce11/u203.csv")
u302 = pandas.read_csv("lekce/Lekce11/u302.csv")

# print(u202)
# print(u202["znamka"].notnull())
# print(u202["znamka"].isnull())
# print(u202["znamka"].notna())
# print(u202[u202["znamka"].isnull()])

# testovaci_data = u202[u202['znamka'].isnull()]
# print(testovaci_data)
# print(testovaci_data.dropna())
# print(testovaci_data.dropna(axis=1))
# print(u202.dropna())
# print(u202.fillna("Neni uvedena hodnota"))

u202 = u202.dropna()
u203 = u203.dropna()
u302 = u302.dropna()

u202["mistnost"] = "u202"
u203["mistnost"] = "u203"
u302["mistnost"] = "u302"
maturita = pandas.concat([u202, u203, u302], ignore_index=True)
# print(maturita)
maturita.to_csv("maturita.csv", index=False)


r = requests.get("https://kodim.cz/czechitas/progr2-python/python-pro-data-1/agregace-a-spojovani/assets/studenti.csv")
open("studenti.csv", "wb").write(r.content)

studenti = pandas.read_csv('lekce/Lekce11/studenti.csv')
# print(studenti)

spojena_data = pandas.merge(u202, studenti)
# print(spojena_data)

r = requests.get("https://kodim.cz/czechitas/progr2-python/python-pro-data-1/agregace-a-spojovani/assets/predsedajici.csv")
open("predsedajici.csv", "wb").write(r.content)

preds = pandas.read_csv('lekce/Lekce11/predsedajici.csv')
# print(preds)
preds["den"] = preds["den"].str.strip()

# novy_propojeny_df = pandas.merge(spojena_data, preds, on=["den"])
novy_propojeny_df = pandas.merge(spojena_data, preds, on=["den"], how="outer")


novy_propojeny_df = novy_propojeny_df.rename(columns={"jmeno_x":"jmeno_studenta", "jmeno_y" : "jmeno_predsedy" })
# print(novy_propojeny_df)

# print(maturita.groupby("predmet")["znamka"].mean())
# print(maturita.groupby("predmet")[["znamka", "cisloStudenta"]].mean())
# print(maturita.groupby("cisloStudenta").agg({"znamka": ["max", "mean"]}))
maturita = maturita.sort_values("predmet", ascending=False)
print(maturita)
