a=int(input())
b=[int(x) for x in input().split()]
c=[x for x in b]
c.sort()
position1=b.index(c[0]);position2=b.index(c[a-1])
little=min(position1,position2)
big=max(position1,position2)
temp=max(position2,a-1-position1)
if(temp==0):
    print(b)
else:
    print(max(position2,a-1-position1))