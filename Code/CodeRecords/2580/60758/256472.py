a1=int(input())
a2=int(input())
a3=int(input())
xmin=10000
ymin=10000
for i in range(0,a3):
    m=list(map(int,input().split(",")))
    if xmin>m[0]:
        xmin=m[0]
    if ymin>m[1]:
        ymin=m[1]
xmin=min(xmin,a1)
ymin=min(ymin,a2)
print(xmin*ymin)