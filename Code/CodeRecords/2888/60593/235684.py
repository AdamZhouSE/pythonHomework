n,m=map(int,input().split())
arr=list(map(int,input().split()))
ones=0
minus=0
for i in arr:
    if(i==1):
        ones+=1
    else:
        minus+=1
for t in range(m):
    l,r=map(int,input().split())
    if((r-l)%2==0):
        print(0)
    else:
        hf=int((r-l+1)/2)
        if(hf<=ones and hf<=minus):
            print(1)
        else:
            print(0)
