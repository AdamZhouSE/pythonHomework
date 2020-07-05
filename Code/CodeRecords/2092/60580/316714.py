a = [0]*200001
f = [0]*200001
v = [0]*200001

n = eval(input())
line = input().split(' ')
x = 200001
for i in range(1,n+1):
    a[i] = int(line[i-1])
for i in range(1,n+1):
    v[i] = 1
    t = i
    p = a[i]
    while(f[p]!=i):
        if f[p]!=0 and f[p]<i:
            break
        v[p] = v[t] + 1
        f[t] = i
        t = p
        p = a[t]
    if f[p]==i and x>v[t]+1-v[p]:
        x = v[t]+1-v[p]
print(x,end = '')