def total_price (person, breakfast = False):
    price_one_person = 850
    breakfast_price = 125
    if breakfast:
        sum = person * (price_one_person + breakfast_price)
    else:
        sum = person * price_one_person
    return sum

persons = int(input("Kolik osob? "))
breakfast = bool(input("Snidane? True/ False: "))
print(total_price(persons, breakfast))

