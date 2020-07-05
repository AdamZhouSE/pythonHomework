t=int(input())
for i in range(t):
    li=input().split()
    x=int(li[0])
    y=int(li[1])
    z=int(li[2])
    xc=0
    yc=0
    while(z!=1):
        if x%z==0:
            xc+=1
            x-=1
        if y%z==0:
            yc+=1
            y-=1
        z-=1
    print(str(xc)+' '+str(yc))