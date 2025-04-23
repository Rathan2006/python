import numpy as np

def generate_odd_magic_square(n):
    magic_square = np.zeros((n, n), dtype=int)
    i, j = 0, n // 2

    for num in range(1, n * n + 1):
        magic_square[i, j] = num
        new_i, new_j = (i - 1) % n, (j + 1) % n
        if magic_square[new_i, new_j]:
            i += 1
        else:
            i, j = new_i, new_j

    return magic_square

def generate_even_magic_square(n):
    magic_square = np.arange(1, n * n + 1).reshape(n, n)
    indices = np.zeros((n, n), dtype=bool)

    for i in range(n):
        for j in range(n):
            if (i < n // 4 or i >= 3 * n // 4) and (j < n // 4 or j >= 3 * n // 4):
                indices[i, j] = True
            elif n // 4 <= i < 3 * n // 4 and n // 4 <= j < 3 * n // 4:
                indices[i, j] = True

    magic_square[indices] = n * n + 1 - magic_square[indices]

    return magic_square

def generate_magic_square(n):
    if n % 2 != 0:
        return generate_odd_magic_square(n)
    elif n % 4 == 0:
        return generate_even_magic_square(n)
    else:
        raise ValueError("Magic squares for even n (not divisible by 4) are not handled by this implementation.")

for n in [4, 5, 6, 7, 8]:
    print(f"Magic Square (N={n}):")
    try:
        magic_square = generate_magic_square(n)
        print(magic_square)
        print("\n")
    except ValueError as e:
        print(e)