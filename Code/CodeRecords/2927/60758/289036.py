n,d=map(int,input().split())
k1,b1=-1,2*n-d
k2,b2=-1,d
k3,b3=1,d
k4,b4=1,-d

m=int(input())
for i in range(m):
    x0,y0=map(int,input().split())
    
    if ((k1*x0+b1>=y0 and k2*x0+b2<=y0)or(k1*x0+b1<=y0 and k2*x0+b2>=y0))and((k3*x0+b3>=y0 and k4*x0+b4<=y0)or(k3*x0+b3<=y0 and k4*x0+b4>=y0)):
        print("YES")
    else:
        print("NO")