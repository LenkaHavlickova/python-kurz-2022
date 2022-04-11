import re
user_name = input("Zadej uzivatelske jmeno: ")

reg_vyraz = re.compile("[a-z]{1,8}")
if reg_vyraz.match(user_name):
    print("OK")
else:
    print("Uživatelské jméno smí obsahovat pouze malá písmena a smí být maximálně 8 znaků dlouhé.")

