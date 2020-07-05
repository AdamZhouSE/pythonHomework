a=int(input())
b=input().split()
c=input().split()
cola=0
for i in range(a):
    b[i]=int(b[i])
    c[i]=int(c[i])
    cola=cola+b[i]
vol=max(c)
c.remove(vol)
vol+=max(c)
if vol<cola:
    print("NO")
else:
    print("YES")