n = int(input())

ar = [0] * (n + 1)

ar[0] = 1
ar[1] = 1

for q in range(2, n + 1):
    ans = 0
    i = 0
    j = q - 1
    while i < q:
        ans += ar[i] * ar[j]
        i += 1
        j -= 1
    ar[q] = ans

print(ar[n]%(10**9 + 7))
