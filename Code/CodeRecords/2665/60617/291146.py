def penalty_shooter():
    row=input().split(" ")
    X=int(row[0])
    Y=int(row[1])
    Z=int(row[2])
    temp=Z
    resX=0
    resY=0
    while temp!=1:
        if X%temp==0:
            resX+=1
            X-=1
            temp-=1
        else:
            temp-=1
    temp=Z
    while temp!=1:
        if Y%temp==0:
            resY+=1
            Y-=1
            temp-=1
        else:
            temp-=1
    print(resX,end=" ")
    print(resY)

if __name__=='__main__':
    T=int(input())
    for i in range(0,T):
        penalty_shooter()
