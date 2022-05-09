#https://stage.kodim.cz/kurzy/python-data-1/python-pro-data-1/zakladni-dotazy
import pandas

staty = pandas.read_json("lekce/Lekce10/staty.json")
# print(staty.shape)
# staty = staty.set_index("name")
# print(staty.head())
staty = staty.sort_index()
# print(staty.loc["Algeria"])
# print(staty.loc[["Algeria","Czech Republic"], "capital"])
# print(staty[["alpha3Code","region"]])


# print(staty["area"] < 1000)
male_staty = staty[staty["area"]<10000]

lidnate_staty = staty[staty["population"]>1000000]
# print(lidnate_staty)

# print(staty.sort_values("population", ascending=False)[:10]["population"])

# & - and
# | - or

# print(staty[(staty["area"]<10000) & (staty["population"]>1000000)])

# dotaz_na_male_staty = staty["area"] < 10_000
# dotaz_na_lidnate_staty = staty["population"] > 1_000_000

# print(staty[dotaz_na_male_staty & dotaz_na_lidnate_staty])

# dotaz_na_staty_asie = staty["region"] == "Asia"
# dotaz_na_staty_afriky = staty["region"] == "Africa"

# dotaz_na_staty_afriky_asie = staty["region"].isin(["Asia", "Africa"])

# 1. zpusob
# print(staty[dotaz_na_staty_asie | dotaz_na_staty_afriky])
# 2. zpusob
# print(staty[dotaz_na_staty_afriky_asie])
print(staty.head())
print(staty[staty["name"].str.lower().str.startswith("a")])

print(staty["population"].max())
print(staty["population"].min())
print(staty["population"].sum())
print(staty["population"].mean())




