from math import ceil

def validation_phone_number (phone_number):
  phone_number = phone_number.replace(" ", "")
  number_lenght = len(phone_number)
  if phone_number[0:4] == "+420":      #validation lenght
    if number_lenght != 13:
      return False
    else:
      phone_number = phone_number[1:13]
  else:
    if number_lenght != 9:
      return False
  
  if phone_number.isnumeric():      # check if characters are numeric
        return True
  else:
        return False


def price_message (message, price_per_sms = 3):     # SMS price calculation  
  lenght_message = len(message)
  num_messages = ceil(lenght_message / 180)
  total_price = num_messages * price_per_sms
  print(f"Zpráva je dlouhá {lenght_message} znaků. Bude rozdělena do {num_messages} zpráv. \nCelková cena za tuto zprávu: {total_price} Kč.")
  return total_price
  
    
price_per_sms = 3
phone_number = input("Zadej telefonní číslo: ")
if validation_phone_number(phone_number) == False:
  print(f"!!! Zadané číslo \"{phone_number}\" není platné !!!")
else:
  price_message(input ("Napiš text krátké zprávy: "), price_per_sms)
