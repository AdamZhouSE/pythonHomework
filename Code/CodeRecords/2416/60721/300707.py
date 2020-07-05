m,n=map(int,input().split(" "))
lis=[]
for i in range(0,m):
    lis.append(0)
for i in range(0,n):
    a=int(input())
    lis[a-1]=1
    count=1
    temp=lis[0]
    re=0
    for j in range(1,m):
        if(lis[j]!=temp):
            count+=1
            temp=lis[j]
        else:
            if(count>re):
                re=count
            count=1
    print(re)