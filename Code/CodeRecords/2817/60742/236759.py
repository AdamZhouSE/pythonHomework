n = int(input())
f = input().split()
res = "NO"
for i in range(n):
    f[i] = int(f[i])-1
for i in range(n):
    if f[f[i]]!=i and f[f[f[i]]]==i:
        res = "YES"
        break
print (res)