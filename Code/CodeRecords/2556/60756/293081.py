N,K=map(int,input().split())
arr=[]
area=0
for i in range(N):
    x,y=map(int,input().split())
    for p in arr:
        a,b=p
        d1=K-abs(x-a)
        d2=K-abs(y-b)
        if d1>0 and d2>0:
            if area==0:
                area=d1*d2
            else:
                area=-1
                break
    arr.append((x,y))
print(area)