def is_req(p1:list,p2:list):
    if p1==p2:
        return False
    disx=abs(p1[0]-p2[0])
    disy=abs(p1[1]-p2[1])
    mdis=disx+disy
    odis=pow(pow(disx,2)+pow(disy,2),0.5)
    if mdis==odis:return True
    else:return False

cases=int(input())
for i in range(cases):
    pnum=int(input())
    points=[]
    res=0
    for p in range(pnum):
        point=list(map(int,input().split()))
        points.append(point)
    for i in range(pnum-1):
        if i==pnum-2:
            if is_req(points[i],points[i+1]):res+=1
        else:
            for j in range(i+1,pnum):
                if is_req(points[i], points[i + 1]): res += 1
    print(res)