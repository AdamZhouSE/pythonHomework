t=int(input())
for i in range(t):
    li=input().split()
    n=int(li[0])
    x=int(li[1])
    y=int(li[2])
    a=list(map(int,input().split()))
    b=list(map(int,input().split()))
    tmp=[]
    for j in range(n):
        tmp.append(abs(a[j]-b[j]))
    count=0
    while(x!=0 and y!=0):
        mm=max(tmp)
        ind=tmp.index(mm)
        tmp[ind]=-1
        if a[ind]>b[ind]:
            count+=a[ind]
            x-=1
        else:
            count+=b[ind]
            y-=1
    if x==0:
        for j in range(len(tmp)):
            if tmp[j]!=-1:
                count+=b[j]
    else:
        for j in range(len(tmp)):
            if tmp[j]!=-1:
                count+=a[j]
    print(count)
            