t = int(input())
for i in range(t):
    x1,y1,x2,y2=[int(x) for x in input().split()]
    k1,k2 = (x1+x2)/2,(y1+y2)/2
    a1,b1,a2,b2=[int(x) for x in input().split()]
    c1,c2 = (a1+a2)/2,(b1+b2)/2
    width = abs(x1-x2)+abs(a1-a2)
    height = abs(y1-y2)+abs(b1-b2)
    print(0 if (2*abs(c1-k1)>=width and  2*abs(c2-k2)>=height) else 1)



