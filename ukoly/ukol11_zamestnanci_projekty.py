import requests

r = requests.get("https://raw.githubusercontent.com/lutydlitatova/python-jaro-2022/main/ukoly/data/zam_praha.csv")
open("ukoly/zam_praha.csv", "wb").write(r.content)

r = requests.get("https://raw.githubusercontent.com/lutydlitatova/python-jaro-2022/main/ukoly/data/zam_plzeň.csv")
open("ukoly/zam_plzeň.csv", "wb").write(r.content)

r = requests.get("https://raw.githubusercontent.com/lutydlitatova/python-jaro-2022/main/ukoly/data/zam_liberec.csv")
open("ukoly/zam_liberec.csv", "wb").write(r.content)

r = requests.get("https://raw.githubusercontent.com/lutydlitatova/python-jaro-2022/main/ukoly/data/platy_2021_02.csv")
open("ukoly/platy_2021_02.csv", "wb").write(r.content)

import pandas

wages = pandas.read_csv("ukoly/platy_2021_02.csv")
empl_liberec = pandas.read_csv("ukoly/zam_liberec.csv")
empl_plzen = pandas.read_csv("ukoly/zam_plzeň.csv")
empl_praha = pandas.read_csv("ukoly/zam_praha.csv")

empl_liberec["kancelar"] = "Liberec"
empl_plzen["kancelar"] = "Plzeň"
empl_praha["kancelar"] = "Praha"

empl_all = pandas.concat([empl_praha, empl_liberec, empl_plzen], ignore_index=True)
# print(empl_all.shape)
empl_wages = pandas.merge(empl_all, wages, on=["cislo_zamestnance"], how="outer")
# print(empl_wages.shape)
print("Bývalí zaměstnanci:")
ex_empl = empl_wages[empl_wages["plat"].isnull()]
num_ex_empl = ex_empl.shape
print(num_ex_empl)
ex_empl.to_csv("ukoly/ex_empl.csv", index=False)
empl_wages = empl_wages.dropna()
print("")
print("Průměrná mzda v kancelářích:")
print(empl_wages.groupby("kancelar")["plat"].mean())

import requests

r = requests.get("https://raw.githubusercontent.com/lutydlitatova/python-jaro-2022/main/ukoly/data/vykazy.csv")
open("ukoly/vykazy.csv", "wb").write(r.content)

reports = pandas.read_csv("ukoly/vykazy.csv")
print("")
print("Vykazané hodiny na jednotlivých projektech:")
print(reports.groupby("project")["hours"].sum())
empl_project = pandas.merge(empl_all, reports, left_on=["cislo_zamestnance"], right_on=["emloyee_id"], how="outer")
print("")
print("!!!Bývalí zaměstnanci, kteří vykázali hodiny na projektech v únoru, ale za únor nedostali plat:")
ex_empl_project = pandas.merge(ex_empl,reports, left_on=["cislo_zamestnance"],right_on = ["emloyee_id"], how="inner")
print(ex_empl_project)
print("")
print("Počet projektových hodin dle jednotlivých kanceláří (včetně hodin bývalých zaměstnanců):")
print(empl_project.groupby("kancelar")["hours"].sum())

