def cal(x1,y1,x2,y2):
    return x1*y2-x2*y1
def judge(x,y,x1,y1,x2,y2,x3,y3):
    if cal(x-x1,y-y1,x-x2,y-y2)*cal(x-x1,y-y1,x-x3,y-y3)<0 and cal(x-x2,y-y2,x-x3,y-y3)*cal(x-x2,y-y2,x-x1,y-y1)<0 and cal(x-x3,y-y3,x-x2,y-y2)*cal(x-x3,y-y3,x-x1,y-y1)<0:
        return True
    return False
n=int(input())
for _ in range(n):
    res=0
    maxx,maxy=-99999,-99999
    minx,miny=99999,99999
    l1=eval('['+input().replace(' ',',')+']')
    x1,y1=l1[0],l1[1]
    l2 = eval('[' + input().replace(' ', ',') + ']')
    x2, y2 = l2[0], l2[1]
    l3 = eval('[' + input().replace(' ', ',') + ']')
    x3, y3 = l3[0], l3[1]
    maxx=max(x1,x2,x3)
    minx=min(x1,x2,x3)
    maxy=max(y1,y2,y3)
    miny=min(y1,y2,y3)
    for i in range(minx,maxx+1):
        for j in range(miny,maxy+1):
            if judge(i,j,x1,y1,x2,y2,x3,y3):
                res+=1
    print(res)