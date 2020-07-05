def chongdie(x1,y1,x2,y2,a1,b1,a2,b2):
    if x2<a1 or a2<x1 or b2>y1 or y2>b1:
        print(0)
    else: 
        print(1)

    
T=int(input())
for i in range(T):
    x11,y11,x22,y22=input().split(' ')
    a11,b11,a22,b22=input().split(' ')
    x1=int(x11)
    y1=int(y11)
    x2=int(x22)
    y2=int(y22)
    a1=int(a11)
    b1=int(b11)
    a2=int(a22)
    b2=int(b22)
    chongdie(x1,y1,x2,y2,a1,b1,a2,b2)