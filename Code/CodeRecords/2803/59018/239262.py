n,m=input().split(' ')
a=[]
for i in range(int(n)):
    info=input().split(' ')
    x=[int(y) for y in info]
    for j in range(1,x[0]+1):
        a.append(x[j])

b=set(a)
c=list(b)
c.sort()
if len(c)<int(m):
    print("NO")
else:
    print("YES")
        
        
        
    