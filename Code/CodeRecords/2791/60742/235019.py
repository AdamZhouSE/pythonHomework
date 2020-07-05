n = int(input())
l = input().split()
l0 = []
for i in range(n):
    l[i] = int(l[i])
for i in range(n):
    if l[i]==1:
        l0.append(i)
t = len(l0)
print (t)
res = []
for j in range(1,t):
    res.append(l[l0[j]-1])
res.append(l[-1])
for j in range(t-1):
    print (res[j],end=" ")
print (res[t-1])