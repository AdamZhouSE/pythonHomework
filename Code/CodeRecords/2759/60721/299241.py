T=int(input())
for i in range(0,T):
    m,n,a,b=(map(int ,input().split(" ")))
    count=0
    for i in range(m,n+1):
        if(i%a==0 or i%b==0):
            count+=1
    print(count)