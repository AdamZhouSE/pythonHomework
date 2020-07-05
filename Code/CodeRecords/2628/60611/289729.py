casenumber=int(input())
for i in range(casenumber):
    count=0
    l=[]
    l.append(list(map(int,input().split(" "))))
    l.append(list(map(int, input().split(" "))))
    l.append(list(map(int, input().split(" "))))
    xmax=max(l[0][0],l[1][0],l[2][0])
    xmin=min(l[0][0],l[1][0],l[2][0])
    ymax = max(l[0][1], l[1][1], l[2][1])
    ymin = min(l[0][1], l[1][1], l[2][1])
    signOfTrig=(l[1][0]-l[0][0])*(l[2][1]-l[0][1])-(l[1][1]-l[0][1])*(l[2][0]-l[0][0])
    for j in range(xmin+1,xmax):
        for k in range(ymin+1,ymax):
            signOfAB=(l[1][0]-l[0][0])*(k-l[0][1])-(l[1][1]-l[0][1])*(j-l[0][0])
            signOfCA = (l[0][0] - l[2][0]) * (k - l[2][1]) - (l[0][1] - l[2][1]) * (j - l[2][0])
            signOfBC = (l[2][0] - l[1][0]) * (k - l[2][1]) - (l[2][1] - l[1][1]) * (j - l[2][0])
            d1=signOfTrig*signOfAB
            d2=signOfTrig*signOfBC
            d3=signOfTrig*signOfCA
            if (d1>0 and d2>0 and d3>0):
                count+=1
    print(count)