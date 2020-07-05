n = int(input())
l = input().split()
for i in range(n-1):
    l[i] = int(l[i])
l0 = input().split()
a = int(l0[0])
b = int(l0[1])
res = 0
for i in range(a-1,b-1):
    res += l[i]
print (res)