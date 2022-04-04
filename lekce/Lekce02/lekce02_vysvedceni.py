school_report = {
  "Český jazyk": 1,
  "Anglický jazyk": 1,
  "Matematika": 1,
  "Přírodopis": 2,
  "Dějepis": 1,
  "Fyzika": 2,
  "Hudební výchova": 4,
  "Výtvarná výchova": 2,
  "Tělesná výchova": 3,
  "Chemie": 4,
}

soucet_znamka = 0

for znamka in school_report:
    soucet_znamka += school_report[znamka]
    if school_report[znamka] == 1:
        print(znamka)

# print(soucet_znamka)
# pocet_znamek = len(school_report)
# print(pocet_znamek)
# prumer = round(soucet_znamka/pocet_znamek, 2)
# print(prumer)


