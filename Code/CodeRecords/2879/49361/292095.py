n = input()
n = int(n)
u = [0 for i in range(10000 + 5)]
v = [0 for i in range(10000 + 5)]
b = [0 for i in range(10000 + 5)]
c = [0 for i in range(10000 + 5)]
d = [0 for i in range(10000 + 5)]
for i in range(n):
    tmp = input()
    tmp = tmp.split(" ")
    u[i] = int(tmp[0])
    v[i] = int(tmp[1])
k = 0
for i in range(n * n):
    if b[u[i]] == 0 and c[v[i]] == 0:
        d[k] = i + 1
        k += 1
        b[u[i]] = 1
        c[v[i]] = 1
for i in range(k - 1):
    print(d[i], end=" ")
print(d[k - 1])
