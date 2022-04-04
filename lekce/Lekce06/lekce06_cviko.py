# seznamy cisel

cisla = [1.12, 4.51, 2.64, 13.1, 0.1]

cisla1 = [cislo*2 for cislo in cisla]
print(cisla1)

cisla2 = [cislo*-1 for cislo in cisla]
print(cisla2)

cisla3 = [str(cislo) for cislo in cisla]
print(cisla3)

#retezce
jmena = ['Roman', 'Jan', 'Miroslav', 'Petr', 'Gabriel']
pocty_pismen = [len(jmeno) for jmeno in jmena]
print(pocty_pismen)
velka_jmena = [jmeno.upper() for jmeno in jmena]
print(velka_jmena)
zenska_jmena = [jmeno + "a" for jmeno in jmena]
print(zenska_jmena)

#teploty
teploty = [
  [2.1, 5.2, 6.1, -0.1],
  [2.2, 4.8, 5.6, -1.0],
  [3.3, 6.5, 5.9, 1.2],
  [2.9, 5.6, 6.0, 0.0],
  [2.0, 4.6, 5.5, -1.2],
  [1.0, 3.2, 2.1, -2.0],
  [0.4, 2.7, 1.3, -2.8]
]

prumerne_denni_teploty = [round(sum(denni_teploty)/len(denni_teploty), 1) for denni_teploty in teploty]
print(prumerne_denni_teploty)
ranni_teploty = [denni_teploty[0] for denni_teploty in teploty]
print(ranni_teploty)
poledni_nocni_teploty = [[denni_teploty[1], denni_teploty[3]] for denni_teploty in teploty]
print(poledni_nocni_teploty)

