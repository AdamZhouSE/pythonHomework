num=int(input())
res=list()
for i in range(num):
    line1=list(map(int,input().split(" ")))
    line2=list(map(int,input().split(" ")))
    x1 = line1[0]
    y1 = line1[1]
    x2 = line1[2]
    y2 = line1[3]

    x3 = line2[0]
    y3 = line2[1]
    x4 = line2[2]
    y4 = line2[3]

    if x2-x1==0 and x4-x3!=0:
        k2=(y4-y3)/(x4-x3)
        b2=y3-k2*x3
        y=k2*x1+b2
        if y>min(y1,y2) and y<max(y1,y2):
            res.append(1)
        else:
            res.append(0)
    elif x2-x1!=0 and x4-x3==0:
        k1=(y2-y1)/(x2-x1)
        b1=y2-k2*x1
        y=k1*x3+b1
        if y>min(y3,y4) and y<max(y3,y4):
            res.append(1)
        else:
            res.append(0)
    elif x2-x1==0 and x4-x3==0:
        if x2==x3:
            res.append(1)
        else:
            res.append(0)
    else:
        k2 = (y4 - y3) / (x4 - x3)
        b2 = y3 - k2 * x3
        k1 = (y2 - y1) / (x2 - x1)
        b1 = y2 - k1 * x2
        if k1==k2:
            if b1==b2:
                if (x1>=x3 and x1<=x4) or (x3>=x1 and x3<=x2):
                    res.append(1)
                else:
                    res.append(0)
            else:
                res.append(0)
        else:
            x=(b1-b2)/(k2-k1)
            if x>=min(x3,x4) and x<=max(x3,x4) and x>=min(x1,x2) and x<=max(x1,x2):
                res.append(1)
            else:
                res.append(0)
for i in res:
    print(i)