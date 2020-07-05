n = int(input())
a = [int(i) for i in input().split()]
pair = []
for i in range(n):
    pair.append([i + 1, a[i]])
pair.sort(key=lambda x: x[1])
res = ""
for i in range(n):
    res+=(str(pair[i][0])+" ")
res = res[0:-1]
print()