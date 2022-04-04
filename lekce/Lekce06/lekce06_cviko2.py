with open ("praha.txt", encoding='utf-8') as vstup:
    slohovka = vstup.readlines()

text = [radek.split() for radek in slohovka]
pocet_slov_radek = [len(radek) for radek in text]
print(pocet_slov_radek)
print(sum(pocet_slov_radek))

