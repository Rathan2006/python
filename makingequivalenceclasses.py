n = 10000
mod = 5
equivalence_classes = [[] for _ in range(mod)]

for i in range(1, n + 1):
    equivalence_classes[i % mod].append(i)

for i in range(mod):
    print(f"Equivalence class for remainder {i}: {equivalence_classes[i][:10]} ...")


