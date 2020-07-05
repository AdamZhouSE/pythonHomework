pnum=int(input())
points=[]
for i in range(pnum):
    co=list(map(int,input().split(',')))
    points.append(co)
steps=0
for i in range(pnum-1):
    pax,pay=points[i][0],points[i][1]
    pbx,pby=points[i+1][0],points[i+1][1]
    disx,disy=abs(pbx-pax),abs(pby-pay)
    steps+=max(disx,disy)
print(steps)