n=int(input())
def makeLine(st,ed):
    return [ed[0]-st[0],ed[1]-st[1]]
def cross(l1,l2):
    if(l1[0]*l2[1]-l2[0]*l1[1])>0:
        return 1
    elif (l1[0]*l2[1]-l2[0]*l1[1])<0:
        return 0
    else:
        return -1
for i in range(n):
    a=list(map(int,input().split( )))
    b = list(map(int, input().split()))
    c = list(map(int, input().split()))
    x1=min(a[0],b[0],c[0])
    x2=max(a[0],b[0],c[0])
    y1=min(a[1],b[1],c[1])
    y2=max(a[1],b[1],c[1])
    ab=makeLine(a,b)
    ca=makeLine(c,a)
    bc=makeLine(b,c)
    sum=0
    for x in range(x1+1,x2):
        for y in range(y1+1,y2):
            p=[x,y]
            if(cross(ab,makeLine(a,p))==cross(ca,makeLine(c,p))and cross(ca,makeLine(c,p))==cross(bc,makeLine(c,p))):
                sum=sum+1
    print(sum)