file = input("Zadej název zdrojového textového souboru: ")
file_path = "ukoly/" + file
if file_path[-4] != '.':
  file_path += '.txt'
with open (file_path, encoding='utf-8') as input:
  cars_overview = input.readlines()

cars_overview = [car.split() for car in cars_overview]
cars_overview = [float(car[1].replace(",", "."))for car in cars_overview]
print(f"Auta v tomto roce celkem dohromady najela: {sum(cars_overview)} tis. km")

