n = int(input())
a = [int(i) for i in input().split()]
pair = []
for i in range(n):
    pair.append([i + 1, a[i]])
pair.sort(key=lambda x: x[1])
for i in range(n):
    print(pair[i][0], end=' ')