m = input()
n = m.split("+")
n = list(map(int, n))
n_len = len(n)

for i in range(0, n_len-1):
    for j in range(0, n_len-i-1):
        if n[j] > n[j + 1]:
            n[j + 1], n[j] = n[j], n[j + 1]

for i in range(0, n_len-1):
    print(str(n[i]) + "+", end='')

print(n[n_len-1])
