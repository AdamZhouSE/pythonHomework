mn = input().split(" ")
m = int(mn[0])
n = int(mn[1])
a = input().split(" ")
a = list(map(int, a))
res = []
for i in range(n):
    r = input().split(" ")
    mi = 2147483647
    for j in range(int(r[0])-1, int(r[1])):
        if a[j]<mi:
            mi=a[j]
    res.append(mi)
for i in range(n):
    print(str(res[i])+" ",end="")
