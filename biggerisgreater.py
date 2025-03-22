def next_permutation(s):
    s = list(s)
    i = len(s) - 2
    while i >= 0 and s[i] >= s[i + 1]:
        i -= 1
    if i == -1:
        return "no answer"
    j = len(s) - 1
    while s[j] <= s[i]:
        j -= 1
    s[i], s[j] = s[j], s[i]
    s[i + 1:].reverse()
    return ''.join(s)

t = int(input("Enter number of test cases: "))
for _ in range(t):
    w = input().strip()
    result = next_permutation(w)
    print(result)
