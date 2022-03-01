baliky = {
    "B541X": True,
    "B547X": False,
    "B251X": False,
    "B501X": True,
    "B947X": False,
}

package = input("Zadej kód balíku: ")
if package in baliky:
  if baliky[package] :           #if baliky[package] == True
    print(f"Balík s kódem {package} byl předán kurýrovi.")
  else:
    print(f"Balík s kódem {package} nebyl dosud předán kurýrovi.")
else:
  print(f"Balík s kódem {package} není evidován v našem systému.")