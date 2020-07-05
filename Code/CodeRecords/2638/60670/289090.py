n,m=map(int,input().split())
a=list(map(int,input().split()))
for i in range(0,m):
    operation=list(map(int,input().split()))
    if operation[0]==1:
        for j in range(operation[1]-1,operation[2]):
            a[j]+=operation[3]
    else:
        sumn=0
        for j in range(operation[1]-1,operation[2]):
            sumn+=a[j]
        average=sumn/(operation[2]-operation[1]+1)
        if operation[0]==2:
            print("%.4f"%average)
        else:
            variance=0
            for j in range(operation[1]-1,operation[2]):
                variance+=((a[j]-average)**2)
            variance/=(operation[2]-operation[1]+1)
            print("%.4f"%variance)
        