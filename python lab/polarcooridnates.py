import numpy as np
import random
import math

coord = []

for i in range(0, random.randint(10, 15)):
    x = [random.randint(-100, 100), random.randint(-100, 100)]
    coord.append(x)

polar = np.array(coord, dtype=float)
print("Your cartesian coordinates are ")
print(polar)

for i in range(len(polar)):
    x = polar[i][0]
    y = polar[i][1]
    polar[i][0] = math.sqrt(pow(x, 2) + pow(y, 2))
    if (x != 0):
        polar[i][1] = (math.atan(y / x) * 180) / math.pi
    else :
        polar[i][1] = 90


print("The equivalent polar coordinates are:")
print(polar)