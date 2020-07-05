[K, M] = list(map(int, input().split(" ")))
s = input()
n = int(input())
for i in range(0, n):
    [a, b, c] = list(map(int, input().split(" ")))
    copy = s[a:b]
    s = s[0:c] + copy + s[c:]
    if len(s) > M:
        s = s[:M]
print(s[0:K])

