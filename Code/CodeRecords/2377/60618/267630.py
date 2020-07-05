n=int(input())
xy=[[0]*2]*n
for i in range(0,n):
    xy[i]=[int(k) for k in input().split(',')]
k1=(xy[0][1]-xy[1][1])/(xy[0][0]-xy[1][0])
k2=(xy[1][1]-xy[2][1])/(xy[0][1]-xy[1][1])
if xy[0]==xy[1] or xy[1]==xy[2] or xy[2]==xy[0]:
    print("False")
else:
    if k1==k2:
        print("False")
    else:
        print("True")
