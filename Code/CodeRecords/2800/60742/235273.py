l0 = input().split()
n = int(l0[0])
d = int(l0[1])
b = input().split()
for i in range(n):
    b[i] = int(b[i])
res = 0
for i in range(1,n):
    while b[i]<=b[i-1]:
        b[i] += d
        res += 1
print (res)