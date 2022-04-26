from datetime import datetime

first_season_beginning = datetime(2021, 7, 1)
first_season_end = datetime(2021, 8, 10)
first_season_price = 250
second_season_beginning = datetime(2021, 8, 11)
second_season_end = datetime(2021, 8, 31)
second_season_price = 180

print("Letní kino - Prodej vstupenek\n===================")
require_date = input("Zadejte požadované datum ve formátu \"den. měsíc. rok\": ")
require_date_f = datetime.strptime(require_date, "%d. %m. %Y")

if (require_date_f < first_season_beginning ) or (require_date_f > second_season_end):
  print("Tento den je letní kino zavřené.")
  exit()
num_tickets = int(input("Zadejte požadovaný počet lístků: "))
if require_date_f <= first_season_end:
  price = first_season_price
elif second_season_beginning <= require_date_f:
  price = second_season_price

total_price = num_tickets * price
print(f"===================\nCelková cena: {total_price} Kč")
