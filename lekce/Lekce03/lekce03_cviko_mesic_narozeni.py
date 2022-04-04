def month_of_birth (rodnecislo):
    druhe_dvojcisli = int(str(rodnecislo)[2] + str(rodnecislo)[3])
    if druhe_dvojcisli > 50:
        mesic = druhe_dvojcisli - 50
    else:
        mesic = druhe_dvojcisli
    return mesic

rodnecislo = int(input("Zadej rodne cislo: "))
mesic = month_of_birth(rodnecislo)
print(f"Mesic narozeni je {mesic}")
