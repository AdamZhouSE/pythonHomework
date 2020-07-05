n = int(input())
a, b = [0] * n, [0] * n
for x in range(n ** 2):
    i, j = map(int, input().split())
    if (not a[i - 1]) and (not b[j - 1]):
        print(x + 1, end = ' ')
        a[i - 1] = b[j - 1] = 1
