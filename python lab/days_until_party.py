import pandas as pd
import random
days = [False, False, False, False,False, False, False, False, False, True]
random.shuffle(days)
idx = days.index(True)

daysleft = [0] * 10
for i in range(idx):
    daysleft[i] = idx - i
x = list("DAY" + str(i) for i in range(1, 11))
print(x)

schedule = pd.DataFrame({
"WIll COME?": days,
"DAYS LEFT": daysleft
}, index = x)
print(schedule)