l0 = input().split()
n = int(l0[0])
m = int(l0[1])
a = input().split()
b = input().split()
for i in range(n):
    a[i] = int(a[i])
for j in range(m):
    b[j] = int(b[j])
a.sort()
res = [0]*m
for j in range(m):
    while res[j]<n and a[res[j]]<=b[j]:
        res[j] += 1
for j in range(m-1):
    print (res[j],end=" ")
print (res[m-1])