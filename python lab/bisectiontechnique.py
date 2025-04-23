import numpy as np
import matplotlib.pyplot as plt
import random

def polynomial_function(x):
    return x**3 - 6*x**2 + 11*x - 6

def bisection_method(f, a, b, tolerance=1e-6):
    if f(a) * f(b) >= 0:
        raise ValueError("The function must have different signs at the interval endpoints.")
    updates = []
    while abs(b - a) > tolerance:
        midpoint = (a + b) / 2
        updates.append(midpoint)
        if f(midpoint) == 0:
            break
        elif f(a) * f(midpoint) < 0:
            b = midpoint
        else:
            a = midpoint
    return midpoint, np.array(updates)

random.seed(42)
while True:
    a = random.uniform(-10, 10)
    b = random.uniform(-10, 10)
    if polynomial_function(a) * polynomial_function(b) < 0:
        break

root, updates_array = bisection_method(polynomial_function, a, b)
x_values = np.linspace(-10, 10, 400)
y_values = polynomial_function(x_values)

plt.figure(figsize=(10, 6))
plt.plot(x_values, y_values)
plt.axhline(0, color='black', linestyle='--')
plt.scatter(updates_array, polynomial_function(updates_array), color='red')
plt.xlabel("x")
plt.ylabel("f(x)")
plt.title("Bisection Method - Root Finding Process")
plt.grid()
plt.show()
