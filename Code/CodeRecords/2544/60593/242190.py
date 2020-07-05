t=int(input())
for tt in range(t):
    x1,y1,x2,y2=map(int,input().split())
    x3,y3,x4,y4=map(int,input().split())
    if((min(x1,x2) >= max(x3,x4) and min(y3,y4) <= max(y1,y2) and min(x3,x4) <= max(x1,x2) and min(y1,y2) <= max(y3,y4))):
        ans=False
    fc=(y3-y1)*(x2-x1)-(x3-x1)*(y2-y1)
    fd=(y4-y1)*(x2-x1)-(x4-x1)*(y2-y1)
    if(fc*fd>0):
        ans=False
    else ans=True
    print(1 if ans else 0)
