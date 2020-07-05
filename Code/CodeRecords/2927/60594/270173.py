row=[int(n) for n in input().split()]
n=row[0]
d=row[1]
m=int(input())
for i in range(m):
    row1=[int(n) for n in input().split()]
    x=row1[0]
    y=row1[1]
    if y-x-d<=0 and y-x+d>=0 and y+x-d>=0 and y+x-(2*n-d)<=0:
        print("YES")
    else:
        print("NO")