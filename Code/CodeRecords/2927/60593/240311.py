def c(a,b,px,py):
    return (b.x-a.x)*(py-a.y)-(px-a.x)*(b.y-a.y)
class point:
    def __init__(self,x,y):
        self.x=x
        self.y=y
n,d=map(int,input().split())
p1=point(0,d)
p2=point(d,0)
p3=point(n,n-d)
p4=point(n-d,n)
m=int(input())
ans=0
for i in range(m):
    xx,yy=map(int,input().split())
    if(c(p1,p2,xx,yy)*c(p3,p4,xx,yy)>=0 and c(p2,p3,xx,yy)*c(p4,p1,xx,yy)>=0):
        ans+=1
print(ans)