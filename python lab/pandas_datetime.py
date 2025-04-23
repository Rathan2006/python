import pandas as pd
import datetime

dt1 = pd.Timestamp('2012-01-15')
print("a) Date time object for Jan 15, 2012:", dt1)

dt2 = pd.Timestamp('2024-12-25 21:20:00')  
print("b) Specific date and time of 9:20 pm:", dt2)

dt3 = pd.Timestamp.now()
print("c) Local date and time:", dt3)

dt4 = pd.to_datetime('2024-04-25').date()
print("d) A date without time:", dt4)

dt5 = pd.Timestamp.today().date()
print("e) Current date:", dt5)

dt6 = pd.Timestamp.now().time()
print("f) Time from a date time:", dt6)

dt7 = datetime.datetime.now().time()
print("g) Current local time (using datetime module):", dt7)
