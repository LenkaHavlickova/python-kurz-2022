from select import select
import pandas
path = input("Zadej název adresáře, kde je uložen soubor s daty: (Pokud je ve stejné složce, dej pouze ENTER) ")
if path:
  file = path + "/" + "temperature.csv"
else:
  file = "temperature.csv"
temp_file = pandas.read_csv(file)
print(temp_file.head())

# Dotaz na měření, která byla provedena v Praze. Je na datech něco zvláštního? Napadá tě, čím to může být? Zde je nápověda.
print(temp_file[temp_file["City"]=="Prague"])
# Teplota je udaná ve Fahrenheitech.

# Dotaz na měření, ve kterých je teplota (sloupec AvgTemperature) vyšší než 80 stupňů.
print(temp_file[temp_file["AvgTemperature"] > 80])

# Dotaz na měření, ve kterých je teplota vyšší než 60 stupňů a současně bylo měření provedeno v regionu (sloupec Region) Evropa (Europe).
print(temp_file[(temp_file["AvgTemperature"]>60) & (temp_file["Region"]=="Europe")])

# Dotaz na extrémní hodnoty, tj. měření, ve kterých je teplota vyšší než 80 stupňů nebo menší než - 20 stupňů.
print(temp_file[(temp_file["AvgTemperature"]>80) | (temp_file["AvgTemperature"]<-20) & (temp_file["AvgTemperature"] !=-99.0)])
# V případě, že nebyla teplota zaznamenána je ve sloupci "AvgTemperature" hodnota "-99.0". O tyto hodnoty je dle mého názoru vhodné select očistit.)

# BONUS 1
import pytemperature
temp_file["AvgTemperatureCelsius"] = pytemperature.f2c(temp_file["AvgTemperature"])
print(temp_file.head())

# Dotaz na měření, ve kterých je teplota (sloupec AvgTemperatureCelsia) vyšší než 30 stupňů Celsia.
print(temp_file[temp_file["AvgTemperatureCelsius"]>30])

# Dotaz na měření, ve kterých je teplota vyšší než 15 stupňů Celsia a současně bylo měření provedeno v regionu (sloupec Region) Evropa (Europe).
print(temp_file[(temp_file["AvgTemperatureCelsius"]>15) & (temp_file["Region"]=="Europe")])

# Dotaz na extrémní hodnoty, tj. měření, ve kterých je teplota vyšší než 30 stupňů Celsia nebo menší než -10 stupňů. Jsou některé hodnoty podezřelé?
print(temp_file[(temp_file["AvgTemperatureCelsius"]>30) | (temp_file["AvgTemperatureCelsius"]<-10)])
extrem_temp_select = temp_file[(temp_file["AvgTemperatureCelsius"]>30) | (temp_file["AvgTemperatureCelsius"]<-10) & (temp_file["AvgTemperatureCelsius"]!=-72.78)]
extrem_temp_select = extrem_temp_select.sort_values("AvgTemperatureCelsius")
print(extrem_temp_select.tail())
print(extrem_temp_select.head())
#  V případě, že nebyla teplota zaznamenána je ve sloupci "AvgTemperature" hodnota "-99.0" Farhenheit(což je -72.78 stupňů Celsia). O tyto hodnoty je dle mého názoru vhodné select očistit.)

# BONUS 2
# Dotaz na řádky z 13. listopadu 2017 (sloupec Day musí mít hodnotu 13).
print(temp_file[temp_file["Day"]==13])

# Dotaz na řádky z 13. listopadu 2017 ze Spojených států amerických (sloupec Day musí mít hodnotu 13 a sloupec Country hodnotu US). Výsledek dotazu si ulož do nové tabulky a použij ji jako vstup pro následující dotaz.
us_13_select = temp_file[(temp_file["Day"]==13) & (temp_file["Country"]=="US")]
print(us_13_select)


# Pro data z předchozího dotazu napiš dotaz na řádky ve městech (sloupec City) Washington a Philadelphia.
print(us_13_select[us_13_select["City"].isin(["Washington", "Philadelphia"])].drop_duplicates(subset=["City"]))


