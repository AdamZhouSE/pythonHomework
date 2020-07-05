import math


def p(x1,y1,x2,y2):
    if x1==x2:
        return abs(y2-y1)-1
    if y2==y1:
        return abs(x2-x1)-1
    return (math.gcd(abs(y2-y1),abs(x2-x1))-1)


t=int(input())
for i in range(t):
    l1 = input().split()
    x1 = int(l1[0])
    y1 = int(l1[1])
    l2 = input().split()
    x2 = int(l2[0])
    y2 = int(l2[1])
    l3 = input().split()
    x3 = int(l3[0])
    y3 = int(l3[1])
    A =   (abs(x1*(y2 - y3) + x2*(y3 - y1) + x3*(y1 - y2))) 
    B=p(x1,y1,x2,y2)+p(x1,y1,x3,y3)+p(x3,y3,x2,y2)+3
    print((A - B + 2) // 2 )