from datetime import datetime, time, timedelta
start_Apolla = datetime(1969, 7, 16, 14, 32)

print(start_Apolla.strftime("%m/%d/%Y"))

start = datetime(2020, 2, 10, 5, 3)
day = start.isoweekday()
print(day)
day_week = start.strftime("%A")
print(day_week)
import locale
locale.setlocale(locale.LC_TIME, ('cs_CZ.utf-8'))
today = datetime.today()
day_week = start.strftime("%A")
print(day_week)
time_from_start = today - start
print(time_from_start)

time_of_order = datetime(2020, 11, 13, 19,47)
holding_order = timedelta(minutes=8, seconds=35)
cooking_time = timedelta(minutes= 25, seconds= 30)
astimate_time_delivery = time_of_order + holding_order + cooking_time
print(astimate_time_delivery)


