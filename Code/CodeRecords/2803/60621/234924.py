a=[int(x) for  x in input().split()]
row,num=a[0],a[1]
c=set()
for i in range(row):
    b=[int(x) for  x in input().split()]
    c.update(b[1:])
if(len(c)==num):
    print("YES")
else:
    print("NO")