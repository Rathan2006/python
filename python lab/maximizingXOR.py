def find_max_xor(L, R):
    max_xor = 0
    for A in range(L, R + 1):
        for B in range(A, R + 1):
            max_xor = max(max_xor, A ^ B)
    return max_xor

L = int(input("Enter L: "))
R = int(input("Enter R: "))
result = find_max_xor(L, R)
print(result)
