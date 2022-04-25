#https://kodim.cz/czechitas/progr2-python/python-pro-data-1/datum

from datetime import datetime, timedelta
# print(datetime.now())
from datetime import timezone
# print(datetime.now(timezone.utc).astimezone())

from datetime import date
# print(date.today())

# print(datetime(2022, 4, 25, 18))

start_Apolla = datetime(1969, 7, 16, 14, 32)
print(start_Apolla)
# print(start_Apolla.weekday())
# print(start_Apolla.isoweekday())

moje_datum = datetime(1986, 9, 23, 2, 30, 12)
# print(moje_datum)
# print(moje_datum.isoweekday())

# print(start_Apolla.isoformat())
# print(moje_datum.strftime("%d. %m. %Y %H:%M:%S" ))
# print(moje_datum.strftime("%d. %m. %Y %I:%M %p" ))
# print(start_Apolla.strftime("%d. %m. %Y %H:%M"))
# print(start_Apolla.strftime("%d. %m. %Y %I:%M %p"))

# print(moje_datum.strftime("%d. %m. %Y %I:%M %p %A" ))
# print(start_Apolla.strftime("%d. %m. %Y %H:%M %A"))

# import locale
# locale.setlocale(locale.LC_TIME, ('cs_CZ.utf-8')) 
# print(start_Apolla.strftime("%A"))

# https://docs.python.org/3/library/datetime.html#strftime-and-strptime-format-codes

# retezec = "1969-07-21T18:54:00"
# pristani_Apolla = datetime.fromisoformat(retezec)
# print(pristani_Apolla)

retezec_bezny_format = "21. 7. 1969, 18:54"
pristani2_Apolla = datetime.strptime(retezec_bezny_format, "%d. %m. %Y, %H:%M")
print(pristani2_Apolla)

delkaMise = pristani2_Apolla - start_Apolla
print(delkaMise)

dnes = datetime.today()
vcera = dnes - timedelta(days=7)
print(vcera)

dni_na_zemi = dnes - moje_datum
print(dni_na_zemi)




