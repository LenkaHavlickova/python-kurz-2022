import matplotlib.pyplot as plt
import pandas as pd

import requests

r = requests.get("https://raw.githubusercontent.com/lutydlitatova/python-jaro-2022/main/ukoly/data/platy_2021_02.csv")
open("ukoly/platy_2021_02.csv", "wb").write(r.content)

wages = pd.read_csv("ukoly/platy_2021_02.csv")
wages_clr = wages.drop(columns="cislo_zamestnance")
wages_clr.hist(bins=[30000, 35000, 40000, 45000, 50000, 55000, 60000])
# plt.show()

empl_liberec = pd.read_csv("ukoly/zam_liberec.csv")
empl_plzen = pd.read_csv("ukoly/zam_plzeň.csv")
empl_praha = pd.read_csv("ukoly/zam_praha.csv")

empl_liberec["mesto"] = "Liberec"
empl_plzen["mesto"] = "Plzeň"
empl_praha["mesto"] = "Praha"

empl_all = pd.concat([empl_liberec, empl_praha, empl_plzen], ignore_index=True)
wages_town = pd.merge(wages, empl_all[["mesto", "cislo_zamestnance"]], on=["cislo_zamestnance"])
wages_town = wages_town.drop(columns=["cislo_zamestnance"])
wages_town.hist(by="mesto", bins=[30000, 35000, 40000, 45000, 50000, 55000, 60000])
# plt.show()

temp = pd.read_csv("ukoly/temperature.csv")
import pytemperature
temp["AvgTemperatureCelsius"] = pytemperature.f2c(temp["AvgTemperature"])
temp = temp[temp["City"].isin(["Helsinki", "Miami Beach", "Tokyo"])]
temp = temp.drop(columns=["Day", "AvgTemperature"])
temp.plot(kind="box", by = "City")
plt.show()


