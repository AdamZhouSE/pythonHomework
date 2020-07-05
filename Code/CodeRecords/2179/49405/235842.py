n, m = map(int, (input().split(' ')))
s = input()
for i in range(m):
    a, b, c, d = map(int, (input().split(' ')))
    j = 0
    while j < b - a + 1 and j < d - c + 1:
        if s[a-1:b][j] != s[c-1:d][j]:
            break
        j += 1
    print(j)