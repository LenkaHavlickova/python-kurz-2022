jmena = ["Michaela", "Jana", "Lenka", "Petr", "Adela", "Jirka"]
emaily = []

for jmeno in jmena:
    email = jmeno.lower() + "@firma.cz"
    emaily.append(email)

print(emaily)

emaily2=[jmeno.lower() + "@firma.cz" for jmeno in jmena]
print(emaily2)



znamky = [0, 2, 4, 1, 0, 3]
citelne_znamky = []

for znamka in znamky:
    citelne_znamky.append(znamka+1)

citelne_znamky2 = [znamka+1 for znamka in znamky]
print(citelne_znamky)
print(citelne_znamky2)

znamky = [[1,3,2,1], [5,2,4,3], [1,1,2,1], [3,2,4,2]]
prumery = []

for student in znamky:
    prumer = sum(student)/len(student)
    prumery.append(prumer)

print(prumery)

prumery2=[sum(student)/len(student) for student in znamky]
print(prumery2)

znamky ={"Lenka":[1,3,2,1], "Jana":[5,2,4,3],"Lota": [1,1,2,1], "Tereza": [3,2,4,2]}

prumery = {}
for student in znamky:
    prumer = sum(znamky[student])/len(znamky[student])
    prumery[student] = prumer

print(prumery)

prumery2 = {student: sum(znamky[student])/len(znamky[student]) for student in znamky}

print(prumery2) 


