class Auto:
  
  def __init__(self, spz, typ_vozu, pocet_najetych_km):
    self.spz = spz
    self.typ_vozu = typ_vozu
    self.pocet_najetych_km = pocet_najetych_km
    self.volne = True
  
  def __str__(self):
    return f"Registrační značka: {self.spz} \nTyp vozidla: {self.typ_vozu} \nPočet najetých kilometrů: {self.pocet_najetych_km} \nVolné: {'Ano' if self.volne else 'Ne'} \n ================== " 
  
  def pujc_auto(self):
    if self.volne:
      print(f"Potvrzuji zapůjčení vozidla {self.typ_vozu}. \n==================" )
      self.volne = False
    else:
      print(f"Vámi zvolené vozidlo {self.typ_vozu} není momentálně k dispozici.\n==================")
  
  def vrat_auto(self, pocet_km_zapujcka, pocet_dni_zapujceni):
    self.pocet_najetych_km += pocet_km_zapujcka
    self.volne = True
    if pocet_dni_zapujceni < 7:
      cena = 400 * pocet_dni_zapujceni
    else:
      cena = 300 * pocet_dni_zapujceni
    return f"==================\nCelková cena za půčení vozidla: {cena} Kč \nAktuální stav tachometru: {self.pocet_najetych_km} km\n=================="

peugot = Auto("4A2 3020", "Peugeot 403 Cabrio", 47534)
skoda = Auto("1P3 4747", "Škoda Octavia", 41253)

def volba_auta (pozadovane_auto):
  #Funkce prevadi textovy vstup uzivatele na konretni zadany objekt
  if pozadovane_auto == "Škoda":
    return(skoda)
  elif pozadovane_auto == "Peugot":
    return(peugot)
  else:
    print(f"Vámi uvedené vozidlo není v naší nabídce.")
    exit()

def pujceni_auta ():
  pozadovane_auto = volba_auta(input("Jaké auto si přejete půjčit? (Škoda/Peugot): "))    #vstup uzivatele: typ vozu, pomoci fce volba_auta preklad na konkretni objekt
  print(pozadovane_auto)
  pozadovane_auto.pujc_auto() 

def vraceni_auta():
  vracene_auto = volba_auta(input("Jaké auto vracíte? (Škoda/Peugot): "))    #vstup uzivatele: typ vozu, pomoci fce volba_auta preklad na konkretni objekt 
  if vracene_auto.volne:     # kontrola zda byl zvoleny objekt aktulne zapujcen 
    print("==================\nTento vůz nebyl zapůjčen.\n==================")
  else:
    vraceni_km = int(input("Zadejte ujete km: "))
    vraceni_dny = int(input("Zadejte počet dní zápůjčky: "))
    print(vracene_auto.vrat_auto(vraceni_km, vraceni_dny))
    


pujceni_auta()
pujceni_auta()
vraceni_auta()
vraceni_auta()





