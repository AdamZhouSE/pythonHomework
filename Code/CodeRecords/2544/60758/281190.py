n=int(input())
for i in range(0,n):
    x1,y1,x2,y2=map(int,input().split())
    x3,y3,x4,y4=map(int,input().split())
    if(x1!=x2):
        k1=(y1-y2)/(x1-x2)
        b1=y1-k1*x1
    if(x3!=x4):
        k2=(y3-y4)/(x3-x4)
        b2=y3-k2*x3
    if(x3==x4 and x1!=x2):
        if(x3>max(x1,x2) or x3<min(x1,x2)):
            print(0)
        else:
            print(1)
    if(x3!=x4 and x1==x2):
        if(x1>max(x3,x4) or x1<min(x3,x4)):
            print(0)
        else:
            print(1)
    if(x3==x4 and x1==x2):
        if(x1!=x3):
            print(0)
        else:
            print(1)
    if(x3!=x4 and x1!=x2):
        if(k1!=k2):
            x=(b2-b1)/(k1-k2)
            if(x>max(x1,x2) or x<min(x1,x2) or x>max(x3,x4) or x<min(x3,x4)):
                print(0)
            else:
                print(1)
        else:
            if(b1!=b2):
                print(0)
            else:
                print(1)