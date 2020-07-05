def cross(a,b,c):#跨立实验
    x1=b[0]-a[0]
    y1=b[1]-a[1]
    x2=c[0]-a[0]
    y2=c[1]-a[1]
    return x1*y2-x2*y1 

n=int(input())
for i in range(n):
    a,b,c,d=[0,0],[0,0],[0,0],[0,0]
    a[0],b[0],a[1],b[1]=input().split(' ')
    c[0],c[1],d[0],d[1]=input().split(' ')
    a[0],b[0],a[1],b[1],c[0],d[0],c[1],d[1]=int(a[0]),int(b[0]),int(a[1]),int(b[1]),int(c[0]),int(d[0]),int(c[1]),int(d[1]),
    #快速排斥
    if min(a[0],b[0])<=max(c[0],d[0]) and min(c[1],d[1])<=max(a[1],b[1]) and min(c[0],d[0])<=max(a[0],b[0]) and min(a[1],b[1])<=max(c[1],d[1]):
        if(cross(a,b,c)*cross(a,b,d)<=0
           and cross(c,d,a)*cross(c,d,b)<=0):
            res=1
        else:
            res=0
    else:
        res=0
    print(res)