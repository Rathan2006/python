import numpy as np
import matplotlib.pyplot as plt

np.random.seed(0)
arr_2d = np.random.randint(0, 10, size=(15, 2))
print(arr_2d)
plt.scatter(arr_2d[:, 0], arr_2d[:, 1], color='blue', label='Points')
plt.title('2D Points Plot')
plt.xlabel('X-axis')
plt.ylabel('Y-axis')
plt.legend()
plt.grid(True)
plt.show()
arr_2d += np.array([1, 2])
print(arr_2d)

plt.scatter(arr_2d[:, 0], arr_2d[:, 1], color='blue', label='Points')
plt.title('2D Points Plot')
plt.xlabel('X-axis')
plt.ylabel('Y-axis')
plt.legend()
plt.grid(True)
plt.show()
