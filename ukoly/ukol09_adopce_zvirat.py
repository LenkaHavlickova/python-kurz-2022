import pandas as pd
path = input("Zadej název adresáře, kde je uložen soubor s daty: (Pokud je ve stejné složce, dej pouze ENTER) ")
if path:
  file = path + "/" + "adopce-zvirat.txt"
else:
  file = "adopce-zvirat.txt"
animals = pd.read_csv(file, sep=';')
print(animals.shape)
print(animals.columns)
print(animals.iloc[34, 1:3])

# BONUS
print("")
animals_bonus = pd.read_csv(file, sep=';', index_col = "nazev_cz")
if animals_bonus.index.is_unique:
  print("Index je unikátní")
else:
  print("Index není unikátní")
print("")
animals_bonus = animals_bonus.sort_index()
print("")
print(animals_bonus.head())
print("")
print(animals_bonus.loc["Outloň váhavý"])
print("")
print(animals_bonus.loc["Želva Smithova":"Želva žlutočelá"])