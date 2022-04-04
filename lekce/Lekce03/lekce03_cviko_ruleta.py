def roulette (rada, sazka):
    import random
    padlo_cislo= random.randint(0,36)
    print(padlo_cislo)
    prvni_rada = [1 , 4, 7, 10, 13, 16, 19, 22, 25, 28, 31, 34]
    druha_rada = [2, 5, 8, 11, 14, 17, 20, 23, 26, 29, 32, 35]
    treti_rada = [3, 6, 9, 12, 15, 18, 21, 24, 27, 30, 33, 36]
    padla_rada = 0
    if padlo_cislo in prvni_rada:
        padla_rada = 1
    elif padlo_cislo in druha_rada:
        padla_rada = 2
    elif padlo_cislo in treti_rada:
        padla_rada = 3
    else:
        vysledek = 0
    print(padla_rada)
    if rada == padla_rada:
        vysledek = sazka * 2
    else:
        vysledek = 0
    return vysledek


rada = int(input("Na kterou sazis radu: "))
sazka = int(input("Vyse sazky: "))
vyhra = roulette(rada, sazka)
print(f"Vyhravas {vyhra}!")