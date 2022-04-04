with open("mereni.txt", encoding = 'utf-8') as vstup:
    mereni = vstup.readlines()

# print(mereni)

# radky = [den.strip() for den in mereni]
radky = [den.split() for den in mereni]
radky = [[den[0], float(den[1])] for den in radky]
print(radky)
