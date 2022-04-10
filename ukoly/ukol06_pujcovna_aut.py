file = input("Zadej název textového souboru (včetně cesty, není-li uložen ve stejném adresáři): ")
if file[-4] != '.':
  file += '.txt'
with open (file, encoding='utf-8') as input:
  cars_overview = input.readlines()

cars_overview = [car.split() for car in cars_overview]
cars_overview = [float(car[1].replace(",", "."))for car in cars_overview]
print(f"Auta v tomto roce celkem dohromady najela: {sum(cars_overview)} tis. km")

