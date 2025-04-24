import random 
import numpy as np
import matplotlib.pyplot as plt


def f(x):
    return x**3 - 2*x + 2


left, right = 0, 0
while True:
    left = random.randint(-20, 0)
    right = random.randint(0, 20)

    if (left > right):
        left, right = right , left

    if f(left) * f(right) < 0:
        break



def bisection(f, left, right, tol):
    points = []
    for i in range(20):
        mid = (left + right) / 2
        points.append(mid)
        if f(mid) == 0 or (right - left) / 2 < tol:
            break

        if f(right) * f(mid) < 0:
            left = mid
        else:
            right = mid
        
    return points


x = bisection(f, left, right, 0.000001)

curve_x = np.linspace(-20, 20, 41)
curve_y = f(curve_x)

plt.plot(curve_x, curve_y, label="Curve f(x)")
plt.plot(x, [f(xi) for xi in x], 'ro-', label="Bisection points")
plt.axhline(0, color='gray', linestyle='--')
plt.axvline(0, color='gray', linestyle='--')
plt.xlabel("x")
plt.ylabel("f(x)")
plt.legend()
plt.title("Bisection Method Visualization")
plt.grid(True)
plt.show()