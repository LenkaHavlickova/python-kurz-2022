import pandas

names = pandas.read_csv("lekce/Lekce10/jmena.csv", index_col="jméno")
print(names.head())

# Vypište na konzoli informace o jménu Jiří.
print(names.loc["Jiří"])

# Vypište na konzoli informace pro jména Martin, Zuzana a Josef.
print(names.loc[["Martin", "Zuzana", "Josef"]])

# Vypište na konzoli informace o všech nejčastějších jménech až po Martina.
print(names.sort_values("četnost", ascending=False).loc[:"Martin"])


# Vypište pouze průměrné věky osob mající jména mezi Martinem a Terezou.
print(names.loc["Martin":"Tereza"]["věk"])

# Vypište průměrný věk a původ pro všechna jména od Libora dolů.
print(names.loc["Libor":][["věk","původ"]])

# Vypište sloupečky mezi věkem a původem pro všechna jména v tabulce.
# print(names.loc[:,"věk":"původ"])

