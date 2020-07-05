k=int(input())
for i in range(0,k):
    a,b,m=map(int,input().split())
    count=0
    for j in range(a,b+1):
        if(j%m==0):
            count+=1
    print(count)