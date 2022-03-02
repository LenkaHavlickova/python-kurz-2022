baliky = {
    "B541X": True,
    "B547X": False,
    "B251X": False,
    "B501X": True,
    "B947X": False,
}

# package = input("Zadej kód balíku: ")
# if package in baliky:
#   if baliky[package] :           #if baliky[package] == True
#     print(f"Balík s kódem {package} byl předán kurýrovi.")
#   else:
#     print(f"Balík s kódem {package} nebyl dosud předán kurýrovi.")
# else:
#   print(f"Balík s kódem {package} není evidován v našem systému.")

# Navrh na doplneni

num_package = input ("Zadej kód balíku pro zadaní změny: ")
if num_package in baliky:
  if baliky[num_package]:
    confirm_delivery = input("Balík byl již dříve předán kurýrovi. Byl již balík doručen a záznam o balíku je možné smazat? (ano/ne): ")
    if confirm_delivery == "ano":
        baliky.pop(num_package)
        print(f"Balík s číslem {num_package} byl smazán.")
        print(baliky)
    else:
        print(f"Žádná změna na balíku číslo {num_package} nebyla zaznamenána.")
  else:
    confirm_handover = input("Balík ještě nebyl předán kurýrovi. Má být uloženo jeho předání? (ano/ne): ") 
    if confirm_handover == "ano":
       baliky[num_package] = True
       print(f"Balík s číslem {num_package} byl předán.")
       print(baliky)
    else:
        print(f"Žádná změna na balíku číslo {num_package} nebyla zaznamenána.")
else:
  confirm_new = input("Balík s tímto kód zatím není v systému. Chceš balík s tímto kódem založit? (ano/ne): ")
  if confirm_new == "ano":
    baliky[num_package] = False
    print(f"Balík s číslem {num_package} byl uložen do systému")
    print(baliky)
  else:
    print(f"Balík s číslem {num_package} nebyl uložen do systému")


