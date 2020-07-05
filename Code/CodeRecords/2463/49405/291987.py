a = list(map(int, input().split(",")))
t = int(input())
n = len(a)
for i in range(n):
    for j in range(i + 1, n):
        if a[i] + a[j] == t:
            print([i + 1, j + 1])
            exit()
print(None)