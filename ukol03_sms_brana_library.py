import phonenumbers
from math import ceil

def phone_number_validation (phone_number):   # phone number validation
  if phone_number[0] != "+":
    phone_number = '+420' + phone_number
  phone_number_pars = phonenumbers.parse(phone_number)
  valid = phonenumbers.is_valid_number(phone_number_pars)
  if valid == False:
    return False
  else:
    possible = phonenumbers.is_possible_number(phone_number_pars)
    return possible

def price_message (message, price_per_sms = 3):     # SMS price calculation  
  lenght_message = len(message)
  num_messages = ceil(lenght_message / 180)
  total_price = num_messages * price_per_sms
  print(f"Zpráva je dlouhá {lenght_message} znaků. Bude rozdělena do {num_messages} zpráv. \nCelková cena za tuto zprávu: {total_price} Kč.")
  return total_price        # just for future extension


price_per_sms = 3
phone_number = input("Zadej telefonní číslo: ")
if phone_number_validation (phone_number) == False:
  print(f"!!! Zadané číslo \"{phone_number}\" není platné !!!")
else:
  price_message(input ("Napiš text krátké zprávy: "), price_per_sms)
