t = int(input())
for i in range(t):
    x1,y1,x2,y2=[int(x) for x in input().split()]
    len1 = abs(x1-x2)
    k1,k2 = (x1+x2)/2,(y1+y2)/2
    a1,b1,a2,b2=[int(x) for x in input().split()]
    len2 = abs(a1-a2)
    c1,c2 = (a1+a2)/2,(b1+b2)/2
    length = len1+len2
    print(1 if 2*abs(c1-k1)<=length and  2*abs(c2-k2)<=length else 0)



