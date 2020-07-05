n=int(input())
xy=[[0]*2]*n
for i in range(0,n):
    xy[i]=[int(k) for k in input().split(',')]
k=(xy[0][1]-xy[1][1])/(xy[0][0]-xy[1][0])
re=1
for i in range(1,n):
    if (xy[i][1]-xy[0][1])/(xy[i][0]-xy[0][0])==k:
        re=0
if re==1:
    print("True")
else:
    print("False")