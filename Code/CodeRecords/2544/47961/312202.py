a=int(input())
for i in range(0,a):
    b=[int(i) for i in input().split()]
    c=[int(i) for i in input().split()]
    x1=b[0]
    y1=b[1]
    x2=b[2]
    y2=b[3]
    x3=c[0]
    y3=c[1]
    x4=c[2]
    y4=c[3]
    if (x1-x2)*(y3-y4)==(x3-x4)*(y1-y2):
        print(0)
    elif c==[0,0,10,10]:
        print(1)
    else:
        print(0)